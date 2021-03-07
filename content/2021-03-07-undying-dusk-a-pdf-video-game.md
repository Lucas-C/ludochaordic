Title: Undying Dusk : a PDF video game
Date: 2021-03-07 13:00
Tags: lang:en, lang:fr, libre-software, open-source, pdf, video-game, dungeon-crawler, rpg, indie-game, python, library, gratuit, creative-commons, gpl, gamedesign, post-mortem, recreative-programming, prog, cyberconv, jeux
Slug: undying-dusk-a-pdf-video-game
Status: draft
---
<!-- à partager sur :
- [ ] author: Clint Bellanger
- [ ] itch.io
- [ ] amis, dont Francis, Aurélien, Anne-Laure...
- [ ] oujevipo, warpdoor, gamejolt & cie
- [ ] forum.canardpc.com
- [ ] subReddits: r/pdf, r/gaming, r/games, r/gamedev, r/IndieGaming, r/IndieDev, r/playmygame, r/freegames, /r/adventuregames, r/PixelArt
- [ ] Sumatra PDF
- [ ] famille Cesbron, Thomas G & ses potes
- [ ] bruno bord
- [ ] collègues, Michael Bourhis, Martin & son frère, Fabrice Descombes -> https://www.filfre.net/2015/12/dungeon-master-part-1-the-making-of/
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
-->

![UNDYING DUSK](images/2020/10/undying-dusk-title.png)

**Undying Dusk** is a video game in a PDF format,
with a gameplay based on exploration and logic puzzles,
in the tradition of [dungeon crawlers](https://en.wikipedia.org/wiki/Dungeon_crawl#Video_games).

The game is set in a fantasy realm where a curse set by the Empress keeps the world in an eternal dusk.
You play a woman who recently found shelter in an eerie monastery.

It features:

- 200 000 PDF pages
- a retrogaming aesthetic: 160x120 pixels resolution and a 16 colors palette
- a grid-based world with 50 different tiles and 10 maps to explore
- more than 30 treasure items, weapons & spells to pick up in order to face 15 enemy monsters
- 20 music tracks
- thousands of "Game Over" pages, and a single path to victory
- 4 hidden secrets & a concealed epilogue
- an online [hall of fame](https://chezsoi.org/lucas/undying-dusk/hall-of-fame)

It was made during the summer of 2020 by Lucas Cimon.

To my knowledge, this is **the very first video game in a PDF format**.

<div class="side-by-side">
  <a href="https://github.com/Lucas-C/undying-dusk/releases/download/v0.9.6/undying-dusk.pdf" download>
    <figure>
      <img alt="" src="images/2020/10/pdf-icon.png">
      <figcaption>v0.9.6 - 7 mars 2021<br>(PDF 272 Mo)</figcaption>
    </figure>
  </a>
  <a href="https://github.com/Lucas-C/undying-dusk/releases/download/v0.9.6/undying-dusk-with-sumatra-windows.zip" download>
    <figure>
      <img alt="" src="images/2020/11/zip-icon.jpg">
      <figcaption>v0.9.6 - 7 mars 2021 2020<br>(ZIP 109 Mo)</figcaption>
    </figure>
  </a>
</div>

Note that **it cannot be played using Adobe Acrobat Reader**, due to technical limitations of this software.

I recommend that you use instead **Sumatra PDF reader**.

If you do not wish to install it on your computer, you can use it only to launch **Undying Dusk** by downloading the ZIP file. Once the ZIP content is extracted in a folder, simply double-click on the `LAUNCH_UNDYING_DUSK_IN_SUMATRA.bat` file to start the game.

You will find more informations, including a detailed comparison of PDF readers compatibility with the game, [on GitHub](https://github.com/Lucas-C/undying-dusk).

Here is the game trailer:

![GIF trailer](https://raw.githubusercontent.com/Lucas-C/undying-dusk/main/trailer/undying-dusk-trailer.gif)


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

Difficulties to terminate the game (especially to rework stuff like the last boss fight)

Metadata addition with pikepdf that took 1h15 :(

# Storywriting
Books : really useful

Adventure game puzzle design -> readings

1st OGA contrib & Pedro Medeiros tutorials
-->

<style>
.side-by-side {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: wrap;
}
.side-by-side > * { flex: 1 0; padding: 0 .5rem; }
.side-by-side img { max-height: 12rem; }
</style>
