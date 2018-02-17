Title: Bonjour, monde !
Date: 2014-07-16 13:07
Tags: lang:fr, ghost-tag, license, backup, project, start, theme, isso, comments, prog
Slug: bonjour-monde
---
Ça y est, c'est ouvert !

Bienvenu sur mon petit coin d'Internet :)

Tout est encore en travaux, mais je compte rédiger rapidement quelques premiers articles.

Au passage:

- ce blog tourne sous [Ghost 0.5.8](//ghost.org)
- le thème actuel est [Day & Night](//github.com/semeano/DayAndNight), réalisé par Pedro Semeano et sous License MIT
- <del>j'y ai ajouté un moteur de recherche en utilisant [ghostHunter](//github.com/i11ume/ghostHunter) de Jamal Neufeld, qui ne cherche pas dans les tags malheureusement</del>
- et [highlight.js](//highlightjs.org/static/test.html) fournit la coloration syntaxique
- le logo "Little Pixel" a été réalisé par [Elliot Jolivet](//www.behance.net/mythostasis), un ami
- la couverture du blog provient d'une [photo](//www.flickr.com/photos/t_e_brown/8677750589) de Tom Brown sous License CC-BY-2.0
- pour les backups, j'utilise un [script](//github.com/dan-v/ghost-backup) de Dan Vittegleo

Et un indice pour comprendre le nom du blog: [la définition de "chaordique" sur Wikipédia](//fr.wikipedia.org/wiki/Chaordique).

Enfin, un petit truc : vous pouvez basculer le contraste en mode "nuit" en appuyant sur le bouton noir en haut.

<hr/>

**EDIT** [21/09/2014] :

- Ghost v0.4 -> v0.5.1
- commentaires [ISSO](http://posativ.org/isso) ajoutés. J'ai utilisé [ce tuto](//tobrunet.ch/articles/comments-for-a-static-website-with-isso/) mais avec une configuration Apache légèrement différente:
```
WSGIPythonHome /var/www/lucas/python-virtualenv
... # VirtualHost specific configuration
WSGIScriptAlias /lucas/isso /var/www/lucas/isso/isso.wsgi
WSGIDaemonProcess isso-blog-lucas user=isso group=isso threads=5
WSGIProcessGroup isso-blog-lucas
WSGIApplicationGroup %{GLOBAL}
```
