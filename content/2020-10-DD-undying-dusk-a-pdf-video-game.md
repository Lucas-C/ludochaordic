Title: Undying Dusk : a PDF video game
Date: 2020-10-07 18:0
Tags: lang:en, lang:fr, libre-software, open-source, pdf, video-game, dungeon-crawler, rpg, indie-game, python, library, gratuit, creative-commons, gpl, gamedesign, post-mortem, recreative-programming, prog, jeux
Slug: undying-dusk-a-pdf-video-game
Status: draft
---
<!-- à partager sur :
- [ ] author: Clint Bellanger
- [ ] oujevipo, warpdoor & cie
- [ ] forum.canardpc.com
- [ ] subReddits: r/pdf, r/gaming, r/games, r/gamedev, r/IndieGaming, r/IndieDev, r/playmygame, r/freegames
- [ ] Sumatra PDF
- [ ] famille Cesbron, Thomas G & ses potes
- [ ] bruno bord
- [ ] Michael Bourhis, Fabrice Descombes -> https://www.filfre.net/2015/12/dungeon-master-part-1-the-making-of/
- [ ] thierry.fetiveau@gmail.com
- [ ] envoyer version PDF à Thib pour tester sur smartphone + msg HackerNews
- [ ] LinkedIn
- [ ] https://adventuregamers.com
- [ ] http://hu-mu.blogspot.com en mode HUMBLE
post write-up:
- [ ] subReddits: r/python, r/programming
- [ ] linux fr ?
- [ ] collègues, dont Michaël Bouris & son beauf fan de JV/jdr
- [ ] Emily F & other Irish people
-->

![UNDYING DUSK](images/2020/10/undying-dusk-title.png)

**Undying Dusk** is a video game in a PDF format,
with a gameplay based on exploration and logic puzzles,
in the tradition of [dungeon crawlers](https://en.wikipedia.org/wiki/Dungeon_crawl#Video_games).

The game is set in a fantasy realm where a curse set by the Empress keeps the world in an eternal dusk.
You play a woman who recently found shelter in an eerie monastery.

It features:

- ~150 000 PDF pages
- a retrogaming aesthetic: 160x120 pixels resolution and a 16 colors palette
- a grid-based world with 36 different tiles and 10 maps to explore
- 30+ treasure items, weapons & spells to pick up in order to face 17 enemy monsters
- 21 music tracks
- 17530 "Game Over" pages, and a single path to victory
- 4 hidden secrets & a hidden ending

It was made during the summer of 2020 by Lucas Cimon.

To my knowledge, this is **the very first video game in a PDF format**.

<a src="https://chezsoi.org/lucas/undying-dusk/undying-dusk-v0.9.0.pdf" target="_blank">
  <figure>
    <img alt="" src="images/2020/10/pdf-icon.png">
    <figcaption>(PDF 150Mo)</figcaption>
  </figure>
</a>

<!-- Autres idées:
_Le crépuscule de l'héroïne_
+ combats, non euclidean maze, highscores...
+ GIF
+ use Boxy-Bold.ttf

mention FLOSS & GitHub link
~3K lines of Python code in 27 files

donation: itch.io

ajouts / changements comparé à l'original à mentionner:
- monsters do NOT appear randomly, but in a predefined way
- there is no sleeping, that restore HP & MP + create "save points"
- monster arrival animations are missing
* moins de gold farming / backtracking
* use content hidden in original sources: 2 monsters & extra equipment (swords & armor)

<!--
## 2nd technical write-up post:

**Concept**: build a PDF that could be played as a video game
Inspiration: [Table Ronde n°1 de la CyberConv 2020](http://www.cyberconv1.com/#programme).
Then I thought: what could be emulated with an interactive PDF? A maze game!

Other video game inspirations: Dungeon Master, Eye of the Beholder, Legend of Grimrock, Moonshades...

mécanisme d'itérations des états & level design progressif avec contrainte (single path)
avec checkpoints
-> le programme assure de l'existence d'une unique solution

graphics:
- Gimp & xcf
- palette DawnBringer

pyfpdf

PDF Checker in CI

accessibility...

optims
- comment gen_pdf.py output of resourrces vs pages size

trucs que j'ai appris :
* le format PDF c'est pas si pire, mais dur de trouver des exemples de PDF valides pour chaque feature...
* PDF readers aren't very fast at rendering basic stuff (comparo ?)

https://xcvgsystems.com/static/adventure/

use ascii map screenshot

### gamedesign

no more than 4 rounds of combat

initial feedbacks: minimap needed, + combat tutorial, give backspace hint faster

puzzles that did not go well...
- goblin hord
- sokoban
- CTRL+F

# Storywriting
Books : really useful
-->