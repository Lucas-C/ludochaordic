Title: Crafting nonograms that reveal QR codes
Date: 2022-05-01 21:30
Lang: en
Tags: lang:en, libre-software, open-source, javascript, nonogram, logic-puzzle, enigme, print-play, gratuit, jeux, prog
---

Today I made a small addition to a Javascript library I sometimes use to generate [nonograms](https://en.wikipedia.org/wiki/Nonogram).

This tool can now build a solvable grid in the form of a valid [QR Code](https://en.wikipedia.org/wiki/QR_code) that, once decoded, reveals some text:

![Animation of a nonogram grid being solved and revealing a QR code](images/2022/05/qrcode.gif)

The nonogram size will depend on the hidden text size,
but even with a short text, it will be a difficult one to solve manually.

To find more about it: [Nonogram JS demo page](https://lucas-c.github.io/Nonogram/#qrcode-nonogram).

Note that I've written about open-source generators to build pen & paper puzzles in the past (in French):

* [Générateurs de puzzles open source (2018)](https://linuxfr.org/news/generateurs-de-puzzles-libres)
* [Nonograms, Topolokus et compagnie (2020)](nonograms-topolokus-et-compagnie.html)
