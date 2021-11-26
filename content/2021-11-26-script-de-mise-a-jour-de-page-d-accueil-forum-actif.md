Title: Script de mise à jour de page d'accueil ForumActif
Date: 2021-11-26 10:30
Tags: lang:fr, bash, curl, html, php, phpbb, forum-actif, framasoft, gitlab, gitlab-ci, gitlab-pages, auberge-des-reveurs, prog
---
Un court article pour partager une méthode bien pratique pour mettre à jour la page d'acceuil d'un forum [ForumActif](https://fr.wikipedia.org/wiki/Forumactif) :

[![Logo de l'association L'Auberge des Rêveurs](images/2021/11/logo-auberge-des-reveurs.webp)](https://laubergedesreveurs.forumactif.com/)

## Contexte

Une association de jeux de rôle a mis en place un site [ForumActif](https://laubergedesreveurs.forumactif.com/forum).
Cet hébergeur inclus dans ses forums phpBB la possibilité de créer des pages HTML statiques,
et de les utiliser comme page d'accueil :

![Capture d'écran du module d'administration des pages HTML](images/2021/11/ForumActif-AdminPanel.jpg)

J'ai donc développé une page d'accueil assez simple mais un peu plus attractive / lisible
que celle "de base" des sites ForumActif.

Le code est herbergé sur FramaGit : <https://framagit.org/auberge-des-reveurs/website-homepage/> (❤️ Gitlab & [FramaSoft](https://framasoft.org/))

Et tout le contenu du site (images, CSS, JS...) est hebergé via des [Gitlab Pages](https://docs.gitlab.com/ee/user/project/pages/) :
<https://auberge-des-reveurs.frama.io/website-homepage/>

Néanmoins, l'activation / mise à jour de la page d'accueil statique sur ForumActif doit se faire manuellement,
via l'interface d'administration du forum.
Hors, je souhaitais que la page d'accueil du site soit mise à jour **automatiquement**,
à chaque _commit_ sur le _repository_ `git`,
via la [pipeline Gitlab CI](https://docs.gitlab.com/ee/ci/pipelines/) qui déployait déjà le site en Gitlab Pages.

## Solution

J'ai développé un court script Bash employant `curl` & `python` qui permet de :

1. s'authentifier sur le forum, et ainsi récupérer un _cookie_ `sid` et un _token_ `tid`
2. _uploader_ une nouvelle version de la page statique (`index.html`)

Le script est ici : [set_phpbb_html_homepage.sh](https://framagit.org/auberge-des-reveurs/website-homepage/-/blob/main/set_phpbb_html_homepage.sh)

Et la pipeline est décrite ici : [.gitlab-ci.yml](https://framagit.org/auberge-des-reveurs/website-homepage/-/blob/main/.gitlab-ci.yml)

J'espère que ça pourra être utile à d'autres administrateurs de sites ForumActif 😋
