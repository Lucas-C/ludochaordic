# -*- coding: utf-8 -*-

import os
import shutil
import sys

from invoke import task
from invoke.main import program
from pelican import main as pelican_main
from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer
from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

def pelican_run(c, cmd):
    cmd += ' ' + program.core.remainder  # allows to pass-through args to pelican
    # cf. https://github.com/getpelican/pelican/pull/2600
    try:
        pelican_main(cmd.split(' '))
    except TypeError:
        c.run('pelican ' + cmd)

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS = {}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_SETTINGS = get_settings_from_file(SETTINGS_FILE_BASE)
SETTINGS.update(LOCAL_SETTINGS)
SETTINGS.update({k:v for k, v in os.environ.items() if k != 'PATH'} )  # useful to override OUTPUT_PATH with an env variable

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': 'publishconf.py',
    # Output path. Can be absolute or relative to tasks.py. Default: 'output'
    'deploy_path': SETTINGS['OUTPUT_PATH'],
    # Port for `serve`
    'port': 8000,
}

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(CONFIG['deploy_path']):
        shutil.rmtree(CONFIG['deploy_path'])
        os.makedirs(CONFIG['deploy_path'])

@task
def build(c, only_src_paths=None):  # CLI usage: invoke build --only-src-paths content/01.md,content/02.md
    """Build local version of site"""
    cmd = '-s {settings_base} -o {deploy_path}'.format(**CONFIG)
    if only_src_paths:
        only_out_paths = [src2out(path) for path in only_src_paths.split(',')]
        cmd += ' -w ' + ','.join(only_out_paths)
    pelican_run(c, cmd)

def src2out(path):  # Sadly custom to my filename-to-slug naming convention, can hardly made generic
    filename = path.split('/', 2)[-1]
    if filename.startswith('20'):
        filename = '-'.join(filename.split('-')[3:])
    return CONFIG['deploy_path'] + '/' + filename.replace('.md', '.html')

@task
def rebuild(c):
    """`build` with the delete switch"""
    pelican_run(c, '-d -s {settings_base}'.format(**CONFIG))

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    pelican_run(c, '-r -s {settings_base}'.format(**CONFIG))

@task
def serve(c):
    """Serve site at http://localhost:$PORT/ (default port is 8000)"""

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        CONFIG['deploy_path'],
        ('', CONFIG['port']),
        ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {port} ...\n'.format(**CONFIG))
    server.serve_forever()

@task
def reserve(c):
    """`build`, then `serve`"""
    build(c)
    serve(c)

@task
def publish(c):
    """Build production version of site"""
    pelican_run(c, '-s {settings_publish} -o {deploy_path}'.format(**CONFIG))
    with open(CONFIG['deploy_path'] + '/tagcloud.html') as tagcloud_file:
        tagcloud_lines = extract_lines_between(tagcloud_file.readlines(), '<ul class="mg-tagcloud">', '</ul>')
    with open(CONFIG['deploy_path'] + '/pages/bienvenue.html', 'r+') as bienvenue_file:
        bienvenue_lines = insert_after_line(bienvenue_file.readlines(), '<!-- tagcloud -->', tagcloud_lines)
        bienvenue_file.seek(0)
        bienvenue_file.write(''.join(bienvenue_lines))
        bienvenue_file.truncate()

def extract_lines_between(in_lines, start_line_content, end_line_content):
    out_lines = []
    inbetween = False
    for line in in_lines:
        if start_line_content in line:
            inbetween = True
        if inbetween:
            out_lines.append(line)
        if inbetween and end_line_content in line:
            break
    return out_lines

def insert_after_line(in_lines, target_line_content, add_lines):
    out_lines = []
    for line in in_lines:
        out_lines.append(line)
        if target_line_content in line:
            out_lines.extend(add_lines)
    return out_lines

@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server
    build(c)
    server = Server()
    # Watch the base settings file
    server.watch(CONFIG['settings_base'], lambda: build(c))
    # Watch content source files
    content_file_extensions = ['.md', '.rst']
    for extension in content_file_extensions:
        content_blob = '{0}/**/*{1}'.format(SETTINGS['PATH'], extension)
        # Relies on https://github.com/lepture/python-livereload/pull/204
        server.watch(content_blob, lambda paths: build(c, paths.join(',')))
    # Watch the theme's templates and static assets
    theme_path = SETTINGS['THEME']
    server.watch('{}/templates/*.html'.format(theme_path), lambda: build(c))
    static_file_extensions = ['.css', '.js']
    for extension in static_file_extensions:
        static_file = '{0}/static/**/*{1}'.format(theme_path, extension)
        server.watch(static_file, lambda: build(c))
    # Serve output path on configured port
    server.serve(port=CONFIG['port'], root=CONFIG['deploy_path'])
