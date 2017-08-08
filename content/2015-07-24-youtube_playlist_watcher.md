Title: youtube_playlist_watcher
Date: 2015-07-24 11:07
Tags: lang:fr, python, youtube, playlist, cron, email, json
Slug: fr-youtube_playlist_watcher
---
Depuis plusieurs années, je ruminais contre Youtube: chaque fois qu'une vidéo est supprimée d'une playlist (parce que l'utilisateur qui l'avait uploadé l'a supprimé par exemple), son nom n'est même pas conservé, seul un lien mort persiste dans la liste.

Et la seule solution est alors de googler le nom de la vidéo pour retrouver, si vous êtes chanceux, de quelle chanson il s'agissait.

C'est pourquoi j'ai écrit un petit script Python pour y remédier : [youtube\_playlist\_watcher](https://github.com/Lucas-C/youtube_playlist_watcher).

Une fois installé dans un _cron job_, il effectue une sauvegarde journalière de votre playlist au format JSON, et vous alerte par email lorsqu'une vidéo est supprimée ou devient inaccessible.

<img src="https://chezsoi.org/lucas/wwcb/photos/NinjaTurtlesPowerRangers.gif">