Title: Test Topoloku
Tags: lang:fr, puzzle, sudoku, topologie, personal-project, maths, jeux
Slug: test-topoloku
Status: hidden
---

<link rel="stylesheet" type="text/css" href="images/enigmes/topoloku.css">

**LABO**: Topolokus en construction

<table class="topoloku" data-size="[5, 5]"
       data-initial-letters='{"2,0": "#", "2,1": "✱", "2,2": "E", "3,1": "E", "2,4": "#"}'
       data-solution="######✱✱E##✱EE##✱✱✱######"></table>

<br><br>

<table class="topoloku" data-size="[4, 2]"
       data-missing-letters="H%"></table>

<br><br>

<table class="topoloku" data-size="[4, 2]"
       data-initial-letters='{"1,1": "S", "2,1": "O", "3,1": "U"}'
       data-missing-letters="BI"
       data-secret-word-pos="[[0, 0], [1, 0], [1, 1], [2, 1], [3, 1]]"></table>

<script type="module">
import { renderTopolokuUsingDataAttrs } from './images/enigmes/topoloku.js';
Array.from(document.getElementsByClassName('topoloku')).forEach(renderTopolokuUsingDataAttrs);
function onSuccess(table) {
  console.log(table);
}
</script>
