#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import dirname, join

AUTHOR = 'Lucas Cimon'
SITENAME = 'Ludochaordic'
SITESUBTITLE = 'Fantaisies programatico-ludiques'
DESCRIPTION = 'programmation, maths, jeux de société et de rôle'

AVATARS = [
    'images/avatar.jpeg',
    'images/avatar.jfif',
]

# Readings, from most recent to oldest
READINGS = (
    {'img_url': 'images/readings/tony-chu-tome-7.jpg', 'description': 'Tony Chu - Tome 7 - John Layman & Rob Guillory (BD)'},
    {'img_url': 'images/readings/au-pays-des-ombres.jpg', 'description': 'Au Pays des Ombres - Mathis & Thierry Martin (BD)'},
    {'img_url': 'images/readings/les_larmes_de_nuwa.jpg', 'description': 'Les Larmes de Nüwa - Benjamin Jurdic & Manuro (BD dont vous êtes le héro)'},
    {'img_url': 'images/readings/saga-tome-8.jpg', 'description': 'Saga - tome 8 - Fiona Staples & Brian K. Vaughan (BD)'},
    {'img_url': 'images/readings/enquetes-generales.jpg', 'description': 'Enquêtes Générales - Immersion au cœur de la brigade de répression du banditisme - Raynal Pellicer & Titwane (BD)'},
    {'img_url': 'images/readings/six-gun-gorilla.jpg', 'description': 'Six-Gun Gorilla - Simon Spurrier & Jeff Stokely (BD)'},
    {'img_url': 'images/readings/dans-la-combi-de-thomas-pesquet.jpg', 'description': 'Dans la combi de Thomas Pesquet - Marion Montaigne (BD)'},
    {'img_url': 'images/readings/Pantheon.jpg', 'description': 'Panthéon! - Hamish Steele (BD)'},
    {'img_url': 'images/readings/desobeisseurs-du-service-public.jpg', 'description': 'Les désobéisseurs du service public (BD)'},
    {'img_url': 'images/readings/l-art-internet.jpg', 'description': "L'Art Internet - Rachel Greene"},
    {'img_url': 'images/readings/The-Thrilling-Adventures-of-Lovelace-and-Babbage.jpg', 'description': 'The Thrilling Adventures of Lovelace and Babbage: The (Mostly) True Story of the First Computer'},
)

# Blogroll
LINKS = (('Blog BD de Boulet', 'http://www.bouletcorp.com'),
         ('Shaarli de sebsauvage', 'http://sebsauvage.net/links'),
         ("Justin Mason's Weblog", 'http://taint.org'),
         ('Sam & Max @Twitter', 'https://twitter.com/sam_et_max'),
         ('Hugin & Munin', 'http://hu-mu.blogspot.fr'),
         ('Derrière le paravent de Greg Pogorzelski', 'http://awarestudios.blogspot.fr'),
         ('OuJeViPo', 'http://oujevipo.fr'),
         ('Neal Krawetz Hacker Factor Blog', 'http://www.hackerfactor.com/blog/'),
         ('J.P. Villain (Access42) @Twitter', 'https://twitter.com/villainjp'),
         ('Blog de David Larlet', 'https://larlet.fr/david/blog/'),
         ('Reflets.info', 'https://reflets.info'),
         ('Tristan Nitot', 'http://standblog.org/blog/post/'),
         ('Blog de Victor Stinner', 'http://vstinner.readthedocs.io'),
         ('Rhizome.org', 'https://anthology.rhizome.org'),
         ('Jeff Atwodd Coding Horror', 'http://blog.codinghorror.com'),
         ("Galerie photo de CheckSam", 'http://www.dumondedanslobjectif.com'),
         ("Galerie d'Elliot Jolivet aka 10seï", 'https://www.behance.net/10sei'),
         ("Galerie d'Elodie Olivier", 'http://elodie-olivier.com'),
         ('Galerie de Camille Cesbron', 'http://camillecesbron.wix.com/peintreillustratrice'),)

SOCIAL = (('shaarli', 'https://chezsoi.org/shaarli'),
          ('youtube', 'https://www.youtube.com/playlist?list=FLF8xTv55ZmwikWWmWLPEAZQ'),
          ('github', 'https://github.com/Lucas-C'),
          ('stackoverflow', 'http://stackoverflow.com/users/636849/lucas-cimon'),
          ('travis-ci', 'https://travis-ci.org/Lucas-C'),
          ('linkedin', 'https://www.linkedin.com/in/lucascimon'))

SUPPORTS = (('LaQuadratureDuNet', 'https://soutien.laquadrature.net', 'images/logo_la-quadrature-du-net_20x20.png', 'Faites un don à la Quadrature !'),
            ('Framasoft', 'https://soutenir.framasoft.org/liste-temoignages', 'images/button_80x15_framasoft.png', 'Soutenez Framasoft !'),
            ('April', 'http://www.april.org/adherer', 'images/cartouche_april-jadhere.png', 'Promouvoir et soutenir le logiciel libre'))

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

PATH = './content'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ('ctags_generator', 'image_process', 'representative_image', 'tag_cloud')

IMAGE_PROCESS = {
    'thumb': ['scale_out 300 300 False'],
}

THEME = '../pelican-mg'
DIRECT_TEMPLATES = ('index', 'tagcloud', 'past_readings')
DEFAULT_PAGINATION = False

ISSO_BASE_URL = '/lucas/isso'

TAG_CLOUD_STEPS = 6
TAG_CLOUD_SORTING = 'alphabetically'
TAG_CLOUD_BADGE = True

MG_NO_EXCERPT = True
MG_DISABLE_SUMMARY = True
MG_FILTER_TAGS = ['jeux', 'maths', 'prog']
MG_LANG_FILTER_TAGS = ['fr', 'en']  # 'lang:'-prefixed tags

CATEGORY_SAVE_AS = ''
ARCHIVE_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
EXTRA_ATOM_FEED = {
    'name': 'Shaarli',
    'url': 'https://chezsoi.org/shaarli/?do=atom'
}


#######################################
# Config options specific to dev-mode:
#######################################

SITEURL = ''
RELATIVE_URLS = True

# Making output generation faster:
TAG_SAVE_AS = ''
FEED_ALL_ATOM = None
STATIC_CHECK_IF_MODIFIED = True # pending pelican 3.8.0 release
STATIC_CREATE_LINKS = True # pending pelican 3.8.0 release
WRITE_SELECTED = [join(dirname(__file__), 'output', f) for f in (
    'index.html',
    'tagcloud.html',
    'past_readings.html',
    'pages/bienvenue.html',
    'pages/jdr-blades-in-the-dark.html',
    'pages/net-art.html',
    'pages/slides.html',

    'traduction-du-temple-du-non-une-histoire-interactive-twine-du-studio-crows-crows-crows.html',
)]
