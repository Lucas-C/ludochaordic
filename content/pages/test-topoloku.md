Title: Test Topoloku
Tags: lang:fr, puzzle, sudoku, topologie, personal-project, maths, jeux
Slug: test-topoloku
Status: hidden
---

<link rel="stylesheet" type="text/css" href="images/enigmes/topoloku.css">

Aujourd'hui, un nouveau type d'énigme !

Il s'agit d'un puzzle logique que Lucas a inventé l'année dernière : un **Topoloku**

Les règles du jeu sont dans [l'article de présentation](topoloku.html).

N'hésitez pas à laisser un commentaire si elles manquent de clarté !

Cliquez ensuite sur les cases de la grille pour la remplir.

<table class="topoloku" data-size="[5, 5]"
       data-initial-letters='{"2,0": "#", "2,1": "✱", "2,2": "E", "3,1": "E", "2,4": "#"}'
       data-solution="######✱✱E##✱EE##✱✱✱######"
       data-on-success="window.onSuccess(this)"></table>


---

**LABO**: ci-dessous d'autres Topolokus que je suis en train de construire / tester

<table class="topoloku" data-size="[4, 3]"
       data-initial-letters='{"0,0": "H", "1,0": "H"}'
       data-missing-letters="#"></table>

<br><br>

<table class="topoloku" data-size="[4, 2]"
       data-missing-letters="H%"></table>

<br><br>

<table class="topoloku" data-size="[4, 2]"
       data-initial-letters='{"1,1": "S", "2,1": "O", "3,1": "U"}'
       data-missing-letters="BI"
       data-secret-word-pos="[[0, 0], [1, 0], [1, 1], [2, 1], [3, 1]]"></table>

<script type="module" src="images/enigmes/topoloku.js"></script>
<script>
function onSuccess(table) {
  console.log(table);
}
</script>
