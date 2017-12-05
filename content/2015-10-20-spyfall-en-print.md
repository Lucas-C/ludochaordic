Title: SpyFall en print&play
Date: 2015-10-20 19:10
Tags: lang:fr, template, printplay, svg, i18n, jeu-de-societe, cards, jeux
Slug: spyfall-en-print
---
![The Spy character from Team Fortress 2](images/2015/10/spy-2.jpg)

La semaine dernière, j'ai enfin offert à un ami le petit jeu de cartes que j'ai bricolé ces dernières semaines.

Comme je pense qu'ils pourra en amuser plus d'un, voici une version prête à imprimer !

<https://chezsoi.org/lucas/spyfall> ([PDF, 3.47Mo](/lucas/spyfall/spyfall_print-and-play.pdf))

# Le jeu
Pour une description complète, je vous recommande [la review de Swatsh sur VindJeu](http://www.vindjeu.eu/2015/01/23/spyfall-agent-trouble/).

Cette version à pour particularité que chaque lieu est une référence à une jeu vidéo. Retrouverez-vous tous les clins d'oeil ? :)

Les règles complètes en anglais: [PDF, 1,58Mo](http://international.hobbyworld.ru/download/rules/international/Spyfall_rules_ENG.pdf)

<img src="images/wwcb/OnlyOneToGiveAShitAboutRules.gif">

# Comment l'imprimer
Tout simplement avec Chrome, en imprimant directement sur papier cartonné ou bien en choisissant "imprimer au format PDF" comme destination dans la fenêtre d'impression (CTRL+P).

# Création de cartes au format SVG
Cette version a été entièrement réalisé avec [Adobe Snap.svg](http://snapsvg.io), en prennant exemple sur [le travail de Kevin Hakanson sur Fluxx](http://www.slideshare.net/kevinhakanson/make-your-own-print-play-card-game-using-svg-and-java-script) ([son repo GitHub](https://github.com/hakanson/tccc16)). Un grand merci à lui pour l'idée !

Pour les devs, je recommande vivement le procédé, qui permet du "templating" de cartes très puissant, de la gestion de versions et du partage sur le web très simplement.

Bien mieux que me précédent bricolages de cartes sour Word...

<img src="images/wwcb/SaPlaceEstDansUnMusée.gif">

L'idée originale de réaliser une version maison de ce jeu revient à mon ami, qui m'a fait découvrir l'existence de 2 apps, au code open-source, pour jouer sur smartphone:

- <http://spyfall.meteor.com>
- <http://spyfall.adrianocola.com>

Comme le travail de localisation avait déjà été fait sur ces apps, je l'ai simplement réutilisé dans cette version print & play. Merci à Evan Brumley et tous les gens qui ont contribué aux traductions !

Suite du développement de cette page web, j'en ai retiré 2 petites leçons :

- **ne pas essayer de créer des éléments HTML avec `paper.el` ou `Snap._.$`**. C'est très technique, mais je m'en suis mordu les doigts: ces fonctions peuvent uniquement créer des éléments SVG car ils utilient [le namespace XML](//github.com/adobe-webplatform/Snap.svg/blob/master/src/svg.js#L93).

- le style CSS appliqué aux éléments, et plus spécifiquement la propriété `text-shadow`, est ignoré par le navigateur lors de l'export en PDF.

Pour cette fois, pas de repo GitHub dédié au projet : l'ensemble du code source nécessaire pour reproduire ce résultat sont accessible dans le code source de la page web !

<img src="images/wwcb/head_body_tatoo.jpg">

Enfin, un remerciement à Dan Hetteix (membre de TheNounProject), qui a créé l'icône d'espion utilisé sur les cartes.
