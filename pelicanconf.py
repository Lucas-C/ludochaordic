#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lucas Cimon'
SITENAME = 'Ludochaordic'
SITESUBTITLE = 'Fantaisies programatico-ludiques'
DESCRIPTION = 'programmation, maths, jeux de société et de rôle'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

THEME = '/root/pelican-mg'

PLUGIN_PATHS = ['/root/pelican-plugins']
PLUGINS = ['sitemap', 'tipue_search']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Shaarli de sebsauvage', 'http://sebsauvage.net/links'),
         ("Justin Mason's Weblog", 'http://taint.org'),
         ('J.P. Villain (Access42) @Twitter', 'https://twitter.com/villainjp'),
         ('Sam & Max', 'https://twitter.com/sam_et_max'),
         ('Blog de David Larlet', 'https://larlet.fr/david/blog/'),
         ('Reflets.info', 'https://reflets.info'),
         ('Hugin & Munin', 'http://hu-mu.blogspot.fr'),
         ('Neal Krawetz Hacker Factor Blog', 'http://www.hackerfactor.com/blog/'),
         ('Jeff Atwodd Coding Horror', 'http://blog.codinghorror.com'),
         ("Galerie d'Elodie Olivier", 'http://elodie-olivier.com'),
         ("Galerie d'Elliot Jolivet aka 10seï", 'https://www.behance.net/10sei'),
         ('Galerie de Camille Cesbron', 'http://camillecesbron.wix.com/peintreillustratrice'),)

# Social widget
SOCIAL = (('github', 'https://github.com/Lucas-C'),
          ('linkedin', 'https://www.linkedin.com/in/lucascimon'),
          ('stackoverflow', 'http://stackoverflow.com/users/636849/lucas-cimon'),
          ('shaarli', 'https://chezsoi.org/shaarli'),
          ('youtube', 'https://www.youtube.com/playlist?list=FLF8xTv55ZmwikWWmWLPEAZQ'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

