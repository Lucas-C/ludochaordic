Title: SpyFall en print&play
Date: 2015-10-20 19:10
Tags: lang:fr, template, printplay, svg, traduction, jeu-de-societe, cards, jeux
Slug: spyfall-en-print
---
![The Spy character from Team Fortress 2](images/2015/10/spy-2.jpg)

La semaine dernière, j'ai enfin offert à un ami le petit jeu de cartes que j'ai bricolé ces dernières semaines.

Comme je pense qu'ils pourra en amuser plus d'un, voici une version prête à imprimer !

<https://chezsoi.org/lucas/spyfall> ([PDF, 3.47Mo](/lucas/spyfall/spyfall_print-and-play.pdf))

Aperçu :

![Photo du jeu de cartes imprimé & découpé](/lucas/spyfall/printed_deck.jpg)

# Le jeu
Pour une description complète, je vous recommande [la review de Swatsh sur VindJeu](http://www.vindjeu.eu/2015/01/23/spyfall-agent-trouble/).

Cette version à pour particularité que chaque lieu est une référence à un jeu vidéo
(avant l'ajout de 27 illustrations supplémentaires grâce à Lukas).
Retrouverez-vous tous les clins d'oeil ? :)

Les réponses : <https://chezsoi.org/lucas/spyfall/img-srcs-answers.txt>

Les règles complètes en anglais: [PDF, 1,58Mo](http://international.hobbyworld.ru/download/rules/international/Spyfall_rules_ENG.pdf)

<img alt="Animation tirée de The Big Lebowsky" src="images/wwcb/OnlyOneToGiveAShitAboutRules.gif">

# Comment l'imprimer
Tout simplement avec Chrome, en imprimant directement sur papier cartonné ou bien en choisissant "imprimer au format PDF" comme destination dans la fenêtre d'impression (CTRL+P).

# Création de cartes au format SVG
Cette version a été entièrement réalisé avec [Adobe Snap.svg](http://snapsvg.io), en prennant exemple sur [le travail de Kevin Hakanson sur Fluxx](http://www.slideshare.net/kevinhakanson/make-your-own-print-play-card-game-using-svg-and-java-script) ([son repo GitHub](https://github.com/hakanson/tccc16)). Un grand merci à lui pour l'idée !

Pour les devs, je recommande vivement le procédé, qui permet du "templating" de cartes très puissant, de la gestion de versions et du partage sur le web très simplement.

Bien mieux que me précédent bricolages de cartes sour Word...

<img alt="Sa place est dans un musée !" src="images/wwcb/SaPlaceEstDansUnMusée.gif">

L'idée originale de réaliser une version maison de ce jeu revient à mon ami, qui m'a fait découvrir l'existence de 2 apps, au code open-source, pour jouer sur smartphone:

- <s><http://spyfall.meteor.com></s> → <https://spyfall.tannerkrewson.com>
- <http://spyfall.adrianocola.com>
- <https://www.spyfall.app>

Comme le travail de localisation avait déjà été fait sur ces apps, je l'ai simplement réutilisé dans cette version print & play. Merci à Evan Brumley et tous les gens qui ont contribué aux traductions !

Suite du développement de cette page web, j'en ai retiré 2 petites leçons :

- **ne pas essayer de créer des éléments HTML avec `paper.el` ou `Snap._.$`**. C'est très technique, mais je m'en suis mordu les doigts: ces fonctions peuvent uniquement créer des éléments SVG car ils utilient [le namespace XML](//github.com/adobe-webplatform/Snap.svg/blob/master/src/svg.js#L93).

- le style CSS appliqué aux éléments, et plus spécifiquement la propriété `text-shadow`, est ignoré par le navigateur lors de l'export en PDF.

Pour cette fois, pas de repo GitHub dédié au projet : l'ensemble du code source nécessaire pour reproduire ce résultat sont accessible dans le code source de la page web !

<img alt="Tatouage d'une balise HTML head" src="images/wwcb/head_body_tatoo.jpg">

Enfin, un remerciement à Dan Hetteix (membre de TheNounProject), qui a créé l'icône d'espion utilisé sur les cartes.


**[EDIT 2020/04/26]** : Thanks to Lukas, I added illustrations for all cards that missed one, using the following images :

- *art museum* ([image source](https://www.piqsels.com/en/public-domain-photo-sjsit))
- *baseball stadium* ([image source](https://pxhere.com/en/photo/64540))
- *candy factory* ([image source](https://www.needpix.com/photo/291294/candy-candy-store-chocolate-m-ms-sweet))
- *cat show* ([image source](https://publicdomainpictures.net/fr/view-image.php?image=76777&picture=dog-show-affiche-de-bande-dessinee))
- *cemetery* ([image source](https://www.pexels.com/photo/selective-focus-photo-of-cemetery-lantern-720730/))
- *coal mine* ([image source](https://www.pxfuel.com/en/free-photo-oxhud))
- *construction site* ([image source](https://pxhere.com/en/photo/89214))
- *day spa* ([image source](https://www.pikrepo.com/fvgmv/trevi-fountain-rome-italy))
- *embassy* ([image source](https://pxhere.com/en/photo/757223))
- *gas station* ([image source](https://www.piqsels.com/en/public-domain-photo-spaqi))
- *harbor docks* ([image source](https://fr.wikipedia.org/wiki/Fichier:Docks_and_shipping,_Hamburg,_Germany-LCCN2002713698.jpg))
- *jail* ([image source](https://pxhere.com/en/photo/1095378))
- *jazz club* ([image source](https://pxhere.com/en/photo/1084769))
- *library* ([image source](https://pxhere.com/en/photo/707871))
- *movie studio* ([image source](https://pxhere.com/en/photo/1588369))
- *ocean liner* ([image source](https://pxhere.com/en/photo/1233488))
- *retirement home* ([image source](https://pxhere.com/en/photo/782117))
- *race track* ([image source](https://www.pickpik.com/transfagarasan-drone-road-green-forest-winding-36518))
- *rock concert* ([image source](https://www.pickpik.com/man-guitar-in-concert-lights-people-music-76510))
- *school* ([image source](https://pxhere.com/en/photo/1147031))
- *sightseeing bus* ([image source](https://www.pexels.com/photo/red-tower-hill-bus-1837590/))
- *subway* ([image source](https://pxhere.com/en/photo/2767))
- *supermarket* ([image source](https://unsplash.com/photos/53SEwmFQLqU))
- *the united nations* ([image source](https://www.pickpik.com/microphone-active-talk-conference-meeting-audio-38534))
- *university* ([image source](https://unsplash.com/photos/TJIF_x88tVk))
- *vineyard* ([image source](https://www.pxfuel.com/en/free-photo-jepqq))
- *wedding* ([image source](https://www.pexels.com/photo/woman-holding-white-calla-lily-flowers-on-sitting-beside-man-wearing-black-suit-265871/))

I sincerely appreciate the contribution, thanks again Lukas !
