Title: Animated one-page-dungeon : Escape of the Torment
Date: 2022-12-02 12:50
Lang: en
Tags: lang:en, jdr, gratuit, aide-de-jeu, one-page-dungeon, blades-in-the-dark, jeux, python, source-code, libre-software, open-source, pdf, libre-office, prog
---

Last week, while translating John Harper's micro-TTRPG [World of Dungeons: Turbo Breakers](world-of-dungeons-turbo-breakers.html), I discovered the wonderful world of **one page dungeons**,
starting with Michael Prescott splendid production at [trilemma.com](http://blog.trilemma.com/p/aventures-en-francais.html)
and also the yearly [One Page Dungeon Context](https://www.dungeoncontest.com/).

While crawling through the OPDC 2021 entries, I discovered a great map by [Brett Simison](https://mooselich.com/): _Escape of the Torment_.
With my experience on building "animated" PDFs (on [Undying Dusk](undying-dusk-a-pdf-video-game.html) and another game I'm currently working on), I thought it would be fun to "animate" this great adventure, and here is the result:

<div class="side-by-side">
  <a href="images/2022/11/EscapeOfTheTorment-animated.pdf">
    <figure>
      <img alt="PDF thumbnail preview" src="images/2022/11/EscapeOfTheTorment-animated.gif">
      <figcaption>PDF (146 pages - 6.76 MB)</figcaption>
    </figure>
  </a>
  <a href="images/2022/11/EscapeOfTheTorment-PythonCodeAndAssets.zip">
    <figure>
      <img alt="ZIP archive thumbnail" src="images/2022/11/EscapeOfTheTorment-zip-thumbnail.jpg">
      <figcaption>ZIP archive of the Python source code &amp; assets (7.73 MB)</figcaption>
    </figure>
  </a>
</div>

> The goal of this "animated" PDF is to provide the GM with a simple PDF document displaying a map,
> so that they can show it in full screen to the players during the game session,
> and click on elements of the map in order for the scene to evolve.

I initially though about building this with HTML, CSS & Javascript as a web page,
but on second though it thought that generating a single PDF could be more handy for GMs,
with the added benefit of not requiring an online connexion. It was also a bit simpler for me not to worry with being adaptive to the browser screen size.

In order to extract the images from the original PDF, I used [LibreOffice Draw](https://libreoffice.org/discover/draw/)
with a custom Python script, included in the ZIP archive.
The archive also includes the `build_animated_EotT.py` program used to generate the animated PDF, using [fpdf2](https://pyfpdf.github.io/fpdf2/).

I hope the PDF will be useful to some GMs. I think it would be a good fit for a D & D or [7th Sea](https://en.wikipedia.org/wiki/7th_Sea_(role-playing_game)) adventure. I personnally plan to use it in my [Blades in the Dark](https://bladesinthedark.com) campaign.

The overall approach of animating TTRPG sceneries / battlegrounds as PDF documents could also be applied to other maps!
Of course it does not offer as much expressivity as a Roll20 / Foundry interactive map,
but it can be a handy, simple alternative, and very fun to build for Python coders! 🐍

<style>
@media (min-width:768px) {
  .side-by-side {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .side-by-side > * { margin: 0 2rem; }
}
</style>

<!-- Com'
* [x] email to dm@mooselich.com
* [x] https://www.casusno.fr/viewtopic.php?t=41384
* [x] Reddit:
    + https://www.reddit.com/r/onePageDungeon/comments/zakoa1/animated_onepagedungeon_escape_of_the_torment/
    + https://www.reddit.com/r/osr/comments/zakr9b/i_made_an_animated_pdf_out_of_brett_simison/
    + https://www.reddit.com/r/battlemaps/comments/zasgjs/i_made_an_animated_pdf_out_of_brett_simison/
-->
