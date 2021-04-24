Title: Undying Dusk : a PDF video game
Date: 2021-04-24 17:00
Tags: lang:en, lang:fr, libre-software, open-source, pdf, video-game, dungeon-crawler, rpg, indie-game, python, library, gratuit, creative-commons, gpl, gamedesign, post-mortem, recreative-programming, prog, cyberconv, jeux
Slug: undying-dusk-a-pdf-video-game
---
![UNDYING DUSK](images/2020/10/undying-dusk-title.png)

**Undying Dusk** is a video game in a PDF format,
with a gameplay based on exploration and logic puzzles,
in the tradition of [dungeon crawlers](https://en.wikipedia.org/wiki/Dungeon_crawl#Video_games).

> A curse set by the Empress keeps the world in an eternal dusk.
> You are have recently found shelter in an eerie monastery.

![GIF trailer #1](https://raw.githubusercontent.com/Lucas-C/undying-dusk/main/trailer/undying-dusk-trailer1.gif)

Featuring:

- ~ 200 000 PDF pages
- retro aesthetics: 160x120 resolution & a 16 colors palette
- a grid-based world with 50+ distinct tiles & 10 maps to explore
- more than 30 treasure items, weapons & spells to pick up in order to face 15 enemy monsters
- 20 music tracks
- thousands of "Game Over" pages, and a single path to victory
- 4 hidden secrets & a concealed epilogue
- an online [hall of fame](https://chezsoi.org/lucas/undying-dusk/hall-of-fame)

To my knowledge, this is **the very first video game in a PDF format**.

Download it on the [**dedicated itch.io page**](https://lucas-c.itch.io/undying-dusk").

![GIF trailer #2](https://raw.githubusercontent.com/Lucas-C/undying-dusk/main/trailer/undying-dusk-trailer2.gif)


<!-- com' :
- [x] itch.io
- [x] blog
- [ ] author: Clint Bellanger
- [ ] amis, dont Francis, Aurélien, Anne-Laure...
- [ ] oujevipo, warpdoor, gamejolt & cie
- [ ] forum.canardpc.com
- [ ] subReddits: r/pdf, r/gaming, r/games, r/gamedev, r/IndieGaming, r/IndieDev, r/playmygame, r/freegames, /r/adventuregames, r/PixelArt
- [ ] Sumatra PDF
- [ ] famille Cesbron, Thomas G & ses potes
- [ ] bruno bord
- [ ] collègues, Michael Bourhis, Martin & son frère, Maxence, Thomas G, Fabrice Descombes -> https://www.filfre.net/2015/12/dungeon-master-part-1-the-making-of/
- [ ] thierry.fetiveau@gmail.com
- [ ] https://www.coupleofgamer.com/about
- [ ] envoyer version PDF à Thib pour tester sur smartphone + msg HackerNews
- [ ] LinkedIn, FaceBook
- [ ] https://adventuregamers.com
- [ ] http://hu-mu.blogspot.com en mode HUMBLE
- [ ] post GIF trailer on Youtube
post write-up:
- [ ] subReddits: r/python, r/programming
- [ ] linux fr ?
- [ ] collègues, dont Michaël Bouris & son beauf fan de JV/jdr
- [ ] Emily F & other Irish people

Idées de format de com' originales et peu coûteuses à réaliser :
* animated GIF that initially just looks like static text

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

Difficulties to terminate the game (especially to rework stuff like the last boss fight)

Metadata addition with pikepdf that took 1h15 :(

# Storywriting
Books : really useful

Adventure game puzzle design -> readings

1st OGA contrib & Pedro Medeiros tutorials

~XK lines of Python code in Y files

ajouts / changements comparé à l'original à mentionner:
- monsters do NOT appear randomly, but in a predefined way
- there is no sleeping, that restore HP & MP + create "save points"
- monster arrival animations are missing
* moins de gold farming / backtracking
* use content hidden in original sources: 2 monsters & extra equipment (swords & armor)
-->

