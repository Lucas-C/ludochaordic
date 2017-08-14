#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lucas Cimon'
SITENAME = 'Ludochaordic'
SITESUBTITLE = 'Fantaisies programatico-ludiques'
DESCRIPTION = 'programmation, maths, jeux de société et de rôle'

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

SUPPORTS = (('LaQuadratureDuNet', 'https://soutien.laquadrature.net', 'images/logo_la-quadrature-du-net_20x20.png', 'Faites un don à la Quadrature !'),
            ('Framasoft', 'https://soutenir.framasoft.org/liste-temoignages', 'images/button_80x15_framasoft.png', 'Soutenez Framasoft !'),
            ('April', 'http://www.april.org/adherer', 'http://www.april.org/files/cartouche_april-jadhere.png', 'Promouvoir et soutenir le logiciel libre'))

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

PATH = './content'

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['image_process', 'representative_image', 'tag_cloud']

IMAGE_PROCESS = {
    'thumb': ['scale_out 300 300 False'],
}
IMAGE_PROCESS_EXCLUDE = ['tipue_search.json']

THEME = '../pelican-mg'
DIRECT_TEMPLATES = ('index', 'search', 'tagcloud', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'
ISSO_BASE_URL = '/lucas/isso'
TAG_CLOUD_STEPS = 6
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = True
MG_NO_EXCERPT = True
MG_DISABLE_SUMMARY = True
MG_FILTER_TAGS = ['jeux', 'maths', 'prog']
MG_LANG_FILTER_TAGS = ['fr', 'en']  # 'lang:'-prefixed tags

ARCHIVE_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
CATEGORY_SAVE_AS = ''

DEFAULT_PAGINATION = False


#######################################
# Config options specific to dev-mode:
#######################################

SITEURL = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

