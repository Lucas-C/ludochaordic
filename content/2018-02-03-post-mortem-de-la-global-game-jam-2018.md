Title: Post-mortem de la Global Game Jam 2018
Date: 2018-02-03 14:00
Tags: lang:fr, game-jam, video-game, indie-game, phaser-js, creative-commons, nantes, ensimag, oui.sncf, gamedesign, post-mortem, open-source, jeux
Slug: post-mortem-de-la-global-game-jam-2018
---

Le week-end dernier, j'ai participé à ma première [Global Game Jam](https://globalgamejam.org), à Nantes.
Dans cet article, je vais vous présenter comment elle s'est déroulée,
et faire le point sur ce qui a plus ou moins bien marché pour notre projet,
[The King Must Know](https://globalgamejam.org/2018/games/king-must-know), dont voici l'écran d'accueil :

[![Écran d'accueil du jeu](images/2018/01/GGJ2018_GameIntroScreenshot.png)](https://lucas-c.github.io/OuiJam2018/build/)

J'avais déjà participé à quelques game jams durant mes études à l'[Ensimag](http://ensimag.grenoble-inp.fr).
Contraintes de colocation obligent, nous nous retrouvions à 8 dans ma chambre d'étudiant d'une quinzaine de mètres carrés, entre 11h du matin et 22h.
On codait [comme des pieds](https://github.com/Lucas-C/ImagGameJams), on faisait nos _sprites_ sous Paint, et on s'amusaient comme des petits fous 😋 🎮 😵

Cette fois, la Global Game Jam était organisée par les écoles E-art Sup & Epitech dans leurs locaux à Nantes.
Merci à eux pour la super organisation, et pour nous avoir prêté leurs locaux le temps du week-end !
Avec deux collègues de [oui.sncf](https://www.oui.sncf), Henri & Loïc, nous avions déjà décidé de former une équipe ensemble pour l'occasion.

<figure>
  <img alt="Photo de l'équipe" src="images/2018/01/GGJ2018_TheTeam.jpg">
  <figcaption>Une équipe qui roxe du poney bleu !</figcaption>
</figure>

Voici grosso-modo comment s'est déroulé le week-end:

- **vendredi 18h30** : environ une centaine de participants se tassent dans un amphi d'E-art Sup, pour donner le coup d'envoi.
Nous sommes clairement parmi les moins jeunes des participants, la plupart étant des étudiants.
Une introduction par [Florent De Grissac](http://www.casusludi.com) nous invite à réfléchir à la raison pour laquelle nous faisons des jeux,
et nous détaille le programme de la GGJ ainsi que quelques conseils.
La [_keynote_ officielle de la GGJ](https://www.youtube.com/watch?v=3Roxls_2W2M) est ensuite diffusée,
assez hallucinante par moments, avec une session d'aérobic en collants roses fluos.
Enfin, **le thème est révélé : TRANSMISSION**
- nous avons alors **10 à 15min** pour imaginer un concept de jeu !
Avec l'équipe, nous aboutissons à une demi-douzaine d'idées, parmi lesquelles:
    * un "party game" de reconnaissance vocale pour téléphone mobile,
    où chaque participant doit prononcer les mots d'une phrase, chacun son tour, dans des langues étrangères
    * un jeu d'évaluation des distances où des personnages s'envoient des messages télépathiques
    * un "sokoban/minesweeper" en temps limité où le joueur incarne le personnage du démineur de Windows et progresse dans le niveau sans faire exploser de bombe
    * un "party game" TIC-TAC-BOUM ou 2 à 4 joueurs devant l'écran se renvoient une bombe
    * un jeu de déduction dans un graphe de relations inspiré du modèle Alice/Bob/César de cryptographie,
    où le joueur doit déterminer qui est l'espion après X tentatives de transmission de messages dans le réseau en sachant lesquelles ont été interceptées
    * un "puzzle-game" avec une balle suivant une trajectoire de folie en rebondissant sur des "tilt" de flipper

Une restitution des idées a alors lieux dans l'amphi, où chaque projet décrit brièvement son concept et exprime ses besoins de compétences (dev, graphiste, sound designer, etc.).
Comme nous avons une équipe mais pas encore de consensus entre nous sur une idée, nous séchons cette étape 😳

- **vendredi 21h** : l'équipe investit une petite salle de l'Epitech, après quelques parts de pizzas offertes par les oganisateurs.
Nous partons finalement sur une idée d'Henri (très prolifique en concepts !) de transmission de message dans une prison.
Nous nous répartissions brièvement les tâches pour la soirée, en partant d'un exemple utilisant le framework [PhaserJS](https://phaser.io)
afin d'essayer d'avoir un prototype au plus vite. Plusieurs dizaines de schémas et de dessins sont gribouillés et commentés.
Vu le concept sur lequel on est parti, ce serait génial d'utiliser les _sprites_ de [PrisonArchitect](http://store.steampowered.com/app/233450/Prison_Architect/) !
Comme c'est un jeu commercial, j'envoie un email [au graphiste qui les a réalisés](http://ryansumo.blogspot.fr) ainsi qu'à [l'éditeur du jeu](https://www.introversion.co.uk/introversion/#about).
Dans l'immédiat, nous décidons d'utiliser un ensemble de _spritesheets_ de [kenney.nl](https://kenney.nl).
- **vendredi dans la soirée** : Lucas Fleurance vient nous proposer de réaliser une bande son pour le jeu !
- **vendredi minuit et demi** : fin de la journée, on rentre se coucher
- **samedi vers 9h30** : nous nous retrouvons dans la salle pour continuer à coder.
Henri réalise le superbe écran d'intro
- **samedi 14h30** : toujours pas de prototype jouable !
Nous participons tout de même à un échange très sympa et motivant avec deux autres équipes participantes,
pour faire le point sur nos avancées et avoir quelques premiers retours.
- **samedi 19h** : alors que nous avons enfin un prototype jouable,
Chris Delay dIntroversion Software nous donne très aimablement l'autorisation par email d'utiliser les _sprites_ de Prison Architect pour notre jeu !
Il est malheureusement trop tard pour nous pour les utiliser 😞
- **samedi minuit** : au dodo pour moi et Loïc, Henri lui poursuit jusqu'au bout de la nuit 💤
- **dimanche 7h** : dernière ligne droite: on corrige quelques bugs;
on ajoute 2 niveaux et une page de crédits; on intègre la musique et les bruitages;
on réussit à intégrer une fonctionnalité dans la dernière heure (le "Hurry Up!");
on prend en compte les retours des testeurs en essayant d'expliquer mieux les mécaniques de jeu dans le premier niveau :

![Premier niveau du jeu](images/2018/01/GGJ2018_lvl_1.png)

- **dimanche 15h** : nous soumettons le jeu en ligne sur [le site de la GGJ](https://globalgamejam.org/2018/games/king-must-know), qui a du mal à tenir la charge.
Après avoir pris le temps de faire le tour des projets des autres équipes et tester plusieurs jeux,
c'est la fin de la jam pour nous. Bien fatigués, on rentre se reposer !

En définitive, c'était une belle aventure !

Je crois pouvoir dire qu'on a tous les trois bien apprécié l'expérience.
Et personnellement je n'ai vraiment pas vu le week-end passer.

Pour les curieux, tout le code source du jeu est disponible sur GitHub: <https://github.com/Lucas-C/OuiJam2018>

Dimanche, après avoir mis en ligne le jeu, nous avons fait un rapide "post-mortem" ensemble.
Voici ce qui ressortait de notre état d'esprit à la fin:

- envie d'en refaire une ! (mais pas tout de suite 💤)
- plutôt content du gameplay final pour un jeu en 48h
- content de l'avoir fait "sans se presser", et sans trop d'ambition,
et de ne pas s'être usé les nerfs les uns les autres
- ravis du résultat en termes de musique et de sons
- content du lieu où s'est déroulé la jam, de l'orga et de la bonne ambiance entre équipes
- plutôt satisfaits de l'adéquation du jeu au thème

Nous avons aussi listé les obstacles qui nous ont cassé les pieds durant cette jam:

- perdre du temps sur des "git merge" suite à des changements d'indentation automatique car nos IDEs étaient configurés différemment 😬
- un bug de Phaser JS sur le chargement des _spritesheets_
([rapporté](https://github.com/photonstorm/phaser-ce/issues/448) depuis et en cours de correction)
- retrouver la position des sprites que l'on voulait utiliser dans les grandes _spritesheets_ → très laborieux
- perdre du temps sur la gestion de la caméra, de la grille de _sprites_ et de leur mise à l'échelle à l'écran

Les trucs auxquels penser la prochaine fois:

- prévoir d'utiliser une éditeur de "tilemaps" comme Tiled, compatible avec Phaser JS, pour gagner du temps
- préparer un peu plus notre "template" de code de départ, en prévoyant comment structurer les entités Phaser JS,
et en configurant un "linter" ES6

Fonctionnalités qu'on aurait aimé ajouter:

- faire se déplacer les prisonniers dans une cellule quand ils le peuvent (et en termes de code, détecter automatiquement les `exits`)
- faire se déplacer les gardes, et indiquer leur ligne de vue en changeant la couleur du sol des cellules
- mieux gérer le niveau de zoom et le déplacement de la caméra
- ajouter des items : WCs, cuiller, revolver...
- ajouter un chargement de niveaux au format JSON/Tiled
- utiliser un générateur aléatoire basé sur une _seed_ exportable & importable

Enfin, au-delà du moteur de jeu, [Phaser JS](http://phaser.io), et des [assets libres de droit](https://github.com/Lucas-C/OuiJam2018#external-resources),
voici les principaux outils que nous avons utilisé:

- [IntelliJ IDEA](https://www.jetbrains.com/idea/)
- [Gimp](https://www.gimp.org/fr/)
- [Framateam](https://framateam.org)
- `git`, GitHub et [GitHub pages](https://pages.github.com) pour héberger une version en ligne

Pour conclure, merci encore aux organisateurs de cette fantastique jam !

Je vous encourage à jeter un œil à tous les jeux créés ce week-end là à [Nantes](https://globalgamejam.org/2018/jam-sites/epitech-nantes),
ainsi que partout ailleurs dans le monde !

Et pour tester le notre en ligne, [cliquez ici](https://lucas-c.github.io/OuiJam2018/build/).

On aimerait beaucoup vos avis / suggestions dessus, donc laissez nous un commentaire si vous le testez !

<style>
article img {
    display: block;
    margin: 0 auto;
    max-height: 30rem;
}
article figcaption {
    text-align: center;
}
</style>
