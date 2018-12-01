Title: Générateurs de puzzles open source
Date: 2018-05-06 08:00
Tags: lang:fr, python, javascript, linuxfr, open-source, puzzle, gratuit, jeux, prog
Slug: generateurs-de-puzzles-open-source
Image: images/2018/05/nonogram.gif
---

Voici une petite dépêche que j'ai écrite sur le site LinuxFr :
<https://linuxfr.org/news/generateurs-de-puzzles-libres>

<!--
Il y a quelques temps, j'étais à la recherche de générateurs de puzzles personnalisables (dont la solution serait un petit mot doux romantique). Des puzzles qui ne soient pas uniquement jouables en ligne, mais imprimables, ne nécessitant qu'une feuille et un crayon.

Au final j'ai découvert de nombreux programmes open source permettant de générer des mots croisés, des grilles de mot mystère, des nonogrammes, etc.

Je vais donc dans cette dépêche vous présenter ces projets, en espérant qu'ils vous inspirent à concocter vos propres puzzles pour vos enfants / neveux, compagnon / compagne ou encore grand parents !


# Mots croisés #

Je n'ai testé qu'un seul programme, en Python, de David Whitlock (riverrun) : [genxword](https://github.com/riverrun/genxword)

Voici un exemple de grille qui peut être générées :

![Exemple de grille avec indices sur le thème des Monty Python](https://raw.githubusercontent.com/riverrun/genxword/master/examples/output/Pdf_grid_example.png)

Pour fonctionner le programme nécessite qu'on lui fournisse une liste de mots, qui sont donc entièrement personnalisables. Chaque mot de la liste peut être associé à une définition.

`genxword` peut générer des grilles sous forme de PDFs, de PNGs ou de SVGs.
Il est compatible Python 2 & 3, est basé sur GTK mais fonctionne sous Windows (j'ai testé) et est sous license GNU v3.


# Nonogrammes #

Également appelés ["picross", "griddlers" an anglais ou encore "hanjie" au Japon](https://fr.wikipedia.org/wiki/Picross), ces puzzles sont parmis mes préférés.

J'ai essayé plusieurs programmes pour générer ce type de puzzle, mais mon préféré de loin est celui de Zhou Qi (HandsomeOne) en Javascript : https://github.com/HandsomeOne/Nonogram

![Nonogram par Zhou Qi](http://i.imgur.com/XRs3jk7.gif)

Il inclut une grille cliquable pour y jouer, un éditeur interactif pour confectionner vos propres grilles et même un solveur avec rendu visuel des étapes pas à pas, permettant de valider que la grille a une solution !

Le code est structuré et lisibile facilement, sans dépendances et sous license MIT.

Comme au final un nonogramme n'est qu'une image pixelisée en noir & blanc, j'ai fait un [_fork_](https://github.com/Lucas-C/Nonogram/) du projet pour simplement rajouter 2 boutons permettant d'importer ou exporter [des grilles au format PNG](https://github.com/Lucas-C/Nonogram/tree/master/grids): https://lucas-c.github.io/Nonogram/ (dans la section "Create Your Own Nonogram")


# Mot mystère

Aussi appelé ["mots cachés"](https://fr.wikipedia.org/wiki/Mots_cach%C3%A9s),
ce puzzle est idéal pour camoufler un message secret dans une grille, afin qu'il soit reconstitué une fois résolu !

Bill Scheidel (bunkat) a créé en Javascript [une grille jouable en ligne, avec éditeur intégré](https://github.com/bunkat/wordfind) : https://lucas-c.github.io/wordfind/

![Capture d'écran de wordfind.js](https://chezsoi.org/lucas/wordfind.png)

Vous pouvez y lister les mots à cacher dans la gille, votre mot secret, l'extension maximum de la grille ou encore le nombre de mots qui peuvent être "ignorés" parmi ceux fournis afin que le générateur produise une grille compacte.

Bref, c'est un programme simple d'utilisation, sans dépendance et sous license MIT.


# Sudoku

Je ne l'ai que très peu testé, mais voici un générateur de Sudoku écrit par Rob McGuire (robatron) en Javascript : https://github.com/robatron/sudoku.js

![Capture d'écran de Sudoku.js](https://chezsoi.org/lucas/SudokuJS.png)

Utilisant jQuery et la bibliothèque Bootstrap, ce projet est sous License MIT et vous permettra de générer vos propres grilles.

Pour ceux qui préfèrent d'autres langage que le Javascript, sachez que comme le Sudoku est un puzzle très populaire, vous trouverez de nombreux générateurs et versions jouables sur Github en Python, Ruby, etc.


# Et plein d'autres puzzles originaux !

Pour conclure, je voudrais mentionner la collection de puzzles de Simon Tatham, sous license MIT et disponibles en Java ou Javascript, qui est à la fois immense et regorge de puzzles originaux :
https://www.chiark.greenend.org.uk/~sgtatham/puzzles/

![La collection de puzzle de Simon Tatham](https://chezsoi.org/lucas/SimonTathamPuzzleCollection.png)

-->
