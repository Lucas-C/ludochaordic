#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import logging, os
from os.path import dirname, join

logging.root.setLevel(logging.INFO)

AUTHOR = 'Lucas Cimon'
SITENAME = 'Ludochaordic'
SITESUBTITLE = 'Fantaisies programatico-ludiques'
DESCRIPTION = '''
<a href="pages/bienvenue.html">Bienvenue</a> !
<br>
En vrac, ce blog traite de <a href="tag/prog.html">programmation</a>, et particulièrement du <a href="tag/python.html">langage Python</a>,
de <a href="tag/jeux.html">jeux</a> (<a href="tag/jeu-de-societe.html">jeux société</a>, <a href="tag/jdr.html">jeux de rôle</a> et <a href="tag/logic-puzzle.html">puzzles logiques</a>)
et parfois un peu même de <a href="tag/maths.html">mathématiques</a>.
<br>
Vous trouverez également ici <a href="pages/jeux-de-role.html">mes créations de jeux de rôle</a>,
les <a href="pages/slides.html">slides</a> de présentations que j'ai donné,
et <a href="past_readings.html">mes lectures passés</a>.
<br>
Enfin, je partage des liens et des actualités sur mon <a href="https://chezsoi.org/shaarli/">Shaarli</a>.
<br>
<small><em>(you can selectively display English articles by clicking <a href="?lang=en">the LANG button above</a>)</em></small>
<br>
<small><em>(les mots en bleu ci-dessus sont des liens cliquables, visitez-les !</em>😉<em>)</em></small>
'''

AVATARS = [
    'images/avatar.jpeg',
    'images/avatar.jfif',
]

# Readings, from most recent to oldest
READINGS = (
    {'date': u'2021-01-26', 'img_url': 'images/readings/Sombre6.jpg', 'description': "Sombre n°6 - Johan Scipion (JdR)"},
    {'date': u'2021-02-18', 'img_url': 'images/readings/lhyperreve.jpg', 'description': "L'Hyperrêve - Marc-Antoine Mathieu (BD)"},
    {'date': u'2020-12-27', 'img_url': 'images/readings/le-chateau-des-animaux.jpg', 'description': "Le château des animaux - Deleps & Dorison (BD)"},
    {'date': u'2020-11-21', 'img_url': 'images/readings/broadway.jpg', 'description': "Broadway - Fabrice Caro (roman)"},
    {'date': u'2020-10-19', 'img_url': 'images/readings/la-zad.jpg', 'description': "La ZAD - C'est plus grand que nous - Rochepeau & Azuélos (BD)"},
    {'date': u'2020-10-06', 'img_url': 'images/readings/kiffe-ton-cycle.jpg', 'description': 'Kiffe ton cycle - Gaëlle Baldassari'},
    {'date': u'2020-09-20', 'img_url': 'images/readings/contre-lalternumerisme.jpg', 'description': 'Contre l’alternumérisme - Julia Laïnae & Nicolas Alep'},
    {'date': u'2020-07-15', 'img_url': 'images/readings/alors-voila.jpg', 'description': 'alors voilà - Les 1001 vies des Urgences - Baptiste Beaulieu (roman)'},
    {'date': u'2020-06-09', 'img_url': 'images/readings/Dirty-MJ-COVER-1.jpg', 'description': 'Dirty MJ - John Wick (essai)'},
    {'date': u'2020-05-24', 'img_url': 'images/readings/SandmanPreludesNocturnes.jpg', 'description': 'Sandman - Preludes & Nocturnes - Neil Gaiman (comics)'},
    {'date': u'2020-05-13', 'img_url': 'images/readings/LesSciencesCaNousRegarde.jpg', 'description': 'Les sciences, ça nous regarde - Lionel LARQUÉ & Dominique PESTRE'},
    {'date': u'2020-04-14', 'img_url': 'images/readings/la-consolante.jpg', 'description': 'La Consolante - Anna Gavalda (roman)'},
    {'date': u'2020-04-08', 'img_url': 'images/readings/Aama.jpg', 'description': 'Aâma - Frederik Peeters (BD)'},
    {'date': u'2020-03-14', 'img_url': 'images/readings/A-la-vie.jpg', 'description': "À la vie ! - L'Homme étoilé (BD)"},
    {'date': u'2020-03-02', 'img_url': 'images/readings/LastMan12.jpg', 'description': 'Last Man tome 12 - Balak & Sanlaville & Vivès (BD)'},
    {'date': u'2020-01-21', 'img_url': 'images/readings/chronosquad.jpg', 'description': 'Chronosquad - Giorgio Albertini & Grégory Panaccione (BD)'},
    {'date': u'2019-12-28', 'img_url': 'images/readings/infinity8_tome5.jpg', 'description': 'Infinity 8 - tome 5 - Lewis Trondheim & Davy Mourier & Lorenzo De Felici (BD)'},
    {'date': u'2019-12-22', 'img_url': 'images/readings/mamada.jpg', 'description': 'Mamada - David Ratte (BD)'},
    {'date': u'2019-12-14', 'img_url': 'images/readings/garduno.jpg', 'description': 'Garduno - Philippe Squarzoni (BD)'},
    {'date': u'2019-11-30', 'img_url': 'images/readings/ian.jpg', 'description': 'Ian - Fabien Vehlmann & Ralph Meyer (BD)'},
    {'date': u'2019-11-20', 'img_url': 'images/readings/hitman.jpg', 'description': 'Hitman - Closing Time - Garth Ennis & John McCrea (Comics)'},
    {'date': u'2019-10-25', 'img_url': 'images/readings/demon.gif', 'description': 'Demon - Jason Shiga (BD)'},
    {'date': u'2019-10-13', 'img_url': 'images/readings/Fiasco_cover.gif', 'description': 'Fiasco - Jason Morningstar (JdR)'},
    {'date': u'2019-10-05', 'img_url': 'images/readings/density.jpg', 'description': 'Density - Lewis TRONDHEIM & Stan VINCE (BD)'},
    {'date': u'2019-09-02', 'img_url': 'images/readings/happycratie.jpg', 'description': 'Happycratie - Edgar Cabanas & Eva Illouz'},
    {'date': u'2019-09-02', 'img_url': 'images/readings/energie-changeons-de-cap.jpg', 'description': 'Energie Changeons de cap ! - Didier Lenoir'},
    {'date': u'2019-09-02', 'img_url': 'images/readings/reality-is-broken.jpg', 'description': 'Reality is broken - Jane Mc Gonigal'},
    {'date': u'2019-08-05', 'img_url': 'images/readings/Hillbilly_t3.jpg', 'description': 'Hillbilly tome 3 - Eric Powell (BD)'},
    {'date': u'2019-07-26', 'img_url': 'images/readings/BDArcaneMajeureT1couv.jpg', 'description': 'Arcane Majeure - Jean-Pierre Pécau & Damien Jacob (BD)'},
    {'date': u'2019-06-15', 'img_url': 'images/readings/vanille_ou_chocolat.jpg', 'description': 'Vanille ou chocolat ? - Jason Shiga (BD)'},
    {'date': u'2019-06-05', 'img_url': 'images/readings/gits.jpeg', 'description': 'The Ghost in the Shell - Shirow Matsamune (manga)'},
    {'date': u'2019-05-19', 'img_url': 'images/readings/Jerome-K-Jerome-Bloche-integrale-t2.jpg', 'description': "Jérôme K. Jérôme Bloche - L'intégrale Tome 2 - Dodier (BD)"},
    {'date': u'2019-05-03', 'img_url': 'images/readings/irl-cover.jpg', 'description': 'In real life - Cory Doctorow & Jen Wang (BD)'},
    {'date': u'2019-04-28', 'img_url': 'images/readings/PourLaScience-HS-LOrdredCacheDesNombres.jpg', 'description': "Pour la Science - Hors Série n°103 - L'ordre caché des nombres"},
    {'date': u'2019-03-29', 'img_url': 'images/readings/dedale-1-doki.jpg', 'description': 'Dédale - Takamichi (manga)'},
    {'date': u'2019-03-10', 'img_url': 'images/readings/spacetrawler.jpg', 'description': 'Spacetrawler - Christopher Baldwin (webcomic)'},
    {'date': u'2019-02-07', 'img_url': 'images/readings/VilleVermine_t1.jpg', 'description': 'VilleVermine tome 1/2 - Julien Lambert (BD)'},
    {'date': u'2019-02-01', 'img_url': 'images/readings/Reinventing_Comics_Scott_McCloud_book_cover_art.jpg', 'description': 'Reinventing Comics - Scott McCloud (BD)'},
    {'date': u'2019-01-20', 'img_url': 'images/readings/goupil_ou_face_couv.jpg', 'description': 'Goupil ou Face - Lou Lubie (BD)'},
    {'date': u'2019-01-05', 'img_url': 'images/readings/CanardPC-15ans.jpg', 'description': 'Canard PC - Hors Série 15 ans'},
    {'date': u'2018-10-16', 'img_url': 'images/readings/revue-dessinee-couv-no21-2018-automne.png', 'description': 'Nantes - Balades urbaines de Sarah Guilbaud (livre sur le Street Art)'},
    {'date': u'2018-10-22', 'img_url': 'images/readings/nantes-balades-urbaines.jpg', 'description': 'Nantes  (Revue BD)'},
    {'date': u'2018-07-17', 'img_url': 'images/readings/cité14.jpg', 'description': 'Citée 14 - Pierre Gabus & Romuald Reutimann (BD)'},
    {'date': u'2018-07-05', 'img_url': 'images/readings/gloutons-et-dragons.jpg', 'description': 'Gloutons & Dragons - Ryoko Kui (manga)'},
    {'date': u'2018-06-15', 'img_url': 'images/readings/tony-chu-tome-7.jpg', 'description': 'Tony Chu - Tome 7 - John Layman & Rob Guillory (BD)'},
    {'date': u'2018-06-13', 'img_url': 'images/readings/au-pays-des-ombres.jpg', 'description': 'Au Pays des Ombres - Mathis & Thierry Martin (BD)'},
    {'date': u'2018-06-02', 'img_url': 'images/readings/les_larmes_de_nuwa.jpg', 'description': 'Les Larmes de Nüwa - Benjamin Jurdic & Manuro (BD dont vous êtes le héro)'},
    {'date': u'2018-05-05', 'img_url': 'images/readings/saga-tome-8.jpg', 'description': 'Saga - tome 8 - Fiona Staples & Brian K. Vaughan (BD)'},
    {'date': u'2018-04-21', 'img_url': 'images/readings/enquetes-generales.jpg', 'description': 'Enquêtes Générales - Immersion au cœur de la brigade de répression du banditisme - Raynal Pellicer & Titwane (BD)'},
    {'date': u'2018-04-08', 'img_url': 'images/readings/six-gun-gorilla.jpg', 'description': 'Six-Gun Gorilla - Simon Spurrier & Jeff Stokely (BD)'},
    {'date': u'2018-03-02', 'img_url': 'images/readings/dans-la-combi-de-thomas-pesquet.jpg', 'description': 'Dans la combi de Thomas Pesquet - Marion Montaigne (BD)'},
    {'date': u'2018-02-16', 'img_url': 'images/readings/Pantheon.jpg', 'description': 'Panthéon! - Hamish Steele (BD)'},
    {'date': u'2018-02-02', 'img_url': 'images/readings/desobeisseurs-du-service-public.jpg', 'description': 'Les désobéisseurs du service public (BD)'},
    {'date': u'2017-11-14', 'img_url': 'images/readings/l-art-internet.jpg', 'description': "L'Art Internet - Rachel Greene"},
    {'date': u'2017-11-16', 'img_url': 'images/readings/The-Thrilling-Adventures-of-Lovelace-and-Babbage.jpg', 'description': 'The Thrilling Adventures of Lovelace and Babbage: The (Mostly) True Story of the First Computer'},
)  # ends READINGS

# Blogroll
LINKS = (("Justin Mason's Weblog", 'http://taint.org'),
         ('Neal Krawetz Hacker Factor Blog', 'http://www.hackerfactor.com/blog/'),
         ('Shaarli de sebsauvage', 'http://sebsauvage.net/links'),
         ('Hugin & Munin', 'http://hu-mu.blogspot.fr'),
         ('Radio Rôliste', 'https://www.radio-roliste.net'),
         ("C'est pas du jeu de rôle", 'https://www.cestpasdujdr.fr'),
         ('Trop Long ; Pas Lu !', 'http://troplongpaslu.fr'),
         ('The Indie RPG Pipeline', 'https://theindierpgpipeline.blogspot.com'),
         ('Derrière le paravent de Greg Pogorzelski', 'http://awarestudios.blogspot.fr'),
         ('Warpdoor', 'http://warpdoor.com'),
         ('AlphaBetaGamer', 'https://www.alphabetagamer.com'),
         ('OuJeViPo', 'http://oujevipo.fr'),
         ('Du papier et des jeux', 'https://pnpfrance.wordpress.com'),
         ('Blog BD de Boulet', 'http://www.bouletcorp.com'),
         ('J.P. Villain (Access42) @Twitter', 'https://twitter.com/villainjp'),
         ('Blog de David Larlet', 'https://larlet.fr/david/blog/'),
         ('No Limit Secu', 'https://www.nolimitsecu.fr'),
         ('Reflets.info', 'https://reflets.info'),
         ('Tristan Nitot', 'http://standblog.org/blog/'),
         ('Blog de Victor Stinner', 'http://vstinner.github.io'),
         ('Rhizome.org', 'https://anthology.rhizome.org'),
         ("Du Monde Dans l'Objectif", 'https://www.dumondedanslobjectif.com'),
         ("Galerie d'Elliot Jolivet aka Tenseï", 'https://illutensei.com'),
         ("Galerie d'Elodie Olivier", 'https://elodie-olivier.com'),)
         # ('John Carmack', 'https://twitter.com/id_aa_carmack/'),
         # ('Jane McGonigal', 'https://twitter.com/avantgame'),
         # ('Antoine Bauza', 'https://twitter.com/Toinito'),

SOCIAL = (('shaarli', 'https://chezsoi.org/shaarli'),
          ('github', 'https://github.com/Lucas-C'),
          ('wikipedia', 'https://fr.wikipedia.org/wiki/Utilisateur:Dr_max_kurt'),
          ('itchio', 'https://lucas-c.itch.io'),
          ('stackoverflow', 'https://stackoverflow.com/users/636849/lucas-cimon'),
          ('discord', 'https://discord.com/invite/BJeuEtX'),
          ('linkedin', 'https://www.linkedin.com/in/lucascimon'),
          ('reddit', 'https://www.reddit.com/user/lucas-c/posts/'))
          # ('reddit', 'https://www.reddit.com/user/drmaxkurt/posts/'),
          # ('deviantart', 'https://www.deviantart.com/drmaxkurt/favourites'),
          # ('travis-ci', 'https://travis-ci.com/Lucas-C'),

SUPPORTS = (('LaQuadratureDuNet', 'https://soutien.laquadrature.net', 'images/logo_la-quadrature-du-net_20x20.png', 'Faites un don à la Quadrature !'),
            ('Framasoft', 'https://soutenir.framasoft.org/liste-temoignages', 'images/button_80x15_framasoft.png', 'Soutenez Framasoft !'),
            ('April', 'https://www.april.org/adherer', 'images/cartouche_april-jadhere.png', 'Promouvoir et soutenir le logiciel libre'),
            ('Microformats', 'http://microformats.org/', 'images/microformats.png', 'Ce site adhère au standard microformats'),
            ('Webmention', 'https://indieweb.org/Webmention', 'images/webmention-button.svg', 'Ce site adhère au standard Webmention'),
            ('Low-tech', 'https://www.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website.html', 'images/low-tech.svg', 'Ce site adhère à la philosophie low-tech'))

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

PINGBACK_URL = 'https://webmention.io/chezsoi.org_lucas_blog_/xmlrpc'
WEBMENTION_URL = 'https://webmention.io/chezsoi.org_lucas_blog_/webmention'

# microformats info for h-card:
COUNTRY = 'France'
LOCALITY = 'Saint-Mathurin-sur-Loire'
SHORT_BIO = 'Software engineer. Tabletop RPG writer. Love libre software, and especially Python 🐍. Currently working for oui.sncf @Nantes'

PATH = './content'
OUTPUT_PATH = './output'

MARKDOWN = {
    'extensions': ['mdx_include'],
    'extension_configs': {
        'mdx_include': {
            'base_path': 'content/'
        },
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.tables': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ('ctags_generator', 'deadlinks', 'image_process', 'representative_image', 'tag_cloud') #, 'w3c_validate')

DEADLINK_VALIDATION = False  # à activer de temps en temps via "inovke build" inclus quelques faux positifs
DEADLINK_OPTS = {}           # cf. https://github.com/silentlamb/pelican-deadlinks#settings

IMAGE_PROCESS = {
    'thumb': ['scale_out 300 300 False'],
}

LINKBACKS_CACHEPATH = os.environ.get('LINKBACKS_CACHEPATH')

THEME = '../pelican-mg'
DIRECT_TEMPLATES = ('index', 'tagcloud', 'past_readings')
DEFAULT_PAGINATION = False

ISSO_BASE_URL = '/lucas/isso'
ISSO_REQUIRE_AUTHOR = True
ENABLE_COMMENTS_ON_PAGES = True
WEBMENTION_IO_API_KEY = '_nitaHZFJP92imjlL6OlGQ'

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

IGNORE_FILES = ['github-project-statistics-and-python-interactive-coding', 'github-stats.html']


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
