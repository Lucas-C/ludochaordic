Title: Quelques sites web que j'ai conçu
Date: 2025-03-10 10:00
Tags: lang:fr, personal-project, kawasso, website, ecoconception, association, creative-commons, libre-software, open-source, source-code, static-site-generator, python, gratuit, prog
---
Au cours des 18 derniers mois, j'ai eu l'occasion de concevoir plusieurs sites web pour des proches et des associations où je suis bénévole.

Dans cet article, je reviens sur mes choix de solutions pour les mettre en place,
et partage mes réflexions concernant les alternatives pour concevoir de "petits" sites web "vitrines",
lorsque l'on est dans mon cas : avoir des compétences en développement logiciel
et vouloir créer rapidement des sites facilement maintenables.


## Sites statiques
<div class="side-by-side">
    <a href="https://renardeau.chezsoi.org/">
        <figure>
            <img alt="Capture d'écran du site web" src="images/2025/03/renardeau.chezsoi.org.png">
            <figcaption>renardeau.chezsoi.org</figcaption>
        </figure>
    </a>
    <a href="https://linstantpresent.chezsoi.org/">
        <figure>
            <img alt="Capture d'écran du site web" src="images/2025/03/linstantpresent.chezsoi.org.png">
            <figcaption>linstantpresent.chezsoi.org</figcaption>
        </figure>
    </a>
</div>

<div class="side-by-side">
    <a href="https://mush-radio.chezsoi.org/">
        <figure>
            <img alt="Capture d'écran du site web" src="images/2025/03/mush-radio.chezsoi.org.png">
            <figcaption>mush-radio.chezsoi.org</figcaption>
        </figure>
    </a>
    <a href="https://atelier-coala.chezsoi.org/">
        <figure>
            <img alt="Capture d'écran du site web" src="images/2025/03/atelier-coala.chezsoi.org.png">
            <figcaption>atelier-coala.chezsoi.org</figcaption>
        </figure>
    </a>
</div>

Les sites statiques sont les sites web les plus **simples** techniquement :
pas de base de donnée, pas de code applicatif exécuté côté serveur,
pas même de framework Javascript _frontend_...

Cela offre plusieurs avantages :

* les sites sont bien **moins vulnérables à des cyberattaques**.
* l'**hébergement est très simple**, ne nécessitant qu'un serveur HTTP, et peut donc même se faire sur [GitHub Pages](https://pages.github.com/) / [Gitlab Pages](https://docs.gitlab.com/user/project/pages/) (par exemple sur [Framagit](https://docs.framasoft.org/fr/gitlab/gitlab-pages.html)).
* les sites sont beaucoup plus **économes en ressources** : cela rejoint les notions d'[écoconception](https://fr.wikipedia.org/wiki/%C3%89coconception) et d'[impact environnemental du numérique](https://fr.wikipedia.org/wiki/Impact_environnemental_du_num%C3%A9rique). 3 des sites ci-dessus mettent cela en valeur via des sous-pages dédiées à l'écoconception web.

Niveau design, j'ai employé des templates HTML web sous licence _Creative Commons_ : deux sont issus de [HTML5UP](https://html5up.net/), un de [FreeHTML5.co](https://freehtml5.co/), et un de [HTML Codex](https://htmlcodex.com/).

Techniquement, un simple script Python se charge de construire le site web,
en employant des templates [jinja2](https://jinja.palletsprojects.com)
afin de réemployer la même structure pour toutes les pages HTML.

Le code source de chacun de ces sites web est open-source,
disponible sur [Framagit](https://docs.framasoft.org/fr/gitlab/).

Bien sûr les sites statiques comportent aussi d'important désavantages :

* certaines fonctionnalités sont tout simplement impossibles, comme un simple formulaire de contact.
* la modification du contenu nécessite un minimum de connaissances techniques, et le bénéficiaire du site web ne peut en général pas être autonome pour réaliser des changements.

Ce type de site web me semble donc idéal pour des **sites vitrines** nécessitant très peu d'évolutions une fois en place.


## Sites Odoo
Dans le cadre d'associations où je suis bénévole,
j'ai souhaité mettre en place des sites web tout simples,
afin de présenter brièvement les actions de l'association.

L'année dernière j'ai donc choisi d'expérimenter
avec l'offre gratuite d'[odoo.com](https://www.odoo.com/fr_FR)
pour cela :

<div class="side-by-side">
    <a href="https://kawasso.odoo.com/">
        <figure>
            <img alt="Capture d'écran du site web" src="images/2025/03/kawasso.odoo.com.png">
            <figcaption>kawasso.odoo.com</figcaption>
        </figure>
    </a>
    <a href="https://afr-champtoce.odoo.com/">
        <figure>
            <img alt="Capture d'écran du site web" src="images/2025/03/afr-champtoce.odoo.com.png">
            <figcaption>afr-champtoce.odoo.com</figcaption>
        </figure>
    </a>
</div>

Cette fois, il est bien possible :

* d'avoir un formulaire de contact, redirigeant les messages vers l'adresse email de chaque association.
* de modifier le contenu du site web sans connaissance technique particulière, grâce une interface en _overlay_ du site, assez ergonomique.

Mon retour d'expérience après quelques mois est que c'est **une offre très intéressante pour les associations**, mais qu'il existe tout de même quelques limitations notables, assez compréhensibles puisqu'il s'agit là uniquement de l'offre gratuite d'`odoo.com` :

* Odoo est open-source, mais il n'est pas possible d'auto-héberger un site Odoo conçu avec l'offre gratuite d'`odoo.com`, sans avoir de _licence key_ correspondant à une offre payante

* sur `odoo.com`, il est possible de télécharger des _backups_ de la base de donnée du site, mais **pas de les restaurer**

<img alt="Capture d'écran du panneau d'administration des bases de donnée d'Odoo"
     src="images/2025/03/odoo-database.png" style="max-height: 15rem">


## Autres solutions
Lors de futurs projets, je compte expérimenter d'autres solutions hybrides,
permettant de concevoir des sites web statiques
où la modification du contenu peut être réalisée par un utilisateur non technique,
via une interface dédiée.

Dans le jargon des développeurs web, on parle de _headless CMS_, _git-based CMS_ et parfois de modèle Jamstack.
Je songe en particulier à tester ces outils :

* [FrontAid](https://frontaid.io/): free, password-less login, GitHub-based, Swiss - BUT: closed source, no preview system
* [Lektor](https://www.getlektor.com/): Python-based with jinja templates, but [admin access must be setup manually](https://github.com/lektor/lektor/issues/237#issuecomment-267307581), _e.g._ using `nginx`


<style>
article figcaption { margin-top: .5rem; }
.side-by-side {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: wrap;
}
@media (min-width:768px) {
  .side-by-side > * {
    display: block;
    margin: 1rem;
    max-width: 45%;
  }
}
</style>
