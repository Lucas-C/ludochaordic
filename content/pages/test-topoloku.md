Title: Test Topoloku
Tags: lang:fr, puzzle, sudoku, topologie, personal-project, maths, jeux
Slug: test-topoloku
Status: hidden
---

<link rel="stylesheet" type="text/css" href="images/enigmes/topoloku.css">

**LABO**: Topolokus en construction

<table class="topoloku" data-size="[7, 10]"
       data-initial-letters='{"0,0": "X", "2,0": "Y", "3,0": "X", "6,0": "X", "0,2": "Z", "0,3": "X", "3,3": "X", "4,3": "X", "6,3": "X", "0,6": "X", "3,6": "X", "6,6": "X", "0,7": "X", "3,7": "X", "0,9": "X", "1,9": "X", "3,9": "X", "6,9": "X"}'></table>

<br><br>

<table class="topoloku" data-size="[6, 5]"
       data-initial-letters='{"5,2": "P", "4,0": "L", "4,2": "T", "3,3": "K", "2,2": "K", "1,2": "K", "0,0": "K", "0,4": "K"}'
       data-secret-word-pos="[[5, 1], [5, 2], [5, 3], [2, 4]]"
       data-on-success="onSuccess"></table>

<br><br>

<table class="topoloku" data-size="[5, 8]"
       data-initial-letters='{"0,0": "⦷", "3,3": "H", "0,4": "#", "1,4": "H", "2,6": "✱", "3,6": "H", "4,6": "#", "2,7": "#"}'></table>

<br><br>

<table class="topoloku" data-size="[4, 5]"
       data-initial-letters='{"0,0": "C", "1,0": "H", "3,1": "A", "0,2": "H", "3,2": "P", "1,3": "M", "2,3": "I", "1,4": "H", "2,4": "N"}'
       data-missing-letters="O"
       data-secret-word-pos="[[0, 0], [1, 0], [3, 1], [1, 2], [3, 2], [2, 3], [3, 3], [3, 4]]"></table>

<br><br>

<table class="topoloku" data-size="[5, 5]"
       data-initial-letters='{"2,0": "#", "2,1": "✱", "2,2": "E", "3,1": "E", "2,4": "#"}'></table>

<br><br>

<table class="topoloku" data-size="[4, 2]"
       data-initial-letters='{"1,1": "S", "2,1": "O", "3,1": "U"}'
       data-missing-letters="BI"
       data-secret-word-pos="[[0, 0], [1, 0], [1, 1], [2, 1], [3, 1]]"></table>

<style>
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
<script type="module">
import { renderTopolokuUsingDataAttrs } from './images/enigmes/topoloku.js';
Array.from(document.getElementsByClassName('topoloku')).forEach(renderTopolokuUsingDataAttrs);
window.onSuccess = function (table) {
  setTimeout(insertExtraLetter, 250, table, [[[5, 1], 'right-o'], [[5, 2], 'right-o'], [[5, 3], 'right-o'], [[2, 4], 'bottom-u']]);
}
function insertExtraLetter(table, letterInfo) {
  if (!letterInfo.length) return;
  const [[i, j], cssClass] = letterInfo.shift();
  table.querySelector(`tr:nth-child(${j + 1}) > td:nth-child(${i + 1})`).classList.add(cssClass);
  setTimeout(insertExtraLetter, 500, table, letterInfo);
}
</script>
