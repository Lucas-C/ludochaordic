Title: Translate PICO-8 games with pico8-l10n
Date: 2026-01-13
Lang: en
Tags: lang:en, indie-game, video-game, Lua, personal-project, traduction, l10n, open-source, gratuit, prog, jeux
Image: images/2026/01/pico8-l10n-website-screenshot.png
---

<center>_Note: cet article est en anglais, mais j'ai traduit les jeux mentionnés en **français**._</center>

Recently, thanks to a game recommendation from [Bart Bonte](https://www.bontegames.com/), I discovered several wonderful video games from [Adam "Atomic" Saltsman](https://en.wikipedia.org/wiki/Adam_Saltsman).
I shared them on my Shaarli there: [chezsoi.org/shaarli/?searchtags=AdamAtomicSaltsman](https://chezsoi.org/shaarli/?searchtags=AdamAtomicSaltsman).

The games are all very short, but also very well designed.
I had so much fun! ❤️

Then I realized that:

1. all those games are [PICO-8](https://www.lexaloffle.com/pico-8.php) games: it's a fantasy console for making, sharing and playing tiny games and other computer programs
2. on Reddit I discovered that some generic consols allow to play PICO-8 games, like the [ANBERNIC RG CubeXX](https://anbernic.com/products/rg-cubexx)

Because I'm French, and many young kids around me do not read English,
I wanted to **translate those PICO-8 games**!

After quickly checking [on PICO-8 BBS forum](https://www.lexaloffle.com/bbs/?tid=154035),
I found out there was currently no solution to translate PICO-8 games...

So that became a very fun personal project I made last week,
programming this in **Lua** : [`pico8-l10n`](https://github.com/Lucas-C/pico8-l10n).

I even made a dedicated web page:
[lucas-c.github.io/pico8-l10n](https://lucas-c.github.io/pico8-l10n/)

![](images/2026/01/pico8-l10n-website-screenshot.png)

It was also very fun to code this!

I learned Lua programming 15 years ago, but never really had the chance to use this language in a useful project.

It become a good opportunity to learn & setup many useful tools when working with Lua code:
[![Luacheck status](https://github.com/Lucas-C/pico8-l10n/workflows/Luacheck/badge.svg)](https://github.com/lunarmodules/luacheck#luacheck)
[![Busted status](https://github.com/Lucas-C/pico8-l10n/workflows/Busted/badge.svg)](https://lunarmodules.github.io/busted/)

I even released my very first LuaRocks package:
[![LuaRocks](https://img.shields.io/luarocks/v/Lucas-C/pico8-l10n)](https://luarocks.org/modules/lucas-c/pico8-l10n)

Finally, it was a good opportunity to setup something I wanted to try for a long time:
CLI application unit tests, using [Prysk](https://github.com/prysk/prysk#prysk):
[![Prysk status](https://github.com/Lucas-C/pico8-l10n/workflows/Prysk/badge.svg)](https://github.com/prysk/prysk#prysk)

It was also very fun to translate games.
I already did that in the past with
[the video game translation of "The Temple of No" (blog article)](traduction-du-temple-du-non-une-histoire-interactive-twine-du-studio-crows-crows-crows.html).
What is a bit trick with PICO-8 games is that sometimes the layout where the text appears is very constrained,
and French being a language more verbose than English,
it is sometimes difficult to fit translation in a limited space on screen!

Finally, I designed `pico8-l10n` to make it easy to share new `PICO-8` game translations,
so go on an contribute a PR if you want to translate your favorite game! 😊

<!-- Com'
* ping Kevin
* linuxfr
-->
