Title: Open-Source
Tags: lang:en, cygwin, hesperides, isso, jenkins, luigi, open-source, pre-commit, python, pelican, shaarli
---

## Pet projects, musings

### For tabletop RPGs
- [shared-img-reveal](https://github.com/Lucas-C/shared-img-reveal) : a minimal web application to share an image with your players, like a map, and progressively reveal it
- [rpg-bonhomme](https://github.com/Lucas-C/rpg-bonhomme) : a tabletop RPG character sheet viewer, with a Python backend using a JSONP key-value store
- [rpg-dice](https://chezsoi.org/lucas/jdr/rpg-dice) : perform dice rolls on a web page shared among players

### Games

- [Undying Dusk](https://github.com/Lucas-C/undying-dusk) : **a video game in a PDF format**, with a gameplay based on exploration and logic puzzles, in the tradition of dungeon crawlers:

![Game trailer](https://raw.githubusercontent.com/Lucas-C/undying-dusk/main/trailer/undying-dusk-trailer.gif)

- [The King Must Know](https://github.com/Lucas-C/OuiJam2018) : a Phaser JS short video game made with 2 colleagues during the Global Game Jam 2018
- [tablut](https://github.com/Lucas-C/tablut/) : a PHP implementation of an old [Scandinavian](https://en.wikipedia.org/wiki/Tafl_games) duel board game for the online platform [BoardGameArena](https://boardgamearena.com), with [simple rules](http://en.doc.boardgamearena.com/Gamehelptablut)
- [MemoryGame.js](https://github.com/Lucas-C/MemoryGame.js) : a simple HTML+JS memory game, forked from Mark Rolich repo to add support for images

### Other
- [Python Black Box challenge](https://lucas-c.frama.io/python-blackbox-challenges/)
- [genealogic-d3](https://github.com/Lucas-C/genealogic-d3) : genealogy tree visualization using [d3.js](https://d3js.org)
- [youtube_playlist_watcher](https://github.com/Lucas-C/youtube_playlist_watcher) : backup Youtube playlists and alert you on songs deletions, written in Python
- [music-emails-spybot](https://github.com/Lucas-C/music-emails-spybot) : Python script generating an HTML archive page of all mentioned songs in emails retrieved from IMAP server (e.g. Gmail)
- [wisemapping-mindmap-viewer](https://github.com/Lucas-C/wisemapping-mindmap-viewer) : a simple HTML+JS mindmap viewer, fork of an original Java project,
with a companion [brain_dump](https://github.com/Lucas-C/brain_dump) repo containing tools to manipulate simple mindmaps described as indented Markdown
- [ecovoit](https://github.com/Lucas-C/ecovoit) : a web search engine for French carpooling offers _(deprecated)_
- [nose-summary-report](https://pypi.org/project/nose-summary-report/) : nose plugin that generates a final summary of tests status as a table
- [unicode-search](https://github.com/Lucas-C/unicode-search) : a NodeJS CLI program to search unicode characters by name

## Contributions
Some open-source projects to which I have contributed.

- <img alt="Logo Python" src="images/open-source/python-logo.png" style="max-width: 16em">
I made a few minor bug fixes to CPython: [GitHub PRs](https://github.com/python/cpython/pulls?utf8=%E2%9C%93&q=author%3ALucas-C)

- [<img alt="Logo pre-commit" src="images/open-source/pre-commit-logo.png" style="max-width: 6em"> pre-commit](http://pre-commit.com) :
Python command line manager for `git` pre-commit hooks
    * created [several hooks](https://github.com/Lucas-C?tab=repositories&q=pre-commit-hooks&type=source)
    * also made some bug fixes, improved support for Cygwin and added support for locally defined hooks

- [<img alt="Logo Shaarli" src="images/open-source/shaarli-logo.png" style="max-width: 6rem"> shaarli](https://github.com/shaarli/Shaarli) :
personal, minimalist, bookmarking service, in PHP
    * improved the search form ergonomy
    * added the ability to display subtags in the tag cloud
    * some bug fixes

- [<img alt="Logo Pelican" src="images/open-source/pelican-logo.png" style="max-width: 6rem"> Pelican](https://getpelican.com/) : a static site generator in Python
    * created [a plugin to send LinkBacks](https://github.com/pelican-plugins/linkbacks/)
    * and another [to insert thumbnails along image links](https://github.com/pelican-plugins/image-preview-thumbnailer)
    * and another [to publish articles on a Shaarli instance](https://github.com/getpelican/pelican-plugins/pull/1167)
    * and another [to generate CTags](https://github.com/getpelican/pelican-plugins/pull/1038)
    * designed [a 2-columns layout theme](https://github.com/Lucas-C/pelican-theme-timeline)
    * improved two other themes: [pelican-mg](https://github.com/Lucas-C/pelican-mg) & [html5-dopetrope](https://github.com/Lucas-C/html5-dopetrope)
    * fixed the [Travis CI pipeline for the pelican-plugins repository](https://github.com/getpelican/pelican-plugins/issues/1170)
    * [added support for the {include} syntax](https://github.com/getpelican/pelican/pull/2628)
    * fixed some minor things in [the core](https://github.com/getpelican/pelican/pulls?utf8=%E2%9C%93&q=is%3Apr+author%3ALucas-C+) & in [plugins](https://github.com/getpelican/pelican-plugins/pull/1035)

- [<img alt="Logo fpdf2" src="images/open-source/fpdf2-logo.png" style="max-width: 12rem"> fpdf2](https://github.com/PyFPDF/fpdf2) : minimalist PDF creation library for Python.
I have implemented [all new features from `v2.1.0` onwards](https://github.com/PyFPDF/fpdf2/blob/master/CHANGELOG.md).
_cf._ [related blog posts](tag/fpdf2.html).

- [<img alt="Logo isso" src="images/open-source/isso-logo.svg" style="max-width: 6rem"> isso](https://posativ.org/isso/) : several [small bugfixes & improvements](https://github.com/posativ/isso/pulls?q=author%3ALucas-C) to this great self-hosted commenting service using Markdown & SQLite

- [pylint](http://pylint.pycqa.org/en/latest/intro.html) : a Python code static analyzer, for which I added [a check for oversighted implicit string concatenations in sequences](https://github.com/PyCQA/pylint/pull/1655)

- [<img alt="Logo luigi" src="images/open-source/luigi-logo.png" style="max-width: 6rem">](https://github.com/spotify/luigi) :
a Python module to build batch pipelines, it handles dependency resolution, workflow management, visualization, etc.
    * added a new parameter type: `DateSecondParameter`
    * some bug fixes and exception messages improvements

- [Nonogram](https://github.com/Lucas-C/Nonogram) : added some features to this great picross / hanjie / logimage game / solver / editor in Javascript

- [pew](https://github.com/berdario/pew) : simplify Python virtual environments management, let use them in dedicated shell session
    * added support for [cmder](http://cmder.net) & Cygwin

- [MinigalNano](https://github.com/sebsauvage/MinigalNano) : a simple PHP image gallery
    * made a bunch of bug fixes, including the RSS feed

- [COVID-19 Le jeu](https://github.com/covid19lejeu/covid-19-le-jeu) : initialization of the repo, build tools & JS code for the web version of this educational _print & play_ board game, under a creative-commons license

I also made some maps for a Ludum Dare game, back in 2009 (the game is worth trying !):
<http://eriatic.wikidot.com/blog:triumph-mappack>


### Open-source contributions made at oui.sncf

When working at [oui.sncf](https://jobs.oui.sncf), I had the opportunity to work on the following open-source projects:

- [`Hesperides`](https://github.com/voyages-sncf-technologies/hesperides):
a configuration management tool providing universal text file templating and properties editing through a REST API or a webapp

<br>

I also created the following ones:

- [<img alt="Logo V.Board" src="images/open-source/logo-vboard.jpg" style="max-width: 6em"> `V.Board`](https://github.com/voyages-sncf-technologies/vboard) :
a "pins" dashboard to share news among an organization

- [<img alt="Logo hesperides-jenkins-lib" src="images/open-source/hesperides-jenkins-lib-logo.png" style="max-width: 6em"> `hesperides-jenkins-lib`](https://github.com/voyages-sncf-technologies/hesperides-jenkins-lib) :
a shared lib for Jenkins pipelines to interact with Hesperides, the in-house configuration management system

- [`nexus_uploader`](https://github.com/voyages-sncf-technologies/nexus_uploader) :
a Python tool to help with the development & deployment of company-private Python packages on a Sonatype Nexus


### Translation
- [translation from English to French](https://github.com/CrowsCrowsCrows/the-temple-of-no/pull/1) of the short, open-source, interactive story game
[The Temple of No](https://crowscrowscrows.itch.io/the-temple-of-no) by the [Crows Crows Crows](http://www.crowscrowscrows.com/) studio


<style>
.uk-article-content > ul > li {
    margin-bottom: 2rem;
}
</style>
