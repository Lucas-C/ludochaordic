Title: Test Topoloku
Tags: lang:fr, puzzle, sudoku, topologie, personal-project, maths, jeux
Slug: test-topoloku
Status: hidden
---

<link rel="stylesheet" type="text/css" href="images/enigmes/topoloku.css">

**LABO**: Topolokus en construction

<table class="topoloku" data-size="[3, 5]"
       data-initial-letters='{"0,1": "C", "1,1": "H", "1,2": "E", "0,3": "C", "1,3": "K"}'
       data-secret-word-pos="[[0,1], [1,1], [1,2], [0,3], [1,3]]"></table>

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
