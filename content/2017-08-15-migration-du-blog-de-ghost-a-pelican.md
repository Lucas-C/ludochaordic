Title: Migration du blog de ghost à pelican
Date: 2017-08-15 21:30
Tags: lang:fr, blog, python, pelican, ghost, prog
Slug: migration-du-blog-de-ghost-a-pelican
---

[![](images/2017/08/ghost2pelican.png)](https://www.artlimited.net/image/fr/219453)

Ça y est ! Bascule effectuée !

Ce blog est désormais un blog **statique**, généré avec [Pelican](https://blog.getpelican.com/).

Et au passage: c'est son anniversaire ! 3 ans :)


## Pourquoi migrer vers un blog statique avec Pelican ?

- par souci de simplicité: `make publish` et il n'y a plus qu'à servir les fichiers HTML générés
- par sécurité, les blogs statiques permettent d'éviter toute une classe de failles: <https://github.com/TryGhost/Ghost/issues?utf8=%E2%9C%93&q=security>
- je préfère versionner mes articles sous `git` plutôt que d'avoir à gérer une base de données
- Pelican est en **Python** ! Et les templates sont en `Jinja2`: je suis bien plus familier et je préfère grandement ces outils
- pour pouvoir `grep`-er mes articles
- manipuler de simple fichiers pour écrire des articles permet bien plus de flexibilité, comme celle d'utiliser le correcteur orthographique de `vim` par exemple, ou de faire du [postprocessing](https://github.com/Lucas-C/ludochaordic/blob/master/Makefile#L75)

## Les étapes de la migration

- convertir l'export de contenu de Ghost, au format JSON, en fichiers markdowns: [gist](https://gist.github.com/Lucas-C/7bd26443669bfe369107c03be8b05bb2)
- établir des régles de redirection pour `nginx`: [gist](https://gist.github.com/Lucas-C/d3ff24ca636e09241eb5eea18e5a4c72)
- chosisir un thème et l'installer: je l'ai forké pour y apporter quelques modifications: <https://github.com/Lucas-C/pelican-mg>
    * commentaires isso (+ cron pour recevoir des emails lorsque des commentaires sont ajoutés: [gist](https://gist.github.com/Lucas-C/42373e6451a28e4c59026c129c1abb73))
    * gestion des tags, manquante
    * correction de bugs en passant les templates au validateur HTML W3C
    * ajout du blogroll et de liens/icônes dans la barre latérale
    * ajout d'un tag cloud
    * ajout d'images miniatures pour caque article dans l'index, avec redimensionnement automatique pour ne pas avoir une page trop lourde
    * plus d'hébergement de resources sur des CDNs
    * boutons de navigation permettant de filtrer les articles par tags

## Bilan

Je suis assez content du résultat, mais **dites-moi ce que VOUS en pensez !** :)

Le blog dispose désormais d'une fonction de recherche, déjà présente dans le thème initial.
Je me demande si c'est utile à conserver, surtout que la lib "Tipue-Search" derrière n'est clairement plus maintenue: <https://github.com/Tipue/Tipue-Search/issues/13>

Je ne vois qu'une fonctionnalité utile de Ghost qui va me manquer: l'auto-complétion des tags, pour ajouter à un article des tags déjà employés.

Et enfin, cette migration a été l'occasion de faire une 1ère contribution au projet Pelican: <https://github.com/getpelican/pelican/pull/2204>,
et d'ajouter la gestion des templates Jinja2 à mes pre-commit hooks git permettant de valider du HTML: <https://github.com/Lucas-C/pre-commit-hooks-html>
