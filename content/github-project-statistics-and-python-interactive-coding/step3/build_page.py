#!/usr/bin/env python3
import argparse, json, os, sys, webbrowser
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
    dummy_data = [
        ( "2019-01-01", 1   ),
        ( "2019-02-01", 4   ),
        ( "2019-03-01", 9   ),
        ( "2019-04-01", 16  ),
        ( "2019-05-01", 25  ),
        ( "2019-06-01", 36  ),
        ( "2019-07-01", 49  ),
        ( "2019-08-01", 64  ),
        ( "2019-09-01", 81  ),
        ( "2019-10-01", 100 ),
        ( "2019-11-01", 121 ),
        ( "2019-12-01", 144 ),
    ]
    github_stats['open_issues_count_over_time'] = dummy_data
    github_stats['closed_issues_count_over_time'] = dummy_data
    github_stats['open_prs_count_over_time'] = dummy_data
    github_stats['closed_prs_count_over_time'] = dummy_data
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
