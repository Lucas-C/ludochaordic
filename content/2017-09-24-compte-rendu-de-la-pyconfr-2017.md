Title: Compte-rendu de la PyConFr 2017
Date: 2017-09-25 19:00
Tags: lang:fr, python, open-source, hackathon, documentation, talk, conference, slides, toulouse, oui.sncf, compte-rendu, opinion, prog
Slug: compte-rendu-de-la-pyconfr-2017
---

<img src="images/2017/09/pyconfr-2017-logo.png" alt="Logo PyConFr 2017">

Cette année, [voyages-sncf.com](https://open.voyages-sncf.com) m'a permis d'aller à la conférence annuelle Python à Toulouse.

<img src="images/2017/09/logo_voyages-sncf.com.png" alt="Logo voyages-sncf.com">

En vrac, voici un petit résumé personnel de cette PyConFr.

J'y étais présent 3 jours sur 4 (sprint le premier et conférences les deux autres),
et j'y ai donné donné 2 présentations, dont le contenu est disponible sur la pages [slides](pages/slides.html).

<!-- toc -->

- [Jour 1 - vendredi 22 septembre](#jour-1---vendredi-22-septembre)
    * [python-docs-fr](#python-docs-fr)
    * [ideascube](#ideascube)
- [Jour 2 - samedi 23 septembre](#jour-2---samedi-23-septembre)
    * [10h30 : Plone, 15 ans d'expérience feront toujours la différence - Eric Bréhault - Makina Corpus](#10h30--plone-15-ans-dexperience-feront-toujours-la-difference---eric-brehault---makina-corpus)
    * [11h30 : Les Aventuriers du Packaging Perdu - Joachim Jablon & Stéphane Angel](#11h30--les-aventuriers-du-packaging-perdu---joachim-jablon--stephane-angel)
    * [14h : Enseigner est apprendre - Céline Martinet Sanchez](#14h--enseigner-est-apprendre---celine-martinet-sanchez)
    * [15h30 : L'interprêteur Python, quel sale type - serge-sans-paille](#15h30--linterpreteur-python-quel-sale-type---serge-sans-paille)
    * [16h30 : Scalable & distributed applications in Python - Julien Danjou - Red Hat](#16h30--scalable--distributed-applications-in-python---julien-danjou---red-hat)
    * [17h30 : As-tu déjà pensé à contribuer à CPython - Stéphane Wirtel](#17h30--as-tu-deja-pense-a-contribuer-a-cpython---stephane-wirtel)
    * [18h30 : C'est quoi être différent ? - Haïkel Guémar](#18h30--cest-quoi-etre-different----haikel-guemar)
- [Jour 3 - dimanche 24 septembre](#jour-3---dimanche-24-septembre)
    * [11h : Frets On Fire (X) et son écosystème après 11 ans - François Magimel](#11h--frets-on-fire-x-et-son-ecosysteme-apres-11-ans---francois-magimel)
    * [12h : nuka - libérez le vilain devops qui est en vous - Gael Pasgrimaud](#12h--nuka---liberez-le-vilain-devops-qui-est-en-vous---gael-pasgrimaud)
    * [14h : Construire et gérer un opérateur Internet en Python - Florian Vichot - Wifirst](#14h--construire-et-gerer-un-operateur-internet-en-python---florian-vichot---wifirst)
    * [16h30 : Organisez vos conférences avec PonyConf - Elie Bouttier](#16h30--organisez-vos-conferences-avec-ponyconf---elie-bouttier)
    * [17h : Python and Poland Directories - Christopher Lozinski](#17h--python-and-poland-directories---christopher-lozinski)
- [Bilan](#bilan)

<!-- tocstop -->


# Jour 1 - vendredi 22 septembre

La conférence était hébergée par l'ENSEEIHT à Toulouse.
Durant les deux jours de sprints nous étions tous rassemblés dans une grande salle classe.

Il était proposé de contribuer à des projets Python parmi [une dizaine de présents](https://www.pycon.fr/2017/programme.html#sprints).
A vue de nez, il y avait dans l'après-midi une soixante de personne concentrées sur leurs ordinateurs portables,
regroupées par petits groupes autour de quelques tables.
Un développeur connaissant le projet était sur place pour le présenter,
indiquer quelques bugs faciles et accompagner les contributeurs.

J'ai personnellement effectué quelques contributions mineures à deux projets:


## python-docs-fr

Cette initiative de [Julien Palard](https://mdk.fr) vise à traduire la documentation de la bibliothèque standard Python en français.
Il m'a dit s'être attelé à ce chantier pour passer le temps lors de longs trajets en RER :)
C'est un sacré chantier, chapeau bas à lui de l'avoir entamé !

<span style="font-size: 3rem">🙏</span>

Ça a été l'occasion pour moi de découvrir [Poedit](https://poedit.net), un éditeur de fichiers `.po` de traductions (standard [gettext](https://fr.wikipedia.org/wiki/GNU_gettext)).

Suite à un rapide échange avec Julien, j'ai soumis une _pull-request_ pour remplacer tous les usages du verbe "retourner" par "renvoyer" ou "revenir" afin d'éviter tout ambiguïté: <https://github.com/python/python-docs-fr/pull/29>

A noter qu'il est possible, et encore plus simple, de contribuer à cette traduction via <https://www.transifex.com/python-doc/public/>

J'ai ensuite commencé à jeter un oeil à un bug concernant le changement de langage dans l'interface web de la doc Python (<http://bugs.python.org/issue31146>), mais je ne suis pas allé au bout au cours de ce sprint.


## ideascube

Avec beaucoup de patience, [Mathieu Bridon](https://mathieu.daitauha.fr/blog/) et [Matthieu Gauthier](https://mgautier.fr) de [Kymeria](https://kymeria.fr) m'ont guidé à travers [quelques corrections de bugs](https://framagit.org/ideascube/ideascube/merge_requests?scope=all&utf8=%E2%9C%93&state=all&author_username=Lucas-C) sur le projet **ideascube**.

Ce projet de _Bibliothèques Sans Frontières_ est une application Django motorisant les [Ideas Box](http://www.ideas-box.org).

![IdeasBox: portable media-center for refugee and vulnerable populations](images/2017/09/IdeasBox.jpg)

Mathieu Bridon en parle plus en détails sur son blog: <https://mathieu.daitauha.fr/blog/2017/09/25/de-retour-de-pycon-fr-et-du-sprint-ideascube/>

Pour en savoir un peu plus sur ces projets de BSF, je vous invite à écoute l'émission récente de la radio Nova sur le sujet:
<http://www.nova.fr/podcast/neo-geo/neo-geo-gren-seme-de-la-reunion-et-jeremy-lachal-de-bibliotheque-sans-frontieres>

J'ai également découvert à cette occasion [Kiwix](http://wiki.kiwix.org), un beau projet à but humanitaire dont bénéficient plus d'1 million d'utilisateurs chaque année:

> **Tout le monde n'a pas accès à Internet**

> Et si c'est le cas, il y a de grandes chances que celui-ci soit lent, erratique ou simplement censuré. Kiwix est une solution hors-ligne qui permet à tout un chacun de consulter des contenus éducatifs tels que Wikipédia, le Wiktionnaire, la bibliothèque Gutenberg et bien d'autres encore - ce sur n'importe quel ordinateur ou smartphone, et sans qu'il y ait besoin d'avoir une connexion permanente à Internet.

> **Kiwix est présent dans des écoles, des universités, et même des prisons**

> Et bien sûr à la maison. Plus rapide qu'une connexion internet, il permet d'économiser de la bande passante et du temps de chargement sur les connexions lentes. Facile à installer et peu gourmand en ressources, Kiwix fonctionne sur les vieux ordinateurs et ceux à faible puissance. Il est disponible sur la plupart des plateformes, d'Android et iOS à Microsoft Windows, macOS et bien sûr GNU/Linux.



# Jour 2 - samedi 23 septembre

Début des conférences !

Je donne mon premier _talk_ à 10h.

A noter que cette année, de nombreuses conférences étaient signées en simultané par des traducteurs en langue des signes.


## 10h30 : Plone, 15 ans d'expérience feront toujours la différence - Eric Bréhault - Makina Corpus

Présentation de [plone](http://plone.fr), "seul" CMS Python, et de ses très nombreuses fonctionnalités _built-in_ (ex: breadcrumbs depuis 2001).

Très sécuritaire, il est notamment utilisé par le FBI.

En cours de refonte pour Python 3 (Zope 4), avec un nouveau projet : **Guillotina**, version purement _headless_ se basant sur `aiohttp`, Elasticsearch et une base donnée similaire à ZODB par-dessus de PostgreSQL ou Cockroach.

Ce CMS est déployable sur Heroku et apparemment extrêmement simple à prendre en main.

Vidéo: <https://www.youtube.com/watch?v=FFIK3neBhMI&list=PLetYPqNT2qjAinIBr976XSjJObaa-zUy5&index=1>


## 11h30 : Les Aventuriers du Packaging Perdu - Joachim Jablon & Stéphane Angel

Présentation très complète des bonnes pratiques de packaging en Python.

Ils m'ont convaincu à transformer le `setup.py` de mes projets en `setup.cfg`,
ce que j'ai fait en parallèle de leur _talk_ ^^

La liste d'outils à la fin de leurs _slides_ vaut vraiment le coup d'être récupérée.


## 14h : Enseigner est apprendre - Céline Martinet Sanchez

Un retour d'expérience très intéressant de cette formatrice et rédactrice de cours sur [OpenClassrooms](https://openclassrooms.com/membres/celinemartinet) portant sur tout ce que peut apporter l'enseignement.

Elle prêchait un convaincu dans mon cas, mais elle a aussi donné quelques très bons conseils sur comment créer un bon cours :

- fournir des exemples concrets et des définitions abstraites
- le bonheur est dans le chemin et dans la finalité
- contenu différenciant
- détaillez toutes les étapes, même les + petites
- Soyez drôle ! Donnez envie !

Enfin, elle a apporté des éléments de réponse à la passionnante question "Qu'est-ce qu'être développeur senior ?"


## 15h30 : L'interprêteur Python, quel sale type - serge-sans-paille

En très bref, une belle démonstration des limites de la validation statique de code Python typé via des annotations, via `mypy` par exemple.

Personnellement il m'a convaincu.

Au passage, selon les critères que l'on choisit pour définir la notion d'objet itérable (existence de la méthode `__iter__`, `isinstance(obj, Iterable)`, etc.),
des objects comme celui-ci peuvent donner des résultats surprenants:
```
class Infinity(objet):
    def __getitem__(self, _)
        return 0
```

La présentation était basée sur un _notebook_ Jupyter permettant d'évaluer du code Python en _live_, avec un _plugin_ de présentation `reveal.js`.

Ce _talk_ s'est conclu par une très intéressante discussion avec Serge et Victor Stinner, ou j'ai découvert [Argument Clinic](https://www.python.org/dev/peps/pep-0436/), un outil CPython visant à:

* fournir des information sur la signature des fonctions _builtin_
* permettre à des implémentations alternatives de Python de créer des tests de compatibilité automatisés
* améliorer les performances du code gérant la lecture de paramètres de fonctions


## 16h30 : Scalable & distributed applications in Python - Julien Danjou - Red Hat

Une présentation très complète détaillant beaucoup de conseils pour concevoir des applications distribuées en Python,
par le développeur de [Gnocchi](https://github.com/gnocchixyz/gnocchi).

<img src="images/2017/09/gnocchi-logo.png" alt="Logo Gnocchi"
     style="max-width: 20rem">

Les _slides_ de ce _talk_ étaient très complets. Voici quelques notes en pagaille qui en sont issues.

_Threads: how to_

- **Concurrent.futures**
- **Futurist**: provide backlog control & statistics

**GIL** => surtout utile pour:

* async I/O
* computation without Python datastructures
* running C extensions in parallel

_Multi-processes: how to_

- pas intéressant pour exécutions courtes
- **Concurrent.futures**
- **Cotyledon**: baby-sitting de daemons

Système distribué ⚠ => plein de nouveaux failure modes
- node failure
- network failure
- latency

**Use queue based systems**: Celery, `rq`

Projet Python implémentant plein de locks ou de coordinateurs: `Tooz`

⚠ Attention! à ce que le gestionnaire de locks ne devienne pas un SPOF

Caching:

- `cachetools` : gère TTL, fourni stats
- `functools.lru_cache`
- `dogpile.cache` : agnostique de l'outil derrière -> Redis, memcache, (Varnish?)

Questions:

- quid. antirez/disque ? (vs `rq`)
- dead letter queue ?


## 17h30 : As-tu déjà pensé à contribuer à CPython - Stéphane Wirtel

Stéphane, organisateur du FOSDEM Python, a démystifié toutes les appréhensions qu'on pouvait avoir sur le sujet.
Il nous a expliqué pas à pas comment se déroulent les contributions sur CPYthon,
les personnes qui peuvent nous aider et toutes les ressources à disposition :

- <https://www.python.org/dev/core-mentorship/>
- le [devguide](https://docs.python.org/devguide/)
- les [mailing-lists](https://www.python.org/community/lists/)

Il nous a mentionné une phrase de Brett Cannon:
> Je suis venu pour le langage, et je suis resté pour la communauté.

Quelques anecdotes découvertes au passage:

- l'intégration continue de CPYthon se fait via des instances [buildbot](http://buildbot.net) hébergées par des bénévoles,
dont l'exécution est déclenchée à distance, ce qui peut mener des [échanges assez drôles](https://haypo.github.io/python-buildbots-2017q2.html#the-vacuum-cleaner) sur la mailing-list.

- suite à l'incident de sécurité sur <https://pypi.org> (paquets typosquattés) qui a refait surface ce mois-ci,
de nombreux commentaires violemment critiques ont été postés sur des sites comme Hacker News, accusant directement
les mainteneurs de pypi et les devs CPython.

Quand on sait que, quel que soit le sondage, Python est systématiquement dans le top 5 des langages les plus utilisés au monde,
c'est assez fou de réaliser que les _core devs_ Python sont quasi-tous de volontaires.

**Une seule personne au monde est rémunérée par la PSF** (pour administrer les sites web Python officiels).
Un _core dev_ est également autorisé par son employeur à consacrer la majeure partie de son temps à Python.
En dehors de ces deux personnes, **Python est entièrement développé et maintenu par des bénévoles sur leur temps libre !!**

Vidéo: <https://www.youtube.com/watch?v=iEDFRCNDZNE&list=PLetYPqNT2qjAinIBr976XSjJObaa-zUy5&index=6>


## 18h30 : C'est quoi être différent ? - Haïkel Guémar

J'ai raté le début de ce _talk_, dont le but était de faire prendre conscience des discriminations existantes,
ainsi que des moyens à notre disposition pour les contrecarrer. J'ai aimé en particulier le passage sur l'illusion de la méritocratie.

Voici quelques unes de ses recommandations:

Que faire concrètement ?

- admettre l'existence du biais
- mesurer les inégalités (salaire, postes)

Théorie de la fenêtre brisée:

- certains propos n'ont pas leur place dans le lieu de travail
- rendre l'environnement accueillant pour tous
- ne pas se taire

Ne pas reproduire les schémas:

- éducation
- remettre en question les choix établis
- charité bien ordonnée commence par soi même

Briser les barrières mentales:

- donner un cadre sécuritaire pour les minorités de s'exprimer et apprendre
- donner des exemples
- ne pas confondre considération et condescendances



# Jour 3 - dimanche 24 septembre

Le matin avait lieu l'AG annuelle de l'AFPY, dont voici le CR : <https://www.afpy.org/news/pv-de-lassemblee-generale-ordinaire-2017>

## 11h : Frets On Fire (X) et son écosystème après 11 ans - François Magimel

Projet gagnant de l'_Assembly demo party_ 2006, issue à l'origine d'une boîte suédoise,
l'aventure continue pour clone de GuitarHero libre, _cloné_ de nombreuses fois.

<img src="images/2017/09/frets-on-fire.png" alt="Illustration du jeu"
     style="max-height: 15rem">

La dernière mouture activement maintenue s'appelle [FoFiX](http://fretsonfire.wikidot.com/fofix-install).

Les technos employées sous le capot: pygame, OpenGL, NumPy, Cython. Et pour les musiques: midi, OGG, Vorbis.

Et, chose que je trouve absolument géniale, un chercheur canadien a adapté _Frets On Fire_ pour les personnes en situation de handicap visuel:
<http://www.eelke.com/projects/blindhero-guitarhero-visual-impairment.html>


## 12h : nuka - libérez le vilain devops qui est en vous - Gael Pasgrimaud

Présentation d'un outil de déploiement fonctionnellement proche d'Ansible: [nuka](https://github.com/bearstech/nuka)

<img src="images/2017/09/bearstech-logo.jpg" alt="Logo bearstech"
     style="max-height: 10rem">

A bearstech ils utilisaient initialement un outil maison, [pussh](https://github.com/bearstech/pussh), très robuste,
mais leurs clients souhaitaient quelque chose de plus moderne / sexy.

Ansible ne convenait pas:

- ils ne voulaient pas d'agent sur les serveurs
- il comporte des limitations en terme de performance pas solubles facilement,
par exemple l'utilisation du module `mulitprocessing` générant un nouveau _process_ à chaque commande exécutée

Cette solution:

- est compatible avec des déploiement dans le "cloud" via l'utilisation de la lib `libcloud`
- nécessite Python3 localement, mais le serveur à distance peut se contenter d'un Python 2.6+
- inclus un système d’introspection de la _stack_ d'appels Python pour éviter les redites de configuration 😱
- supporte `gpg`

_Benchmark_ indicatif: 296 exécution de la commande `ls` en 15s (contre ~40s avant)

Astuce: pour gagner en vitesse, changer la priorité système du processus `ssh-agent`


## 14h : Construire et gérer un opérateur Internet en Python - Florian Vichot - Wifirst

Une des présentations les plus détaillées et pointue techniquement que j'ai vu de la conférence.
Je n'ai pas tout saisi des aspects "infrastructure physique du réseau", mais dans l'ensemble
c'était un retour d'expérience très complet et très clair.

Je n'ai par contre pris que très peu de notes.

Ils utilisent extensivement `pyroute2`, une _lib_ permettant de se connecter à une socket Netlink et de configurer tout ce que permet `iproute2`.

Ils ont atteint les limites d'Ansible:

* → lenteur 😞
* → ont développé un module de _callback_ listant des résultats d'exécution plus complets
* → quelques problèmes avec les mauvais réseaux (type satellite) pour SSH
* → `/bin/true` 4min30 vs `/bin/false` 22min


## 16h30 : Organisez vos conférences avec PonyConf - Élie Bouttier

Une présentation de l'appli libre Django qu'ils ont développé et utilisé pour organiser PyCon:
<https://github.com/toulibre/ponyconf>

La liste de fonctionnalités est assez impressionnante ! (elle est détaillée dans ses _slides_)
Ils ont fait un sacré beau boulot, et prévoient encore pas mal d'améliorations.

Clairement l'outil que j'utiliserais pour organiser une conf.


## 17h : Python and Poland Directories - Christopher Lozinski
Présentation de <https://pythonlinks.info>.

Plutôt que de répéter son contenu, je vous invite à regarder la vidéo d'introduction au projet sur la page d’accueil du site.

Vidéo: <https://www.youtube.com/watch?v=eZynCkvjjhE&list=PLetYPqNT2qjAinIBr976XSjJObaa-zUy5&index=4>


# Bilan

Il y a au moins deux conférences qui m'avaient l'air très intéressants mais auxquelles, absence d'ubiquité oblige, je n'ai pas pu assister:
celle sur [le solver Z3](https://github.com/Z3Prover/z3) de Michael Scherer, et celle sur l'histoire du standard Unicode de Guillaume Ayoub.

Les présentations ont été filmées: <https://www.youtube.com/playlist?list=PLetYPqNT2qjAinIBr976XSjJObaa-zUy5>

A noter qu'en parallèle de la conférence, un ["Crypto challenge"](https://www.bde.enseeiht.fr/~deniauv/affiche.pdf) était organisé.
Je ne me suis essayé qu'aux premières étapes (un bot <https://riot.im> était impliqué),
mais à ce qu'on m'a dit il était tordu à souhait !

Enfin, ça a surtout été l'occasion de faire de chouettes rencontres: Stéphane, Kevin, Damien, Florian, Hugo, Ludo, Antoine, Victor...
Au plaisir de vous revoir à la prochaine convention ;)



<script>
['h1', 'h2'].forEach(function (selector) {
    document.querySelectorAll(selector).forEach(function (title) {
        if (!title.classList.length) {
            title.id = title.textContent
                            .toLowerCase()
                            .replace(/[()?:,'&]/g, '')
                            .replace(/[à]/g, 'a')
                            .replace(/[ç]/g, 'c')
                            .replace(/[éêè]/g, 'e')
                            .replace(/[ï]/g, 'i')
                            .replace(/ /g, '-');
        }
    });
});
</script>

<style>
article img { display: block; margin: 0 auto; }
</style>
