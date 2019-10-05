#!/usr/bin/env python3
import argparse, sys, webbrowser
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

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--watch-and-serve', action='store_true')
    return parser.parse_args()  # reads sys.argv

def build_page(args):
    env = Environment(loader=FileSystemLoader(PARENT_DIR))
    with open(join(PARENT_DIR, 'page.html'), 'w') as output_file:
        output_file.write(env.get_template('template.html').render(name='Bob'))

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
