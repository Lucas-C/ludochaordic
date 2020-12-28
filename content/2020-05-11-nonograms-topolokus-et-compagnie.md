Title: Nonograms, Topolokus et compagnie
Date: 2020-05-11 21:45
Tags: lang:fr, personal-project, open-source, nonogram, topoloku, concept, enigme, javascript, logic-puzzle, print-play, gratuit, prog, maths, jeux
Slug: nonograms-topolokus-et-compagnie
Image: images/2020/05/topoloku.png
---
<!-- Partagé sur :
- http://www.bibmath.net/forums/viewtopic.php?id=12588
- http://www.prise2tete.fr/forum/viewtopic.php?id=13888
NEXT: translate & put it on https://www.reddit.com/r/puzzles ?
> If you are linking your own blog or puzzle game/app, please submit this as a comment in the stickied self promotion thread. Please either post a text version of your puzzle, or rehost the image through Reddit or Imgur. Links to blogs/apps should be kept to the self promotion thread.
-->

<link rel="stylesheet" type="text/css" href="images/enigmes/topoloku.css">

Depuis le 24 mars, avec ma compagne, nous avons décidé de partager un petit puzzle logique par jour à nos amis & familles,
pour les distraire un peu en cette période difficile.

J'avais même bricolé un petit système de score, et j'en profite d'ailleurs pour féliciter ici les gagnants !

![Podium des gagnants : Elise & Thibaut ont la 1ère place, Isabelle la 2e et youchos la 3e](images/enigmes/podium.jpg)

Comme aujourd'hui marque la date du "déconfinement", nous avons décidé de conclure cette série d'énigmes.

C'est l'occasion de les partager plus largement ici, en incluant toutes celles que nous n'avons pas eu l'occasion de soumettre.

# Nonograms
Également nommés picross, logigraphes, hanjie, griddlers, ou encore logimages,
j'affectionne particulièrement ces puzzles logiques !

J'avais déjà évoqué ces casse-têtes par le passé dans [un article sur LinuxFr](https://linuxfr.org/news/generateurs-de-jeux-de-lettres-chiffres-libres),
et ce confinement a été l'occasion d'en rassembler quelques dizaines.

Une galerie collectant **52 grilles** est maintenant disponible en ligne à cette adresse :
<https://lucas-c.github.io/Nonogram/gallery.html>

Cliquez sur les points d'interrogations pour tenter de les résoudre !


# Topolokus

J'ai inventé ces petits casse-têtes l'année dernière, et les règles sont décrites [dans l'article de présentation](topoloku.html) sur ce blog.

Voici quelques grilles que j'ai conçu le mois dernier.
Cliquez sur les cases de chaque grille pour la remplir :

<table class="topoloku" data-size="[5, 4]"
       data-initial-letters='{"0,3": "✱", "1,3": "H", "2,0": "#", "3,3": "A"}'></table>

<br><br>

<table class="topoloku" data-size="[6, 5]"
       data-initial-letters='{"5,2": "P", "4,0": "L", "4,2": "T", "3,3": "K", "2,2": "K", "1,2": "K", "0,0": "K", "0,4": "K"}'
       data-secret-word-pos="[[5, 1], [5, 2], [5, 3], [2, 4]]"
       data-on-success="onTopolokuSuccess"></table>

<br><br>

<table class="topoloku" data-size="[5, 8]"
       data-initial-letters='{"0,0": "⦷", "3,3": "H", "0,4": "#", "1,4": "H", "2,6": "✱", "3,6": "H", "4,6": "#", "2,7": "#"}'></table>

<br><br>

<table class="topoloku" data-size="[5, 5]"
       data-initial-letters='{"2,0": "#", "2,1": "✱", "2,2": "E", "3,1": "E", "2,4": "#"}'></table>

<br><br>

<table class="topoloku" data-size="[6, 4]"
       data-initial-letters='{"0,0": "+", "3,0": "♡", "5,0": "=", "1,1": "L", "3,1": "L", "1,2": "=", "4,2": "=", "0,3": "L", "3,3": "+"}'
       data-secret-word-pos="[[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]"></table>

<br><br>

<table class="topoloku" data-size="[7, 10]"
       data-initial-letters='{"1,0": "X", "2,0": "Y", "3,0": "X", "6,0": "X", "0,2": "Z", "0,3": "X", "3,3": "X", "4,3": "X", "6,3": "X", "0,6": "X", "3,6": "X", "6,6": "X", "0,7": "X", "3,7": "X", "0,9": "X", "1,9": "X", "3,9": "X", "6,9": "X"}'></table>


# Rébus Concept

Comme il s'agit d'un jeu de société génial (sûrement en vente prêt de chez vous),
par respect pour le droit d'auteur je ne vais pas partager ici les splendides rébus que ma compagne a conçu.

Je peux cependant vous rediriger vers :

- [ces 10 rébus disponibles en PDF](https://concept-the-game.com/pnp/) sur le site officiel du jeu
- les [règles en PDF](https://concept-the-game.com/concept/files/rules/CONCEPT-RULES-FR.pdf)
ainsi que la très utile [aide de jeu](https://concept-the-game.com/concept/files/rules/CONCEPT-HELPSHEET-FR.pdf),
toujours sur leur site officiel


# Énigmages

Ces énigmes consistaient en des images se révélant progressivement,
et dont il fallait deviner ce qu'elles représentaient le plus tôt possible.

Elle sont toutes rassemblées sur cette page : [pages/enigmages.html](pages/enigmages.html)


<script type="module">
import { renderTopolokuUsingDataAttrs } from './images/enigmes/topoloku.js';
window.onTopolokuSuccess = (table) => {
  setTimeout(insertExtraLetter, 250, table, [[[5, 1], 'right-o'], [[5, 2], 'right-o'], [[5, 3], 'right-o'], [[2, 4], 'bottom-u']]);
  onTopolokuSuccess(table);
}
function insertExtraLetter(table, letterInfo) {
  if (!letterInfo.length) return;
  const [[i, j], cssClass] = letterInfo.shift();
  table.querySelector(`tr:nth-child(${j + 1}) > td:nth-child(${i + 1})`).classList.add(cssClass);
  setTimeout(insertExtraLetter, 500, table, letterInfo);
}
Array.from(document.getElementsByClassName('topoloku')).forEach(renderTopolokuUsingDataAttrs);
document.querySelectorAll('h1').forEach(function (title) {
  if (!title.classList.length) {
    title.id = title.textContent
                    .toLowerCase()
                    .replace(/[()?!:,'&@]/g, '')
                    .replace(/[à]/g, 'a')
                    .replace(/[ç]/g, 'c')
                    .replace(/[éêè]/g, 'e')
                    .replace(/[ï]/g, 'i')
                    .replace(/ /g, '-');
    const a = document.createElement('a');
    a.href = document.location + '#' + title.id;
    a['aria-hidden'] = true;
    a.style.float = 'left';
    a.style['padding-right'] = '4px';
    a.style['margin-left'] = '-20px';
    a.style['line-height'] = 1;
    title.appendChild(a);
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('aria-hidden', true);
    svg.setAttribute('height', 16);
    svg.setAttribute('width', 16);
    svg.setAttribute('viewBox', '0 0 16 16');
    svg.style.color = '#1b1f23';
    svg.style['vertical-align'] = 'middle';
    svg.style.visibility = 'hidden';
    a.appendChild(svg);
    const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
    path.setAttributeNS(null, 'fill-rule', 'evenodd');
    path.setAttributeNS(null, 'd', 'M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z');
    svg.appendChild(path);
    title.onmouseover = function () { this.getElementsByTagName('svg')[0].style.visibility = 'visible'; };
    title.onmouseout = function () { this.getElementsByTagName('svg')[0].style.visibility = 'hidden'; };
  }
});
</script>

<style>
table.topoloku { margin: 0 auto; }
.right-o::after {
  content: 'O';
  display: block;
  width: var(--cell-size);
  line-height: var(--cell-size);
  position: absolute;
  right: calc(-1 * var(--cell-size));
  top: 0;
  background-color: lightgreen;
}
.bottom-u::after {
  content: 'U';
  display: block;
  width: var(--cell-size);
  line-height: var(--cell-size);
  position: absolute;
  right: 0;
  bottom: calc(-1 * var(--cell-size));
  background-color: lightgreen;
}
</style>
