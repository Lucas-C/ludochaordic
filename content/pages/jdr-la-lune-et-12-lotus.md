Title: Campagne de JdR La Lune et 12 Lotus
Tags: lang:fr, jdr, la-lune-et-12-lotus, jeux, @Aurelien, @Elliot
Status: hidden
---

![Carte de l'univers](images/lle12l/LLDL-MapNB.jpg)

* [Page officielle du site du Grümph](http://legrumph.org/Terrier/public/chibi/lledl)
* [Page du GROG](https://www.legrog.org/jeux/lune-et-douze-lotus/lune-et-douze-lotus-fr)

# Session 1 - mars 2022

Lieu : désert entre le Sarmath et l'Erebe, au nord des Montagnes Blanches

Villes : Glassice (départ) - Aldap (étape) - Tomer (arrivée)

PJs :
* Matan (sabathéen) : ancien pécheur de baleine devenu pirate après qu'on lui ait promis la gloire
  PV: 15 - Réputation: 1 - Témérité: 9 -2 protection = CA 7
* Lushan (siamois) : ancien maître d'arme, exilé volontaire en quête de rédemption
  PV: 13 - Réputation: 1 -Témérité: 7 -3 protection = CA 4

PNJs encontrés :
* Ramal : chef d'escorte mercenaire
* Alès : mercenaire sabathéen rencontré à Glassice
* Hephia : marchand revendeur d’orfèvrerie en bronze

<!--
Scénarios :
* p6. Or de tout doute [mixé avec] p17. De l'eau pour les braves [ainsi que] p49. L’auberge rousse
* p8. La confusion des sentiments
* p23. Une putain de bonne nuit ! -> improviser un système pour la récupération des souvenirs, dans le désordre
* p30. Survivre et se venger -> en remplaçant les Grostesques par autre chose... mais la structure est bonne !
* p32. Les villages du damné (les PJs doivent être des quasi-paladins pour prendre ce risque !)
* p51. Du shamar à l’Erebe
* https://surlepouce.dragounet.com/scenarios/la-lune-et-12-lotus

Bande son ? https://tabletopaudio.com/dungeon_sp.html / https://www.youtube.com/watch?v=5DZu8TB6kbE
Scénarios inspirés d'Olija ? https://www.instagram.com/p/CVlOIBxFWKS/
* harpon légendaire : https://halfglassgaming.com/wp-content/uploads/2021/01/olija-relic.jpg / https://www.instagram.com/p/CKe3KRQj2-Y/
* moonblade
* Faraday : https://www.instagram.com/p/CLR5FM8DBGD/
* Terraphage / Rade-Marée = Oaktide
* clan Noirsaule = Rottenwood / Yellow cloak (twisted god with a single eye)
* character design: https://twitter.com/skeletoncrewen/status/1085090717955846146


## One page dungeons
* The sky-blind spire (wizard tower with a puzzle): http://blog.trilemma.com/2016/04/the-sky-blind-spire.html
* Basilica of the Leper Messiah: http://blog.trilemma.com/2017/09/basilica-of-leper-messiah.html
* The call of the light: http://blog.trilemma.com/2016/12/the-call-of-light.html
* Worrying volcano that received offers: https://cmartins.itch.io/melting-pot (OPDC 2022)
* Temple of the Moon Priests (OPDC 2017 winner): http://beholderpie.blogspot.com/2017/04/one-page-dungeon-2017-temple-of-moon.html
* A Stolen Song by P. Aaron Potter (OPDC 2015 winner)
-->

<style>
@font-face {
  font-family: Kirsty;
  src: url('images/bitd/fonts/kirsty.otf') format('opentype');
}
h1, h2, h3, h4 { font-family: Kirsty; }
h1 { text-align: center; }
article img, article video, article iframe {
  max-height: 80vh;
  display: block;
  margin: 0 auto;
}
article figcaption { text-align: center; }
.side-by-side {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: wrap;
}
.side-by-side > * { flex: 1 0; padding: 0 .5rem; }
.side-by-side > figcaption { min-width: 100%; }
/* headless tables */
article table { border-spacing: 0; border-collapse: collapse; page-break-inside: avoid; margin: 0 auto; }
article td, article th { font-weight: normal; padding: 5px 10px; text-align: left; }
article td { border-top: 1px solid #ddd; }
article tr > td:first-child, article tr > th:first-child { font-weight: bold; text-align: right; }
</style>
<script>
const ANCHOR_ID_CHAR_RANGE_TO_IGNORE = '[\x00-\x2F\x3A-\x40\x5B-\x60\x7B-\uFFFF]+';
function slugify(s) {
  var s = String(s)
  s = s.trim()
  s = s.toLowerCase()
  s = s.replace(new RegExp('^'+ANCHOR_ID_CHAR_RANGE_TO_IGNORE, 'g'), '')
  s = s.replace(new RegExp(ANCHOR_ID_CHAR_RANGE_TO_IGNORE, 'g'), '-')
  return encodeURIComponent(s);
}
function buildId(s) {
  let slug = slugify(s)
  let newId = slug
  let suffixInt = 1
  while (document.getElementById(newId)) {
    newId = slug + '-' + (++suffixInt)
  }
  return newId
}
['h2', 'h3', 'h4'].forEach(function (selector) {
    document.querySelectorAll(selector).forEach(function (title) {
        if (!title.id) { title.id = buildId(title.textContent); }
        var a = document.createElement('a');
        a.href = document.location + '#' + title.id;
        a['aria-hidden'] = true;
        a.style.float = 'left';
        a.style['padding-right'] = '4px';
        a.style['margin-left'] = '-20px';
        a.style['line-height'] = 1;
        title.appendChild(a);
        var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        svg.setAttribute('aria-hidden', true);
        svg.setAttribute('height', 16);
        svg.setAttribute('width', 16);
        svg.setAttribute('viewBox', '0 0 16 16');
        svg.style.color = '#1b1f23';
        svg.style['vertical-align'] = 'middle';
        svg.style.visibility = 'hidden';
        a.appendChild(svg);
        var path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttributeNS(null, 'fill-rule', 'evenodd');
        path.setAttributeNS(null, 'd', 'M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z');
        svg.appendChild(path);
        title.onmouseover = function () { this.getElementsByTagName('svg')[0].style.visibility = 'visible'; };
        title.onmouseout = function () { this.getElementsByTagName('svg')[0].style.visibility = 'hidden'; };
    });
});
</script>
