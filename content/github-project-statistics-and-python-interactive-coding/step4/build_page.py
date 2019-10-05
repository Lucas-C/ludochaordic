#!/usr/bin/env python3
import argparse, json, os, sys, webbrowser
from collections import defaultdict
from itertools import count
from os.path import dirname, join, realpath

from jinja2 import Environment, FileSystemLoader
from livereload import Server
import requests
from xreload import xreload


PARENT_DIR = dirname(realpath(__file__))


def main():
    args = parse_args()
    build_page(args)
    if args.watch_and_serve:
        watch_and_serve(args)

def parse_args(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('org_repo', help='Format: $org/$repo similar to https://github.com/$org/$repo')
    parser.add_argument('--use-dump', action='store_true')
    parser.add_argument('--watch-and-serve', action='store_true')
    return parser.parse_args(argv)  # reads sys.argv

def build_page(args):
    github_stats = read_dump()
    if not github_stats or not args.use_dump:
        github_stats = get_github_stats(args.org_repo)
        write_dump(github_stats)
    generate_html(pre_process(github_stats))

def get_github_stats(org_repo):
    github_stats = {'org_repo': org_repo, 'issues': []}
    headers = {'Authorization': 'token ' + os.environ['GITHUB_OAUTH_TOKEN']} if 'GITHUB_OAUTH_TOKEN' in os.environ else None
    for page in count(1):
        response = requests.get('https://api.github.com/repos/{}/issues?state=all&page={}'.format(org_repo, page), headers=headers)
        if response.status_code == 403:
            print(response.json(), file=sys.stderr)
        response.raise_for_status()
        issues = response.json()
        if issues:
            github_stats['issues'].extend(issues)
        else:
            break
    return github_stats

def pre_process(github_stats):
    issues_per_creation_day = defaultdict(list)
    for issue in github_stats['issues']:
        creation_day = issue['created_at'].split('T')[0]
        issues_per_creation_day[creation_day].append(issue)
    open_issues_count_over_time, closed_issues_count_over_time = [], []
    open_prs_count_over_time, closed_prs_count_over_time = [], []
    open_issues_count, closed_issues_count = 0, 0
    open_prs_count, closed_prs_count = 0, 0
    for day in sorted(issues_per_creation_day.keys()):
        open_issues_count += len([issue for issue in issues_per_creation_day[day]
                                        if 'pull_request' not in issue])
        open_issues_count_over_time.append((day, open_issues_count))
        closed_issues_count += len([issue for issue in issues_per_creation_day[day]
                                          if 'pull_request' not in issue and issue['state'] == 'closed'])
        closed_issues_count_over_time.append((day, closed_issues_count))
        open_prs_count += len([issue for issue in issues_per_creation_day[day]
                                     if 'pull_request' in issue])
        open_prs_count_over_time.append((day, open_prs_count))
        closed_prs_count += len([issue for issue in issues_per_creation_day[day]
                                       if 'pull_request' in issue and issue['state'] == 'closed'])
        closed_prs_count_over_time.append((day, closed_prs_count))
    github_stats['open_issues_count_over_time'] = open_issues_count_over_time
    github_stats['closed_issues_count_over_time'] = closed_issues_count_over_time
    github_stats['open_prs_count_over_time'] = open_prs_count_over_time
    github_stats['closed_prs_count_over_time'] = closed_prs_count_over_time
    return github_stats

def write_dump(dump_data):
    with open(join(PARENT_DIR, 'dump.json'), 'w+') as json_file:
        return json.dump(dump_data, json_file)

def read_dump():
    try:
        with open(join(PARENT_DIR, 'dump.json')) as json_file:
            return json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def generate_html(github_stats):
    env = Environment(loader=FileSystemLoader(PARENT_DIR))
    with open(join(PARENT_DIR, 'page.html'), 'w') as output_file:
        output_file.write(env.get_template('template.html').render(github_stats))

def watch_and_serve(args):
    server = Server()
    server.watch('template.html', lambda: build_page(args))
    server.watch(__file__,        lambda: reload_script() and build_page(args))
    webbrowser.open('http://localhost:5500/page.html')
    server.serve(root=PARENT_DIR, port=5500)

def reload_script():
    return xreload(sys.modules[__name__], new_annotations={'RELOADING': True})


if __name__ == '__main__' and 'RELOADING' not in __annotations__:
    main()
