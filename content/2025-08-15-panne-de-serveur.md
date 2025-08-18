Title: Panne de serveur
Date: 2025-08-15 16:00
Lang: fr
Tags: lang:fr, backup, caddy, nginx, ansible, infomaniak, lxc, scaleway, ubuntu, SelfHosted, prog
---

Avant-hier matin, mercredi 13 août, suite à une mise à jour vers Ubuntu 22 de mon serveur, j'ai eu la mauvaise surprise de ne pas le voir redémarrer...

Subissant en plus un rhume carabiné, je me suis un peu décomposé en voyant mes systèmes de supervision m'alerter lorsque la vingtaine de services hebergés sur le serveur est tombée KO d'un coup 😱

![I'll just change this one line...](images/wwcb/Ill_just_change_this_one_line...-DevOpsReactions.gif)

Après d'infructueuses tentatives de dépannage, le dernier clou dans le cerceuil a été planté par le support de Scaleway :

![Capture d'écrant d'un message dur support de Scaleway](images/2025/08/ScalewaySupport.png)

Cette chère Dédibox, initialement louée chez Online.net, a rendu de bons & loyaux services pendant plus de 10 ans. 

Heureuseument, des backups quotidiens des conteneurs LXC en place via FTP on limité l'impact de la catastrophe 😅

Cependant toute la configuration `lxc` / `iptables` / `bind9` / etc. a été perdue 😔

Finalement, j'ai décidé de migrer mes services ailleurs, chez Infomaniak.
Avec une ambition cette fois : tout redéployer avec de l'_infrastructure as code_, avec Ansible notamment,
pour faciliter d'éventuelles futures migrations.
Et en profiter pour expérimenter de nouveaux outils, comme remplacer `nginx` par `caddy` pour certains services.

Durant encore quelques jours, certains liens pointant vers `chezsoi.org` risquent de ne pas fonctionner.
La remise en place de ce blog s'est avérée assez rapide, donc j'espère que tout sera réglé assez vite.

Si jamais cela vous empêche d'accéder à certains services, veuillez bien m'excuser pour la gêne occasionnée.
