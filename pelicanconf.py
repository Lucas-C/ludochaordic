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
    {'img_url': 'images/readings/BDArcaneMajeureT1couv.jpg', 'description': 'Arcane Majeure - Jean-Pierre Pécau & Damien Jacob (BD)', 'date': '2019-07-26'},
    {'img_url': 'images/readings/vanille_ou_chocolat.jpg', 'description': 'Vanille ou chocolat ? - Jason Shiga (BD)', 'date': '2019-06-15'},
    {'img_url': 'images/readings/gits.jpeg', 'description': 'The Ghost in the Shell - Shirow Matsamune (manga)', 'date': '2019-06-05'},
    {'img_url': 'images/readings/Jerome-K-Jerome-Bloche-integrale-t2.jpg', 'description': "Jérôme K. Jérôme Bloche - L'intégrale Tome 2 - Dodier (BD)", 'date': '2019-05-19'},
    {'img_url': 'images/readings/irl-cover.jpg', 'description': 'In real life - Cory Doctorow & Jen Wang (BD)', 'date': '2019-05-03'},
    {'img_url': 'images/readings/PourLaScience-HS-LOrdredCacheDesNombres.jpg', 'description': "Pour la Science - Hors Série n°103 - L'ordre caché des nombres", 'date': '2019-04-28'},
    {'img_url': 'images/readings/dedale-1-doki.jpg', 'description': 'Dédale - Takamichi (manga)', 'date': '2019-03-29'},
    {'img_url': 'images/readings/spacetrawler.jpg', 'description': 'Spacetrawler - Christopher Baldwin (webcomic)', 'date': '2019-03-10'},
    {'img_url': 'images/readings/VilleVermine_t1.jpg', 'description': 'VilleVermine tome 1/2 - Julien Lambert (BD)', 'date': '2019-02-07'},
    {'img_url': 'images/readings/Reinventing_Comics_Scott_McCloud_book_cover_art.jpg', 'description': 'Reinventing Comics - Scott McCloud (BD)', 'date': '2019-02-01'},
    {'img_url': 'images/readings/goupil_ou_face_couv.jpg', 'description': 'Goupil ou Face - Lou Lubie (BD)', 'date': '2019-01-20'},
    {'img_url': 'images/readings/CanardPC-15ans.jpg', 'description': 'Canard PC - Hors Série 15 ans', 'date': '2019-01-05'},
    {'img_url': 'images/readings/revue-dessinee-couv-no21-2018-automne.png', 'description': 'Nantes - Balades urbaines de Sarah Guilbaud (livre sur le Street Art)', 'date': '2018-10-16'},
    {'img_url': 'images/readings/nantes-balades-urbaines.jpg', 'description': 'Nantes  (Revue BD)', 'date': '2018-10-22'},
    {'img_url': 'images/readings/cité14.jpg', 'description': 'Cité 14 - Pierre Gabus & Romuald Reutimann (BD)', 'date': '2018-07-17'},
    {'img_url': 'images/readings/gloutons-et-dragons.jpg', 'description': 'Gloutons & Dragons - Ryoko Kui (manga)', 'date': '2018-07-05'},
    {'img_url': 'images/readings/tony-chu-tome-7.jpg', 'description': 'Tony Chu - Tome 7 - John Layman & Rob Guillory (BD)', 'date': '2018-06-15'},
    {'img_url': 'images/readings/au-pays-des-ombres.jpg', 'description': 'Au Pays des Ombres - Mathis & Thierry Martin (BD)', 'date': '2018-06-13'},
    {'img_url': 'images/readings/les_larmes_de_nuwa.jpg', 'description': 'Les Larmes de Nüwa - Benjamin Jurdic & Manuro (BD dont vous êtes le héro)', 'date': '2018-06-02'},
    {'img_url': 'images/readings/saga-tome-8.jpg', 'description': 'Saga - tome 8 - Fiona Staples & Brian K. Vaughan (BD)', 'date': '2018-05-05'},
    {'img_url': 'images/readings/enquetes-generales.jpg', 'description': 'Enquêtes Générales - Immersion au cœur de la brigade de répression du banditisme - Raynal Pellicer & Titwane (BD)', 'date': '2018-04-21'},
    {'img_url': 'images/readings/six-gun-gorilla.jpg', 'description': 'Six-Gun Gorilla - Simon Spurrier & Jeff Stokely (BD)', 'date': '2018-04-08'},
    {'img_url': 'images/readings/dans-la-combi-de-thomas-pesquet.jpg', 'description': 'Dans la combi de Thomas Pesquet - Marion Montaigne (BD)', 'date': '2018-03-02'},
    {'img_url': 'images/readings/Pantheon.jpg', 'description': 'Panthéon! - Hamish Steele (BD)', 'date': '2018-02-16'},
    {'img_url': 'images/readings/desobeisseurs-du-service-public.jpg', 'description': 'Les désobéisseurs du service public (BD)', 'date': '2018-02-02'},
    {'img_url': 'images/readings/l-art-internet.jpg', 'description': "L'Art Internet - Rachel Greene", 'date': '2017-11-14'},
    {'img_url': 'images/readings/The-Thrilling-Adventures-of-Lovelace-and-Babbage.jpg', 'description': 'The Thrilling Adventures of Lovelace and Babbage: The (Mostly) True Story of the First Computer', 'date': '2017-11-16'},
)  # ends READINGS

# Blogroll
LINKS = (('Blog BD de Boulet', 'http://www.bouletcorp.com'),
         ('Shaarli de sebsauvage', 'http://sebsauvage.net/links'),
         ("Justin Mason's Weblog", 'http://taint.org'),
         ('Sam & Max @Twitter', 'https://twitter.com/sam_et_max'),
         ('Hugin & Munin', 'http://hu-mu.blogspot.fr'),
         ('Derrière le paravent de Greg Pogorzelski', 'http://awarestudios.blogspot.fr'),
         ('La partie du lundi', 'https://lapartiedulundi.wordpress.com'),
         ('OuJeViPo', 'http://oujevipo.fr'),
         ('Neal Krawetz Hacker Factor Blog', 'http://www.hackerfactor.com/blog/'),
         ('J.P. Villain (Access42) @Twitter', 'https://twitter.com/villainjp'),
         ('Blog de David Larlet', 'https://larlet.fr/david/blog/'),
         ('Reflets.info', 'https://reflets.info'),
         ('Tristan Nitot', 'http://standblog.org/blog/post/'),
         ('Blog de Victor Stinner', 'http://vstinner.readthedocs.io'),
         ('Rhizome.org', 'https://anthology.rhizome.org'),
         ('Jeff Atwodd Coding Horror', 'http://blog.codinghorror.com'),
         ("Du Monde Dans l'Objectif", 'http://www.dumondedanslobjectif.com'),
         ("Galerie d'Elliot Jolivet aka 10seï", 'https://illutensei.com'),
         ("Galerie d'Elodie Olivier", 'http://elodie-olivier.com'),)

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
OUTPUT_PATH = './output'

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
STATIC_CHECK_IF_MODIFIED = True # create links instead of copying files
STATIC_CREATE_LINKS = True # compare mtimes of content and output files, and only copy content files that are newer than existing output files
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True
