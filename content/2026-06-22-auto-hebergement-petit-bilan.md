Title: Auto hébergement : petit bilan
Date: 2026-06-22
Tags: lang:fr, alerting, service-monitoring, AutoHebergement, sysadmin, linux, ansible, infomaniak, scaleway, OVH, cybersecurity, framasoft, shaarli, caddy, gatus, pelican, php, systemd, prog
---

J'évoque très rarement le sujet de l'**auto-hébergement** sur ce blog, alors que depuis 12 ans je consacre un temps conséquent à bidouiller plein de trucs dans ce domaine ! 😁

Si vous ne connaissez pas ce terme : en bref, l'**auto-hébergement** c'est gérer soi-même différents services numériques (emails, stockage de donnée, applications web, etc.) sur son son propre [serveur informatique](https://fr.wikipedia.org/wiki/Serveur_informatique).
Cela peut constituer un _hobby_, mais aussi une démarche pour promouvoir des alternatives aux services gérés par les [GAFAM](https://fr.wikipedia.org/wiki/GAFAM), bien plus préoccupés par leurs profits que par des considérations éthiques.

Suite notamment à ma [panne de serveur Scaleway](panne-de-serveur.html) l'été dernier, j'ai bricolé des tas de choses ces derniers mois.

Cet article est donc l'occasion pour moi de faire un petit bilan sur le sujet, de partager mes réflexions, mon organisation et quelques outils que j'ai pu employer.

## Sommaire
* [Préambule : auto-hébergement, limites, cybersécurité](auto-hebergement-petit-bilan.html#preambule--auto-hebergement-limites-cybersecurite)
* [Petit historique](auto-hebergement-petit-bilan.html#petit-historique)
* [Adoption d'Ansible](auto-hebergement-petit-bilan.html#adoption-dansible)
* [Serveur HTTP](auto-hebergement-petit-bilan.html#serveur-http)
* [Backups](auto-hebergement-petit-bilan.html#backups)
* [Supervision](auto-hebergement-petit-bilan.html#supervision)
* [Services hébergés](auto-hebergement-petit-bilan.html#services-heberges)
* [WordPress](auto-hebergement-petit-bilan.html#wordpress)
* [Expérimentations](auto-hebergement-petit-bilan.html#experimentations)
* [Conclusion](auto-hebergement-petit-bilan.html#conclusion)

## Préambule : auto-hébergement, limites, cybersécurité
Tout d'abord, **je ne me suis jamais lancé dans un auto-hébergement « à domicile »**, avec une machine dédiée installée chez moi,
ni dans les passionnants sujets associés comme l'emploi d'un [FAI alternatif, tel **FAI maison** autour de Nantes](https://www.faimaison.net).

<figure>
  <img src="images/2026/06/YunoHost-internet_topologies.png" alt="">
  <figcaption>Schéma en anglais issu de <a href="https://doc.old.yunohost.org/en/selfhosting">la documentation YunoHost</a></figcaption>
</figure>

Je me suis contenté, au fil des années, d'installer et gérer quelques serveurs, hébergés chez différents fournisseurs (je retrace l'historique plus bas).
<br>
Dès le départ, c'était un choix « raisonné » : même si la démarche d'auto-hébergement à domicile me semble séduisante, sur le plan idéologique tout comme sur le plan de l'indépendance / autonomie, j'y vois aussi de sérieux inconvénients : manque de compétences personnelles, devoir gérer le matériel physique et son usure / remplacement, moindre efficience énergétique en l'absence de mutualisation des resources, ... et flemme aussi il faut bien l'avouer 😅

Pour une réflexion plus poussée à ce sujet, je vous recommande par exemple cette présentation d'[aeris](https://imirhil.fr/) à l'APRIL il y a quelque temps : [Auto-hébergement : la fausse bonne idée ?](https://www.april.org/auto-hebergement-fausse-bonne-idee-aeris)

Après plus de 10 ans, à titre personnel j'en tire le bilan suivant : **plus on souhaite maîtriser et auto-héberger de services et de « couches basses », plus cela nécessite du temps, et plus on aura à gérer des mauvaises surprises **.

Cela peut paraître évident, mais je pense que c'est à garder en tête lorsqu'on se lance dans l'aventure de l'auto-hébergement&nbsp;: mieux vaut parfois « choisir ses chevaux de bataille », débuter par un projet modeste et avoir la satisfaction de le mener au bout, plutôt que d'être trop ambitieux. Bien sûr d'autres choix sont possibles, et héberger un [Raspberry Pi](https://fr.wikipedia.org/wiki/Raspberry_Pi) chez soi avec quelques services minimalistes peut être un super point de départ !

Enfin, pour conclure ce préambule, je voudrais évoquer le sujet de la **sécurité informatique**. C'est un sujet auquel je m’intéresse avec curiosité depuis longtemps (je suis par exemple un fidèle auditeur de [NoLimitSecu](https://www.nolimitsecu.fr/)), mais ce n'est pas mon domaine d'expertise professionnelle. **Gérer mon propre serveur a été une bonne occasion d'apprendre**, et de mettre en pratique certaines bonnes pratiques de sécurité, mais je vous encourage vivement à vous renseigner sur ce sujet si vous souhaitez vous lancer, et à toujours garder en tête qu'**il existera toujours un risque que vous perdriez le contrôle de votre serveur et des données associées**.

Voici une anecdote pour illustrer cela :

Ma première expérience d'auto-hébergement était il y a une vingtaine d'années, lorsque j'étais adolescent et que j'ai déployé mon premier site WordPress. Et ça n'a pas loupé : après quelques semaines, il avait été [_defaced_](https://fr.wikipedia.org/wiki/D%C3%A9facement) par des hackers, et bien sûr je n'avais pas de _backup_ de toutes les données que j'avais publié... Une première expérience cruelle mais instructive.

Aujourd'hui ma _stack_ technique est un peu plus solide, mais loin d'être parfaite.
Je n'ai pas la même ambition de sécurité et je n'emploie pas les même outils sur mon humble petit serveur que dans un cadre professionnel.
<br>
En partageant cet article je suis conscient de prendre un risque de fournir aussi des informations utiles à de potentiels acteurs malveillants, et c'est pourquoi je ne rentrerai pas toujours dans tous les détails.

## Petit historique
Tout a commencé en 2013, lorsque mon oncle Sébastien, également ingénieur en informatique, m'a proposé de mettre en place un serveur ensemble.
L'origine du projet : une volonté d'auto-héberger un lecteur de flux RSS (Google venait d'annoncer la fin de Google Reader) et un serveur d'emails.
C'est amusant de relire nos échanges email de l'époque : on évoquait [la mythique conférence de Benjamin Bayard : Internet Libre ou Minitel 2.0](https://www.fdn.fr/actions/confs/internet-libre-ou-minitel-2-0/).

Nous étions alors partis sur une offre [Kimusfi d'OVH](https://www.kimsufi.com/) : KS-2G à 18 € par mois, sous Ubuntu 12.04.
Initialement nous avions installé Apache comme serveur HTTP, [OwnCloud](https://owncloud.com/), [RainLoop](https://www.rainloop.net/) comme _webmail_ (avec emploi de `postfix` & `dovecot` derrière), et configuré `fail2ban` & `iptables` pour sécuriser un peu le serveur.
J'avais ensuite mis en place un blog avec [ghost](https://ghost.org/), une galerie d'images avec [MiniGal Nano](https://sebsauvage.net/wiki/doku.php?id=minigal_nano) et une instance [Shaarli](https://shaarli.readthedocs.io), qui existe toujours aujourd'hui : [chezsoi.org/shaarli](https://chezsoi.org/shaarli). Mon petit défi à l'époque avait été de bidouiller un script Python pour importer mes favoris FireFox dans Shaarli. L'ambition était à l'origine de partager cette instance Shaarli avec mes anciens colocs, mais le projet n'a finalement pas abouti.

<div class="side-by-side">
  <img src="images/2026/06/MinigalNano-logo.png" alt="Logo de MiniGal Nano">
  <img src="images/2026/06/Shaarli-logo.png" alt="Logo de Shaarli">
</div>

Fin 2014, nous avons testé quelques mois un VPS hébergé chez [PulseHeberg](https://pulseheberg.com/) : VPS DC M à 15 € par mois.
Nous avons alors basculé côté emails sur [iRedMail](https://www.iredmail.org/admin_panel.html),
et nous avons installé [YunoHost](https://yunohost.org/).
Mais nous avions régulièrement des indispos, et nous avons décidé après quelques mois de finalement opter pour un serveur Dedibox (une filiale d'Iliad qui a ensuite fusionné avec Online.net puis est devenu Scaleway), pour 19,19 € par mois.
Nous compartimentons alors le serveur en [conteneurs LXC](https://fr.wikipedia.org/wiki/LXC).
Nous basculons aussi d'Apache vers [nginx](fr.wikipedia.org/wiki/NGINX) comme serveur HTTP, et installons [bind](https://fr.wikipedia.org/wiki/BIND) pour gérer la partie DNS.
J'ai d'ailleurs des souvenirs un peu douloureux d'avoir bataillé au fil des années pour faire cohabiter `bind9`, `dnsmasq` et `systemd-resolved` sur le serveur 😅

Côté backup, un _cron job_ quotidien exécutait le script [`backup-manager`](https://github.com/sukria/Backup-Manager) pour exporter les données sur un serveur via FTP. Il a fallu pas mal d'itérations et quelques patchs pour qu'il sauvegarde correctement les fichiers que l'on souhaitait preserver.

En 2026-2017 nous avons basculé de OwnCloud vers [NextCloud](https://nextcloud.com/fr/), et adopté [Let's Encrypt](https://letsencrypt.org/) pour générer des certificats SSL pour tous nos sites web.
Nous avons brièvement hébergé une instance Gitlab, rapidement remplacé par [Gogs](https://gogs.io), plus léger, pour héberger quelques repos `git`. J'ai aussi décidé de remplacer ghost par un moteur de blog statique, et adopté [Pelican](https://getpelican.com/) ([article dédié](https://chezsoi.org/lucas/blog/migration-du-blog-de-ghost-a-pelican.html)).

<img alt="" src="images/2017/08/ghost2pelican.png" style="max-width: 16rem">

_Fast forward_ en 2025, après de longues années de bons & loyaux services, notre [serveur Scaleway crashe](panne-de-serveur.html).
Nous décidons alors de basculer vers des petits [VPS chez Infomaniak](https://www.infomaniak.com/fr/hebergement/vps-cloud) : 1 CPU, 2 Go RAM, 20 Go de stockage, Ubuntu 24.04 LTS, à seulement 3,24 € par mois chacun.

## Adoption d'Ansible
La remise en place de mes services suite au crash du serveur précédent a été l'occasion d'adopter [**Ansible**](https://docs.ansible.com/) pour automatiser leur déploiement, avec une approche _Infrastructure As Code_. C'est une méthode que j'emploie régulièrement dans mon travail depuis des années, mais plutôt avec des outils comme Puppet, Terraform ou AWS CDK.
Pour mes usages personnels, j'ai choisi Ansible car j'étais curieux de découvrir cet outil, et que j'ai un faible pour les solutions issues de l'écosystème Python 🐍🥰.

<img alt="" src="images/2026/06/ansible.png" style="max-width: 30rem">

Au final je suis très content de ce choix !
Par rapport aux autres outils que j'ai cité, ce n'est sans doute pas le mieux conçu globalement : il n'y a pas de gestion d'état "global" du système, la structure des _playbooks_ est assez "figée" et peu modulaire, et dans l'ensemble j'ai vraiment eu l'impression de faire du bricolage.
Mais ça marche !
Et je me suis beaucoup amusé à bricoler ainsi 😁

Parmi les points forts :

- de nombreuses _tasks_ natives (_builtin_) sont disponibles. Combinées avec le système de _templates_ Jinja, elles m'ont permis de très facilement implémenter les étapes d'installation de mes services, et notamment la création de _users_ et de services `systemd` dédiés. À ce sujet je recommande [ce papier de l'ANSSI pour "durcir" sa configuration systemd](https://www.sstic.org/media/SSTIC2017/SSTIC-actes/durcissement_systeme_avec_systemd/SSTIC2017-Article-durcissement_systeme_avec_systemd-ravier.pdf).
- [`ansible-lint`](https://docs.ansible.com/projects/lint/) est très facile à mettre en place, et m'a appris à adopter de nombreuses bonnes pratiques
- il existe quelques optimisations importantes à mettre en place pour rendre Ansible plus rapide, comme détaillé par exemple dans [cet article du site de Stéphane Robert](https://blog.stephane-robert.info/docs/infra-as-code/gestion-de-configuration/ansible/ansible-increase-performance/)

Je vais continuer à employer Ansible pendant un moment,
mais si je dois tester un nouvel outil à l'avenir, je me pencherai sans doute sur [Nix](https://nixos.org/).

## Serveur HTTP
La migration de serveur a été l'occasion pour moi de tester une alternative à `nginx` :
[`caddy`](https://caddyserver.com/), qui gère notamment automatiquement les certificats TLS avec LetsEncrypt.

Pour un serveur HTTP basique, je trouve que c'est un très bon choix.
Les performances me semblent bonnes, son language de configuration est assez facile à prendre en main, et la plupart du temps les valeurs par défaut font parfaitement l'affaire.

<img alt="" src="images/2026/06/Caddyserver_logo_light.svg.png" style="max-width: 16rem">

Voici quelques trucs & astuces à vous partager :

Pour découper la configuration `caddy` en plusieurs fichiers,
j'ai employé cette instruction dans mon `Caddyfile` : `import /etc/caddy/*.caddy`

Une configuration pour avoir des _access logs_ avec une rotation automatique :
```
{
	log main {
		include http.log.access.main
		output file /var/log/caddy/access.log {
			roll_size 100mb
			roll_keep 5
		}
		format json
	}
}
chezsoi.org {
	log main
	...
}
```

J'ai mis en place une page [/now](https://nownownow.com/) : [chezsoi.org/now](https://chezsoi.org/now)

J'ai employé [Google PageSpeed Insights](https://pagespeed.web.dev/) & [WebPageTest](https://www.webpagetest.org/) pour identifier les améliorations de performances configurables au niveau du serveur HTTP.

Une commande utile pour valider les fichiers de configuration : `caddy validate --config /etc/caddy/Caddyfile`

J'ai aussi mis en place un _tag_ Ansible pour pouvoir juste redémarrer le serveur :
`ansible-playbook -i inventory.ini site.yml --tags http-server,reload-only`

```yaml
# Provide a "reload-only" tag:
- become: true
  tags: ["never", "reload-only"]
  block:
    - name: Update Caddyfile and reload
      ansible.builtin.template:
        src: Caddyfile
        dest: /etc/caddy/
        owner: root
        group: root
        mode: "644"
      notify: Reload caddy
```

## Backups
J'emploie désormais un _cron job_ qui invoque [rclone](https://rclone.org/), pour réaliser un backup quotidien. C'est un outil très performant, capable de ne sauvegarder que les fichiers modifiés depuis la dernière exécution, et qui gère de nombreux types de stockage distant.

<img alt="" src="images/2026/06/Rclone_wide_logo.svg.png" style="max-width: 16rem">

## Supervision
Elle est basée sur deux piliers :

* [Gatus](https://gatus.io/), un outil de _monitoring_ actif, très performant et facile à mettre en place. Il supervise tous mes services HTTP et quelques autres. Il fournit un _dashboard_ et est capable d'envoyer des notifications lorsqu'un service est KO. Je l'adore ❤️.

<img alt="" src="images/2026/06/Gatus-logo.webp" style="max-width: 16rem">

* pour recevoir des alertes par SMS, j'emploie tout simplement l'API Free. Son usage est par exemple détaillé dans cet article : [ti1.free.fr](http://ti1.free.fr/index.php/free-senvoyer-des-notifications-par-sms/). Durant longtemps j'étais juste abonné au [forfait Free à 2€ par mois](https://mobile.free.fr/fiche-forfait-2-euros), et cette fonctionnalité incluse d'API d'envoi de SMS est super pratique.

Pour superviser mes _cron jobs_, je fais en sorte qu'en cas d'échec ils suppriment un fichier `.status` servi par le serveur HTTP. Ce fichier est surveillé par Gatus, et donc s'il disparaît (HTTP 404) je suis automatiquement prévenu qu'un _cron job_ a échoué.
J'emploie ce système pour être par exemple être alerté si mon espace disque se réduit anormalement et descend en dessous d'un certain seuil.

En complément j'emploie :

* [UptimeRobot](https://uptimerobot.com/) qui a une offre gratuite très complète, capable même d'envoyer des notifications, très utile pour détecter quand tout sur le serveur - y compris Gatus - est KO

* [GoAccess](https://goaccess.io/) est un super outil pour consulter ses logs, et notamment ceux de Caddy en employant cette configuration de `.goaccessrc` :

```
log-file /var/log/caddy/access.log
log-format CADDY
```

## Services hébergés
Voici quelques-uns des services que j'héberge :

* des **galeries d'images** avec [Sigal](https://sigal.readthedocs.io/en/latest/), comme par exemple celle-ci : [chezsoi.org/lucas/wwcb](https://chezsoi.org/lucas/wwcb/)
* un **wiki** avec [Dokuwiki](https://www.dokuwiki.org/dokuwiki)
* un serveur de **commentaires** pour mon blog, avec [Isso](https://isso-comments.de/)
* un serveur **Gopher** : le contenu de mon blog est accessible via [Gopher](https://fr.wikipedia.org/wiki/Gopher), un protocole alternatif à HTTP très simple et économe
* **serveur CalDAV**, pour avoir un calendrier partagé avec mon épouse, en le combinant sous Android avec [DAVx⁵](https://www.davx5.com/)
* une instance [Shaarli](https://shaarli.readthedocs.io) : [chezsoi.org/shaarli](https://chezsoi.org/shaarli)
* une instance [YOURLS](https://yourls.org/), un **raccourcisseur d'URL** permettant de compter le nombre de visites 
* une instance de [youtube-dl-server](https://github.com/manbearwiz/youtube-dl-server) légèrement personnalisée

## WordPress
Il m'arrive d'héberger quelques sites web pour des proches ou des associations, _cf._ [cet article précédent](quelques-sites-web-que-jai-concu.html). Certains d'entre eux sont des sites WordPress, et j'ai appris beaucoup de choses au fil des ans pour les héberger correctement.

J'étais à la base parti de ce _playbook_ Ansible que j'ai amélioré et adapté à mes besoins : [github.com/nerrad/wordpress-ansible-playbook](https://github.com/nerrad/wordpress-ansible-playbook).

J'ai eu souvent besoin de personnaliser les métadonnées publiques de sites WordPress (balises HTML `<meta>`). Vous trouverez des _plugins_ dédiés à cela, mais en définitive j'ai trouvé bien plus pratique de passer par des _hooks_ PHP :
```php
function head_meta_html() {
    $post = get_post();
    if ($post != null && $post->post_status == 'private') {
        echo '<meta name="robots" content="noindex">'.PHP_EOL;
    }
    echo <<<'EOD'
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta content="on" name="twitter:dnt">
<meta content="FR-49" name="geo.region">
EOD;
}
add_action('wp_head', 'head_meta_html');
```

Je ne maîtrise pas encore pleinement la personnalisation des thèmes WordPress, que je trouve assez complexe. Il m'arrive de définir des styles CSS personnalisés, mais je n'ai pas encore trouvé mieux que d'employer des sélecteurs `.page-id-XXX` dans la feuille de style du thème pour cibler des pages en particulier, ce qui me semble loin d'être idéal...

Lorsqu'on connaît les bases de PHP, il est assez facile de construire un petit plugin "maison". Sur [laubergedesreveurs.fr](https://laubergedesreveurs.fr/) par exemple, j'ai ainsi pu très facilement insérer en pied de page un petit personnage qui change à chaque visite.

## Expérimentations
Quelques projets que j'ai tenté d'héberger mais qui n'ont pas abouti,
soit car ils étaient au final trop complexes à installer ou gourmands en ressources,
soit par manque d'intérêt en définitive :

* [Etherpad](https://github.com/ether/etherpad) : un super projet de document partagé en ligne. Je l'ai utilisé pendant plusieurs années avant de finalement le délaisser, employant ponctuellement [FramaPad](https://framapad.org/abc/fr/) à la place
* Piwik, alternative gratuite à _Google Analytics_, dont je me passe au final très bien. J'ai aussi testé [AWSStats](https://awstats.sourceforge.io/) mais je n'ai jamais réussi à bien le configurer pour qu'il produise de données fiables.
* Splunk, pour superviser mes logs, finalement trop "lourd" et gourmand en ressources
* [soundtrack.io](https://github.com/martindale/soundtrack.io) : _self-hosted collaborative music playing application_
* [Searx](https://fr.wikipedia.org/wiki/Searx) : un métamoteur de recherche libre
* serveur XMPP / Jabber, puis serveur [matrix](https://fr.wikipedia.org/wiki/Matrix_(protocole)) : je ne les utilisais au final jamais...

## Conclusion
Mon expérience de l'auto-hébergement est globalement très positive, et je recommande à toute personne déjà intéressée par Linux, ou qui programme un peu, de s'y essayer un jour. Vous pouvez vous lancer avec un micro-budget, et si cela vous plaît, vous découvrirez **un terrain de jeu sans limite**.

Je vous conseille par contre de ne pas héberger de service ou de données trop sensibles ou critiques sans un peu d'expérience. Je recommande aussi de prévoir un plan en cas de _crash_ ou de cyberattaque.
Sachez aussi connaître vos limites : personnellement, je me suis résolu à ne pas héberger mes emails moi-même car cela me semble aujourd'hui trop complexe et critique.

Enfin, je pense qu'il très intéressant de se lancer dans cette aventure à plusieurs. Sans mon oncle, je ne sais pas si je me serais lancé. Donc parlez-en autour de vous, dans votre famille, avec vos potes, dans votre association... Et lancez-vous dans l'aventure à plusieurs, c'est plus amusant !

Joyeux auto-hébergement à tous 😊

<script>
['article h2', 'article h3'].forEach(selector => {
  document.querySelectorAll(selector).forEach(title => {
    title.id = title.textContent.toLowerCase()
                    .replace(/[()?!:,'&@]/g, '')
                    .replace(/[à]/g, 'a')
                    .replace(/[ç]/g, 'c')
                    .replace(/[éêè]/g, 'e')
                    .replace(/[ï]/g, 'i')
                    .replace(/ /g, '-')
  })
})
</script>

<style>
.side-by-side {
  display: flex;
  justify-content: center;
  align-items: center;
}
.side-by-side > * {
  margin: 1rem;
  display: block;
  max-width: 33%;
}
</style>

<!-- Com'
* [x] https://linuxfr.org/users/lucas-c/liens/auto-hebergement-petit-bilan
* [x] https://old.reddit.com/r/AutoHebergement/comments/1ucwee7/auto_h%C3%A9bergement_petit_bilan/?
-->
