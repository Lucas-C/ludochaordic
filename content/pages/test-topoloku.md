Title: Test Topoloku
Tags: lang:fr, puzzle, sudoku, topologie, personal-project, maths, jeux
Slug: test-topoloku
Status: hidden
---

<link rel="stylesheet" type="text/css" href="images/enigmes/topoloku.css">

**LABO**: Topolokus en construction

<table class="topoloku" data-size="[6, 4]"
       data-initial-letters='{"0,0": "+", "3,0": "♡", "5,0": "=", "1,1": "L", "3,1": "L", "1,2": "=", "4,2": "=", "0,3": "L", "3,3": "+"}'
       data-secret-word-pos="[[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]"></table>

<br><br>

<table class="topoloku" data-size="[7, 10]"
       data-initial-letters='{"1,0": "X", "2,0": "Y", "3,0": "X", "6,0": "X", "0,2": "Z", "0,3": "X", "3,3": "X", "4,3": "X", "6,3": "X", "0,6": "X", "3,6": "X", "6,6": "X", "0,7": "X", "3,7": "X", "0,9": "X", "1,9": "X", "3,9": "X", "6,9": "X"}'></table>

<br><br>

<table class="topoloku" data-size="[5, 8]"
       data-initial-letters='{"0,0": "⦷", "3,3": "H", "0,4": "#", "1,4": "H", "2,6": "✱", "3,6": "H", "4,6": "#", "2,7": "#"}'></table>

<br><br>

<table class="topoloku" data-size="[5, 5]"
       data-initial-letters='{"2,0": "#", "2,1": "✱", "2,2": "E", "3,1": "E", "2,4": "#"}'></table>

<br><br>

<table class="topoloku" data-size="[4, 2]"
       data-initial-letters='{"1,1": "S", "2,1": "O", "3,1": "U"}'
       data-missing-letters="BI"
       data-secret-word-pos="[[0, 0], [1, 0], [1, 1], [2, 1], [3, 1]]"></table>

<script type="module">
import { renderTopolokuUsingDataAttrs } from './images/enigmes/topoloku.js';
Array.from(document.getElementsByClassName('topoloku')).forEach(renderTopolokuUsingDataAttrs);
</script>
