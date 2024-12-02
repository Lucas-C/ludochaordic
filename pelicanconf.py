#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import logging, os
from os.path import dirname, join

logging.root.setLevel(logging.INFO)
logging.getLogger('pelican.utils').setLevel(logging.WARN)  # avoids verbose "-> Copying ..." logs
logging.getLogger('tornado.access').setLevel(logging.WARN)  # avoids verbose HTTP logs from livereload server
# Configure LOG_FORMAT to prefix it with "%(asctime)s [%(module)s]":
# (TODO : PR to Pelican to allow this to be easily configured)
if logging.root.handlers:  # handlers are only set the 2nd time this file is evaluated by Pelican
    formatter = logging.root.handlers[0].formatter
    formatter._fmt = formatter._style._fmt = "%(asctime)s [%(name)s] %(levelname)s %(message)s"

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
<small><em>(les mots en bleu ci-dessus sont des liens cliquables, visitez-les ! </em>😉<em>)</em></small>
'''

EXTRA_PAGE_LINKS = (
    ("Découvertes vidéoludiques", "https://chezsoi.org/shaarli/?searchtags=GreatOnes"),
    ("Gopher access (beta)", "gopher://chezsoi.org/"),
)

# Readings, from most recent to oldest - BEWARE: descriptions should NOT contain double quotes "", or HTML alt/title attributes will break
READINGS = (
    # {'date': '2024-05-?', 'img_url': 'images/readings/', 'description': 'Thèque 2 - Nick Seaver - Robin James - Laura Forlano - Julie Le Baron (Essai)'}, # https://audimat-editions.fr/catalogue/teque2
    {'date': '2024-11-23', 'img_url': 'images/readings/LesBataillesDuRail.jpg', 'description': 'Les batailles du rail - Le Monde diplomatique (Revue)'},
    {'date': '2024-11-02', 'img_url': 'images/readings/Paranormal.jpg', 'description': 'Paranormal - Dan Christensen - tomes 1/2/3 (BD)'},
    {'date': '2024-10-28', 'img_url': 'images/readings/Bookhunter.jpg', 'description': 'Bookhunter - Jason Shiga (BD)'},
    {'date': '2024-10-14', 'img_url': 'images/readings/SaisonBrune.jpg', 'description': 'Saison Brune - Philippe Squarzoni (BD)'},
    {'date': '2024-09-27', 'img_url': 'images/readings/CeNestPasToiQueJattendais.jpg', 'description': "Ce n'est pas toi que j'attendais - Fabien Toulmé (BD)"},
    {'date': '2024-09-08', 'img_url': 'images/readings/Bourdieu-UneEnqueteAlgerienne.jpg', 'description': 'Bourdieu : une enquête algérienne - Pascal Génot & Olivier Thomas (BD)'},
    {'date': '2024-09-07', 'img_url': 'images/readings/BouleDeFeu.jpg', 'description': 'Boule de feu - Anouk Ricard & Etienne Chaize (BD)'},
    {'date': '2024-08-06', 'img_url': 'images/readings/Birdking.jpg', 'description': 'Birdking - Daniel Freedman & CROM (BD)'},
    {'date': '2024-06-14', 'img_url': 'images/readings/PetitManuelDAutoDefenseEnInterrogatoire.webp', 'description': "Petit manuel d'autodéfense en interrogatoire - Éditions du commun (essai)"},
    {'date': '2024-05-03', 'img_url': 'images/readings/LaFilleMauditeDuCapitainePirate.png', 'description': 'La Fille Maudite Du Capitaine Pirate - Jeremy Bastian (BD)'},
    {'date': '2024-04-25', 'img_url': 'images/readings/ParadisPerdu.jpg', 'description': "ParadisPerdu - Anthony 'Yno' Combrexelle (JdR)"},
    {'date': '2024-04-08', 'img_url': 'images/readings/bleu-a-la-lumiere-du-jour.jpg', 'description': 'Bleu à la lumière du jour - Borja Gonzalez (BD)'},
    {'date': '2024-04-02', 'img_url': 'images/readings/MadMaxiJack.jpg', 'description': 'Mad Maxi Jack - Étienne Beck (BD)'},
    {'date': '2024-03-13', 'img_url': 'images/readings/TheLastRonin.jpg', 'description': 'TMNT: The Last Ronin - Kevin Eastman & Peter Laird & Tom Waltz (comics)'},
    {'date': '2024-02-27', 'img_url': 'images/readings/PrettyDeadly3.jpg', 'description': 'Pretty Deadly Volume 3 The Rat - Kelly Sue DeConnick & Emma Rios (comics)'},
    {'date': '2024-01-07', 'img_url': 'images/readings/Sombre12.jpg', 'description': 'Sombre n°12 - Johan Scipion (JdR)'},
    {'date': '2023-11-13', 'img_url': 'images/readings/LesContesDuGivre.jpg', 'description': 'Les Contes du Givre - Josselin Billard (BD)'},
    {'date': '2023-10-21', 'img_url': 'images/readings/pepin-et-olivia-t1.jpg', 'description': 'Pépin et Olivia - Camille Jourdy (BD)'},
    {'date': '2023-10-15', 'img_url': 'images/readings/Lau-dela_JasonShiga.jpg', 'description': "L'au-delà - Jason Shiga (BD)"},
    {'date': '2023-09-30', 'img_url': 'images/readings/le-mythe-de-l-rsquo-ossuaire-des-milliers-de-plumes-noires.jpg', 'description': "Des milliers de plumes noires - Jeff Lemire & Andrea Sorrentino (BD)"},
    {'date': '2023-08-21', 'img_url': 'images/readings/pour-quelques-degres-de-plus.jpg', 'description': "Pour quelques degrés de plus - Ulysse Gry (BD)"},
    {'date': '2023-08-11', 'img_url': 'images/readings/animan.jpg', 'description': "Animan - Anouk Ricard (BD)"},
    {'date': '2023-08-02', 'img_url': 'images/readings/moi-ce-que-jaime-cest-les-monstres.jpg', 'description': "Moi, ce que j'aime, c'est les monstres - Emil Ferris (BD)"},
    {'date': '2023-07-29', 'img_url': 'images/readings/LesPhilanthropesAuxPochesPercees.jpeg', 'description': "Les philanthropes aux poches percées - Scarlett & Sophie Rickard (BD)"},
    {'date': '2023-07-28', 'img_url': 'images/readings/bd-frontier.jpg', 'description': "Frontier - Guillaume Singelin (BD)"},
    {'date': '2023-05-11', 'img_url': 'images/readings/GameEngineBlackBook-Wolfenstein3D.jpg', 'description': "Game Engine Black Book : Wolfenstein3 D - Fabien Sanglard (essai)"},
    {'date': '2023-04-24', 'img_url': 'images/readings/Flic-L-histoire-vraie-du-journaliste-qui-a-infiltre-la-police.jpg', 'description': " Flic - L'histoire vraie du journaliste qui a infiltré la police - Valentin Gendrot & Thierry Chavant (BD)"},
    {'date': '2023-01-25', 'img_url': 'images/readings/la-naissance-en-bd.jpg', 'description': "La Naissance en BD - Lucile Gomez (BD)"},
    {'date': '2022-12-10', 'img_url': 'images/readings/Considerations-sur-les-fleches-de-lamour.jpg', 'description': "Considérations sur les flèches de l’amour Broché – Ibn al Rabin (BD)"},
    {'date': '2022-11-15', 'img_url': 'images/readings/jusquici-tout-allait-bien.jpg', 'description': "Jusqu'ici tout allait bien - Ersin Karabulut (BD)"},
    {'date': '2022-10-09', 'img_url': 'images/readings/juliette.jpg', 'description': "Juliette - Camille Jourdy (BD)"},
    {'date': '2022-09-26', 'img_url': 'images/readings/Leviathan.jpg', 'description': "Léviathan - Jason Shiga (BD dont vous êtes le héro)"},
    {'date': '2022-09-07', 'img_url': 'images/readings/RosalieBlum.jpg', 'description': "Rosalie Blum - Camille Jourdy (BD)"},
    {'date': '2022-07-20', 'img_url': 'images/readings/LaCantineDeMinuit.jpg', 'description': "La Cantine De Minuit - Yarô Abe (manga)"},
    {'date': '2022-06-05', 'img_url': 'images/readings/ShadowLife.jpg', 'description': "Shadow life - Ann Xu & Hiromi Goto (manga)"},
    {'date': '2022-05-14', 'img_url': 'images/readings/LaHordeDuContrevent.jpg', 'description': "La horde du Contrevent - Alain Damasio (roman)"},
    {'date': '2022-03-21', 'img_url': 'images/readings/on-ne-nait-pas-grosse.jpg', 'description': "On ne naît pas grosse - Gabrielle Deydier (essai)"},
    {'date': '2022-02-20', 'img_url': 'images/readings/le-monde-sans-fin.jpg', 'description': "Le monde sans fin - Blain & Jancovici (BD)"},
    {'date': '2022-02-14', 'img_url': 'images/readings/facing-the-titan.png', 'description': "Face au Titan - Nicolas Ronvel (JdR)"},
    {'date': '2022-02-03', 'img_url': 'images/readings/s-occuper-de-son-sperme.jpg', 'description': "S’occuper de son sperme et être contracepté.e - éditions Leslie Bhar (essai)"},
    {'date': '2021-12-29', 'img_url': 'images/readings/Strangers_in_Paradise.jpg', 'description': "Strangers in paradise - Terry Moore (BD)"},
    {'date': '2021-12-27', 'img_url': 'images/readings/ion-mud.jpg', 'description': "Ion Mud - Amaury Bündgen (BD)"},
    {'date': '2021-12-21', 'img_url': 'images/readings/FaussesPistes.jpg', 'description': "Fausses pistes - Duhamel (BD)"},
    {'date': '2021-11-15', 'img_url': 'images/readings/encore-des-patates.webp', 'description': "Encore des patates !? Pour une Sécurité Sociale de l'Alimentation (BD)"},
    {'date': '2021-08-22', 'img_url': 'images/readings/the-private-eye.jpg', 'description': "The Private Eye - Brian K Vaughan &  Marcos Martin (BD)"},
    {'date': '2021-08-16', 'img_url': 'images/readings/DoggyBags-tome13.jpg', 'description': "Doggybags tome 13 - Tanguy Mandias - RUN - Elsa Bordier (BD)"},
    {'date': '2021-08-03', 'img_url': 'images/readings/il-faut-flinguer-ramirez-tome-2.jpg', 'description': "Il faut flinguer Ramirez - Nicolas Petrimaux (BD)"},
    {'date': '2021-06-29', 'img_url': 'images/readings/manifeste-pour-un-urbanisme-circulaire.jpg', 'description': "Manifeste pour un urbanisme circulaire : pour des alternatives concrètes à l'étalement de la ville (essai)"},
    {'date': '2021-04-27', 'img_url': 'images/readings/la-communaute.jpg', 'description': "La Communauté - Hervé Tanquerelle & Yann Benoit (BD)"},
    {'date': '2021-02-18', 'img_url': 'images/readings/lhyperreve.jpg', 'description': "L'Hyperrêve - Marc-Antoine Mathieu (BD)"},
    {'date': '2021-01-26', 'img_url': 'images/readings/Sombre6.jpg', 'description': "Sombre n°6 - Johan Scipion (JdR)"},
    {'date': '2020-12-27', 'img_url': 'images/readings/le-chateau-des-animaux.jpg', 'description': "Le château des animaux - Deleps & Dorison (BD)"},
    {'date': '2020-11-21', 'img_url': 'images/readings/broadway.jpg', 'description': "Broadway - Fabrice Caro (roman)"},
    {'date': '2020-10-19', 'img_url': 'images/readings/la-zad.jpg', 'description': "La ZAD - C'est plus grand que nous - Rochepeau & Azuélos (BD)"},
    {'date': '2020-10-06', 'img_url': 'images/readings/kiffe-ton-cycle.jpg', 'description': 'Kiffe ton cycle - Gaëlle Baldassari'},
    {'date': '2020-09-20', 'img_url': 'images/readings/contre-lalternumerisme.jpg', 'description': 'Contre l’alternumérisme - Julia Laïnae & Nicolas Alep'},
    {'date': '2020-07-15', 'img_url': 'images/readings/alors-voila.jpg', 'description': 'alors voilà - Les 1001 vies des Urgences - Baptiste Beaulieu (roman)'},
    {'date': '2020-06-09', 'img_url': 'images/readings/Dirty-MJ-COVER-1.jpg', 'description': 'Dirty MJ - John Wick (essai)'},
    {'date': '2020-05-24', 'img_url': 'images/readings/SandmanPreludesNocturnes.jpg', 'description': 'Sandman - Preludes & Nocturnes - Neil Gaiman (comics)'},
    {'date': '2020-05-13', 'img_url': 'images/readings/LesSciencesCaNousRegarde.jpg', 'description': 'Les sciences, ça nous regarde - Lionel LARQUÉ & Dominique PESTRE'},
    {'date': '2020-04-14', 'img_url': 'images/readings/la-consolante.jpg', 'description': 'La Consolante - Anna Gavalda (roman)'},
    {'date': '2020-04-08', 'img_url': 'images/readings/Aama.jpg', 'description': 'Aâma - Frederik Peeters (BD)'},
    {'date': '2020-03-14', 'img_url': 'images/readings/A-la-vie.jpg', 'description': "À la vie ! - L'Homme étoilé (BD)"},
    {'date': '2020-03-02', 'img_url': 'images/readings/LastMan12.jpg', 'description': 'Last Man tome 12 - Balak & Sanlaville & Vivès (BD)'},
    {'date': '2020-01-21', 'img_url': 'images/readings/chronosquad.jpg', 'description': 'Chronosquad - Giorgio Albertini & Grégory Panaccione (BD)'},
    {'date': '2019-12-28', 'img_url': 'images/readings/infinity8_tome5.jpg', 'description': 'Infinity 8 - tome 5 - Lewis Trondheim & Davy Mourier & Lorenzo De Felici (BD)'},
    {'date': '2019-12-22', 'img_url': 'images/readings/mamada.jpg', 'description': 'Mamada - David Ratte (BD)'},
    {'date': '2019-12-14', 'img_url': 'images/readings/garduno.jpg', 'description': 'Garduno - Philippe Squarzoni (BD)'},
    {'date': '2019-11-30', 'img_url': 'images/readings/ian.jpg', 'description': 'Ian - Fabien Vehlmann & Ralph Meyer (BD)'},
    {'date': '2019-11-20', 'img_url': 'images/readings/hitman.jpg', 'description': 'Hitman - Closing Time - Garth Ennis & John McCrea (Comics)'},
    {'date': '2019-10-25', 'img_url': 'images/readings/demon.gif', 'description': 'Demon - Jason Shiga (BD)'},
    {'date': '2019-10-13', 'img_url': 'images/readings/Fiasco_cover.gif', 'description': 'Fiasco - Jason Morningstar (JdR)'},
    {'date': '2019-10-05', 'img_url': 'images/readings/density.jpg', 'description': 'Density - Lewis TRONDHEIM & Stan VINCE (BD)'},
    {'date': '2019-09-02', 'img_url': 'images/readings/happycratie.jpg', 'description': 'Happycratie - Edgar Cabanas & Eva Illouz'},
    {'date': '2019-09-02', 'img_url': 'images/readings/energie-changeons-de-cap.jpg', 'description': 'Energie Changeons de cap ! - Didier Lenoir'},
    {'date': '2019-09-02', 'img_url': 'images/readings/reality-is-broken.jpg', 'description': 'Reality is broken - Jane Mc Gonigal'},
    {'date': '2019-08-05', 'img_url': 'images/readings/Hillbilly_t3.jpg', 'description': 'Hillbilly tome 3 - Eric Powell (BD)'},
    {'date': '2019-07-26', 'img_url': 'images/readings/BDArcaneMajeureT1couv.jpg', 'description': 'Arcane Majeure - Jean-Pierre Pécau & Damien Jacob (BD)'},
    {'date': '2019-06-15', 'img_url': 'images/readings/vanille_ou_chocolat.jpg', 'description': 'Vanille ou chocolat ? - Jason Shiga (BD)'},
    {'date': '2019-06-05', 'img_url': 'images/readings/gits.jpeg', 'description': 'The Ghost in the Shell - Shirow Matsamune (manga)'},
    {'date': '2019-05-19', 'img_url': 'images/readings/Jerome-K-Jerome-Bloche-integrale-t2.jpg', 'description': "Jérôme K. Jérôme Bloche - L'intégrale Tome 2 - Dodier (BD)"},
    {'date': '2019-05-03', 'img_url': 'images/readings/irl-cover.jpg', 'description': 'In real life - Cory Doctorow & Jen Wang (BD)'},
    {'date': '2019-04-28', 'img_url': 'images/readings/PourLaScience-HS-LOrdredCacheDesNombres.jpg', 'description': "Pour la Science - Hors Série n°103 - L'ordre caché des nombres"},
    {'date': '2019-03-29', 'img_url': 'images/readings/dedale-1-doki.jpg', 'description': 'Dédale - Takamichi (manga)'},
    {'date': '2019-03-10', 'img_url': 'images/readings/spacetrawler.jpg', 'description': 'Spacetrawler - Christopher Baldwin (webcomic)'},
    {'date': '2019-02-07', 'img_url': 'images/readings/VilleVermine_t1.jpg', 'description': 'VilleVermine tome 1/2 - Julien Lambert (BD)'},
    {'date': '2019-02-01', 'img_url': 'images/readings/Reinventing_Comics_Scott_McCloud_book_cover_art.jpg', 'description': 'Reinventing Comics - Scott McCloud (BD)'},
    {'date': '2019-01-20', 'img_url': 'images/readings/goupil_ou_face_couv.jpg', 'description': 'Goupil ou Face - Lou Lubie (BD)'},
    {'date': '2019-01-05', 'img_url': 'images/readings/CanardPC-15ans.jpg', 'description': 'Canard PC - Hors Série 15 ans'},
    {'date': '2018-10-16', 'img_url': 'images/readings/revue-dessinee-couv-no21-2018-automne.png', 'description': 'Nantes - Balades urbaines de Sarah Guilbaud (livre sur le Street Art)'},
    {'date': '2018-10-22', 'img_url': 'images/readings/nantes-balades-urbaines.jpg', 'description': 'Nantes  (Revue BD)'},
    {'date': '2018-07-17', 'img_url': 'images/readings/cité14.jpg', 'description': 'Citée 14 - Pierre Gabus & Romuald Reutimann (BD)'},
    {'date': '2018-07-05', 'img_url': 'images/readings/gloutons-et-dragons.jpg', 'description': 'Gloutons & Dragons - Ryoko Kui (manga)'},
    {'date': '2018-06-15', 'img_url': 'images/readings/tony-chu-tome-7.jpg', 'description': 'Tony Chu - Tome 7 - John Layman & Rob Guillory (BD)'},
    {'date': '2018-06-13', 'img_url': 'images/readings/au-pays-des-ombres.jpg', 'description': 'Au Pays des Ombres - Mathis & Thierry Martin (BD)'},
    {'date': '2018-06-02', 'img_url': 'images/readings/les_larmes_de_nuwa.jpg', 'description': 'Les Larmes de Nüwa - Benjamin Jurdic & Manuro (BD dont vous êtes le héro)'},
    {'date': '2018-05-05', 'img_url': 'images/readings/saga-tome-8.jpg', 'description': 'Saga - tome 8 - Fiona Staples & Brian K. Vaughan (BD)'},
    {'date': '2018-04-21', 'img_url': 'images/readings/enquetes-generales.jpg', 'description': 'Enquêtes Générales - Immersion au cœur de la brigade de répression du banditisme - Raynal Pellicer & Titwane (BD)'},
    {'date': '2018-04-08', 'img_url': 'images/readings/six-gun-gorilla.jpg', 'description': 'Six-Gun Gorilla - Simon Spurrier & Jeff Stokely (BD)'},
    {'date': '2018-03-02', 'img_url': 'images/readings/dans-la-combi-de-thomas-pesquet.jpg', 'description': 'Dans la combi de Thomas Pesquet - Marion Montaigne (BD)'},
    {'date': '2018-02-16', 'img_url': 'images/readings/Pantheon.jpg', 'description': 'Panthéon! - Hamish Steele (BD)'},
    {'date': '2018-02-02', 'img_url': 'images/readings/desobeisseurs-du-service-public.jpg', 'description': 'Les désobéisseurs du service public (BD)'},
    {'date': '2017-11-14', 'img_url': 'images/readings/l-art-internet.jpg', 'description': "L'Art Internet - Rachel Greene"},
    {'date': '2017-11-16', 'img_url': 'images/readings/The-Thrilling-Adventures-of-Lovelace-and-Babbage.jpg', 'description': 'The Thrilling Adventures of Lovelace and Babbage: The (Mostly) True Story of the First Computer'},
)  # ends READINGS

AVATARS = [
    'images/avatar.jpeg',
    'images/avatar.jfif',
]

# Blogroll
LINKS = (("Justin Mason's Weblog", 'https://jmason.ie/'),
         ('Neal Krawetz Hacker Factor Blog', 'http://www.hackerfactor.com/blog/'),
         ('Shaarli de sebsauvage', 'http://sebsauvage.net/links'),
         ('Hugin & Munin', 'http://hu-mu.blogspot.fr'),
         ('Radio Rôliste', 'https://www.radio-roliste.net'),
         ("C'est pas du jeu de rôle", 'https://www.cestpasdujdr.fr'),
         ('Trop Long ; Pas Lu !', 'http://troplongpaslu.fr'),
         ('Le blog de Gulix', 'https://www.gulix.fr'),
         ('Le blog de JeePee', 'http://www.jeepeeonline.be'),
         ('Le Fix di6dent', 'http://lefix.di6dent.fr/'),
         ('ptgptb', 'https://ptgptb.fr/'),
         ('The Indie RPG Pipeline', 'https://therpgpipeline.blogspot.com'),
         ('Derrière le paravent de Greg Pogorzelski', 'http://awarestudios.blogspot.fr'),
         ('Oglaf', 'https://www.oglaf.com'),
         ('Blog BD de Boulet', 'http://bouletcorp.com'),
         ('Warpdoor', 'http://warpdoor.com'),
         ('AlphaBetaGamer', 'https://www.alphabetagamer.com'),
         ('Free Game Planet', 'https://www.freegameplanet.com'),
         ('OuJeViPo', 'http://oujevipo.fr'),
         ('Du papier et des jeux', 'https://pnpfrance.wordpress.com'),
         ('J.P. Villain (Access42) @Twitter', 'https://twitter.com/villainjp'),
         ('Blog de David Larlet', 'https://larlet.fr/david/'),
         ('No Limit Secu', 'https://www.nolimitsecu.fr'),
         ('LinuxFR', 'https://linuxfr.org/'),
         ('Framablog', 'https://framablog.org/'),
         ('Reflets.info', 'https://reflets.info'),
         ('Tristan Nitot', 'http://standblog.org/blog/'),
         ('Blog de Victor Stinner', 'http://vstinner.github.io'),
         ('Rhizome.org', 'https://anthology.rhizome.org'),
         ("Du Monde Dans l'Objectif", 'https://www.dumondedanslobjectif.com'),
         ("Galerie d'Elliot Jolivet aka Tenseï", 'https://illutensei.com'),
         ("Galerie d'Elodie Olivier", 'https://elodie-olivier.com'),
         ("Les bocaux-mondes de Laure Coignard", 'https://www.instagram.com/b.o.k.a_l/'),
         ("Renard'eau", 'https://renardeau.chezsoi.org/'),
         # ('Steam Hidden Gems', 'https://www.canardpc.com/cat%C3%A9gorie/jeu-video/cabinet-de-curiosites/'),
         # ('Le Cabinet de Curiosités de CanardPC', 'https://steam250.com/hidden_gems'),
         # ('Fenêtre sur cour', 'https://www.arteradio.com/emission/fenetre_sur_cour'),
         # ('John Carmack', 'https://twitter.com/id_aa_carmack/'),
         # ('Jane McGonigal', 'https://twitter.com/avantgame'),
         # ('Antoine Bauza', 'https://twitter.com/Toinito'),
)

SOCIAL = (('shaarli', 'https://chezsoi.org/shaarli'),
          ('github', 'https://github.com/Lucas-C'),
          ('wikipedia', 'https://fr.wikipedia.org/wiki/Utilisateur:Dr_max_kurt'),
          ('itchio', 'https://lucas-c.itch.io'),
          ('stackoverflow', 'https://stackoverflow.com/users/636849/lucas-cimon'),
          ('discord', 'https://discord.com/invite/BJeuEtX'),
          ('linkedin', 'https://www.linkedin.com/in/lucascimon'),
          ('reddit', 'https://www.reddit.com/user/lucas-c/posts/'))
          # ('root-me', 'https://www.root-me.org/Lucas-C'),
          # ('reddit', 'https://www.reddit.com/user/drmaxkurt/posts/'),
          # ('deviantart', 'https://www.deviantart.com/drmaxkurt/favourites'),
          # ('travis-ci', 'https://travis-ci.com/Lucas-C'),

SUPPORTS = (('La Topette', 'https://latopette.fr/', 'images/LaTopette.png', 'Abonnez-vous à La Topette'),
            ('La Revue Dessinée', 'https://www.larevuedessinee.fr/', 'images/LaRevueDessinee.jpg', 'Abonnez-vous à la Revue Dessinée'),
            ('Backseat', 'https://www.youtube.com/@backseat_fr', 'images/backseat.jpg', 'Soutenez Backseat'),
            ('SPARK', 'https://www.youtube.com/@Spark-Stories-FR', 'images/spark.webp', 'Soutenez SPARK'),
            ('Mediapart', 'https://www.mediapart.fr/', 'images/mediapart.svg', 'Soutenez Mediapart'),
            ('Blast', 'https://www.blast-info.fr/', 'images/blast.jpg', 'Soutenez Blast'),
            ('Le Media', 'https://www.lemediatv.fr/', 'images/LeMedia.jpg', 'Soutenez Le Media'),
            ('Fonds Pour Une Press Libre', 'https://fondspresselibre.org/', 'images/logo-FondsPourUnePressLibre.png', 'Soutenez Mediapart et le Fonds Pour Une Press Libre'),
            ('Fakir', 'https://www.fakirpresse.info/', 'images/fakir.jpg', 'Abonnez-vous à Fakir'),
            ('LaQuadratureDuNet', 'https://soutien.laquadrature.net', 'images/LaQuadratureDuNet.png', 'Faites un don à la Quadrature'),
            ('Framasoft', 'https://soutenir.framasoft.org/liste-temoignages', 'images/framasoft.jpg', 'Soutenez Framasoft'),
            ('Enercoop', 'https://www.enercoop.fr/', 'images/Logo_Enercoop.png', 'Soutenez Enercoop'),
            ('andro switch', 'https://www.contraceptionmasculine.fr/andro-switch/', 'images/logo-andro-switch.png', 'La contraception masculine, renseignez-vous'),
            ('attac', 'https://france.attac.org/', 'images/attac.png', 'Soutenez attac'),
            ('Microformats', 'http://microformats.org/', 'images/microformats.png', 'Ce site adhère au standard microformats'),
            ('Webmention', 'https://indieweb.org/Webmention', 'images/webmention-button.svg', 'Ce site adhère au standard Webmention'),
            ('Low-tech', 'https://www.lowtechmagazine.com/2018/09/how-to-build-a-lowtech-website.html', 'images/low-tech.svg', 'Ce site adhère à la philosophie low-tech'))

MG_JOKES = (
    ("Pourquoi les canards sont toujours à l'heure ?", "Parce qu’ils sont dans l’étang."),
    ("Que fait une fraise sur un cheval ?", "Tagada Tagada."),
    ("Quel est le crustacé le plus léger de la mer ?", "La palourde"),
    ("Qu'est-ce qui fait toin toin ?", "Un tanard."),
    ("Pourquoi est-ce que Napoléon n'a pas voulu acheter de maison ?", "Parce qu’il avait déjà un Bonaparte"),
    ("Comment appelle-t-on un préservatif pour statue britannique ?", "Une capote en glaise."),
    ("Pourquoi n'y a-t-il plus de mammouths sur terre ?", "Parce qu’il n’y a plus de pappouths."),
    ("Pourquoi est-ce qu'on met tous les crocos en prison ?", "Parce que les crocos dealent."),
    ("Quel fruit est assez fort pour couper des arbres?", "Le ci-tron"),
    ("Que dit une noisette quand elle tombe à l'eau ?", "Je me noix"),
    ("Quel est le jambon que tout le monde déteste ?", "Le sale ami"),
    ("Que fait un cendrier devant un ascenseur ?", "Il veut des cendres"),
    ("Que dit une imprimante dans l'eau ?", "J’ai papier"),
    ("Pourquoi les vaches ferment-elles les yeux pendant la traite de lait ?", "Pour faire du lait concentré"),
    ("Comment savoir quand un sapin est en colère ?", "Il a les boules"),
    ("Que prend un éléphant dans un bar ?", "Beaucoup de place"),
    ("Pourquoi dit-on que les Bretons sont tous frères et sœurs ?", "Parce qu’ils ont Quimper"),
    ("Pourquoi est-ce que les livres ont-ils toujours chaud ?", "Parce qu’ils ont une couverture"),
)

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
# LOCALE = 'fr_FR.utf8'  # impacts date format; must be installed with sudo dpkg-reconfigure locales

SITEMAP_URL = './sitemap.xml'
PINGBACK_URL = 'https://webmention.io/chezsoi.org_lucas_blog_/xmlrpc'
WEBMENTION_URL = 'https://webmention.io/chezsoi.org_lucas_blog_/webmention'

# "Open Graph tags do not acknowledge <base>, and should always have full absolute URLs" - https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base
META_IMAGE = 'https://chezsoi.org/lucas/blog/images/Tom_Brown_Mathematics_CC-by-2-0_800x534.jpg'

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
PLUGINS = ('ctags_generator', 'deadlinks', 'image_preview_thumbnailer', 'representative_image') #, 'w3c_validate')

# Configuring image lazyloading for the image_preview_thumbnailer plugin:
IMAGE_PREVIEW_THUMBNAILER_INSERTED_HTML = '<a href="{link}" target="_blank"s><img loading="lazy" src="{thumb}" class="preview-thumbnail"></a>'

DEADLINK_VALIDATION = False  # à activer de temps en temps via "invoke build" inclus quelques faux positifs
DEADLINK_OPTS = {}           # cf. https://github.com/silentlamb/pelican-deadlinks#settings

# logging.getLogger('pelican.plugins.image_process.image_process').setLevel(logging.DEBUG)
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
MG_FILTER_TAGS = ('jeux', 'maths', 'prog')
MG_LANG_FILTER_TAGS = ['fr', 'en']  # 'lang:'-prefixed tags

CATEGORY_SAVE_AS = ''
ARCHIVE_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
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
