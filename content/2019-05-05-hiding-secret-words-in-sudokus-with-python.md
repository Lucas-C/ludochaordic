Title: Hiding secret words in Sudokus with Python
Date: 2019-05-05 15:30
Tags: lang:en, puzzle, sudoku, python, numpy, numba, algorithm, open-source, maths, prog, jeux
Slug: hiding-secret-words-in-sudokus-with-python
---

Yesterday I was crafting some puzzles for my girlfriends,
and I was looking for letter-based ones where I a secret word
would be revealed once solved.

![Solution of a size-12 Wordoku I created displaying the hidden words: AMOUR PASSION](images/2019/05/sudoku-letters-amourpassion-solution.png)
![Wordoku initial grid for this same puzzle](images/2019/05/sudoku-letters-amourpassion-grid.png)

With this same goal, I had already once worked on an open-source JS
[word search](https://en.wikipedia.org/wiki/Word_search) generator:
<https://lucas-c.github.io/wordfind/>

_(pour les francophones, vous trouverez quelques autres générateurs de jeux de lettres / chiffres dans [cet article sur linuxfr.org](https://linuxfr.org/news/generateurs-de-jeux-de-lettres-chiffres-libres))_

This time I started crafting [Masyu](https://fr.wikipedia.org/wiki/Masyu) puzzles into letter shapes,
but then I realized Sudokus would be a perfect pick, with digits replaced by letters !
Those are sometimes named [Wordokus](https://en.wikipedia.org/wiki/Sudoku#Alphabetical_Sudoku).

Hence I wrote a Wordoku generator in Python,
where the secret word appears in the diagonal starting from the top-left:
[secret_word_sudokulike_grid_generator.py](https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/secret_word_sudokulike_grid_generator.py)

```
# ./secret_word_sudokulike_grid_generator.py ensemble

   ..L.|...J               EMLS|BNKJ
   BNK.|...L               BNKJ|EMSL
   ---------               ---------
   ....|....               MLSB|JENK
   J..E|.S.M               JKNE|LSBM
   ---------   solution:   ---------
   S..K|....               SBJK|MLEN
   L..N|KB.S               LEMN|KBJS
   ---------               ---------
   .J.M|.KLB               NJEM|SKLB
   .S.L|..ME               KSBL|NJME
```

Because I wanted to be able to generate grids for any size, even for prime number sizes like 7,
this program can drop the constraint of the boxes for those cases:
the generated grid is a pseudo-sudoku, where the only rules are that columns & rows must contain all letters.

```
# ./secret_word_sudokulike_grid_generator.py --no-boxes-constraint ensemble

   E . M . . L . .               E D M S N L Q B
   . N . M . . S L               Q N D M B E S L
   B E . . . . . N               B E S L Q D M N
   . . . . . . . .   solution:   N S B E L Q D M
   D . L B . N . S               D Q L B M N E S
   . M E . . . N .               L M E D S B N Q
   S B . . E . . D               S B Q N E M L D
   . . . Q D S B .               M L N Q D S B E
```

You can see that the word `ENSEMBLE` appears on the diagonal in the solution.

On the technical side, the script is relatively straightforward.
I only needed a fast sudoku solver.
I used Ali Assaf's excellent one, that he describes in this article:
<https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html>

Using the fact that Sudoku puzzles may be described as an [exact cover problem](https://en.wikipedia.org/wiki/Exact_cover#Sudoku),
he implemented Donald Knuth « Algorithm X » with _Dancing Links_ ( how poetic ! )

Kudos to him for writing this. The code is under the GNU GPL license.

At some point I tried to optimize the code using Numpy & Numba,
but I faced many issues with the later lib:
no support for `np.argwhere` / `np.setdiff1d` / `np.isin` / `np.in1d`,
[new bugs](https://github.com/numba/numba/issues/4053)...
I started looking at at contributing by implementing those,
but Numba's internal code is quite complex. 😞

In the end I did not bother improving the performances:
even for a large grid like the size-12 one at the top of this article,
the script execution times is between 10s and 10min,
which is totally OK for my needs.

**EDIT [2019/10/05]:** I discovered that this lind of puzzle was sometimes called « SudoLettre » in French.

<script>
document.querySelectorAll('article img').forEach(img => img.title = img.alt)
</script>

<!--
| |S| | |P| |M|R| |O|W| |
|-|-|-|-|-|-|-|-|-|-|-|-|
| | |W|L| |G|O| |I| | |P|
|U| | | |L| | |W| |A| | |
|I| |P| | | | |A| |R| | |
|S|L|A| |R| | |N| | |P|I|
|W| | | |I|P|S| | | | | |
|N| | |S| | | |G| |P| | |
| |P| |O| | | |S|L| | |A|
|G|A| | |U| |I|P| | |R|O|
|O| | |G| | |U| | |I|S| |
| | | | | | | | |M| | |W|
| |W|U| | | | | | |L|A| |

<br>

A|S|G|N|P|I|M|R|U|O|W|L
-|-|-|-|-|-|-|-|-|-|-|-
R|M|W|L|A|G|O|U|I|S|N|P
U|I|O|P|L|S|N|W|R|A|M|G
I|O|P|U|M|W|L|A|N|R|G|S
S|L|A|M|R|U|G|N|O|W|P|I
W|G|N|R|I|P|S|O|A|M|L|U
N|U|R|S|O|L|A|G|W|P|I|M
M|P|I|O|N|R|W|S|L|G|U|A
G|A|L|W|U|M|I|P|S|N|R|O
O|N|M|G|W|A|U|L|P|I|S|R
L|R|S|A|G|N|P|I|M|U|O|W
P|W|U|I|S|O|R|M|G|L|A|N
-->

<style>
article img { display: inline-block; }
article pre { line-height: 1rem; }

td, th {
  font-weight: normal;
  font-size: 2rem;
  font-size: 2rem;
  padding: 0;
  width: 2.5rem;
  height: 2.5rem;
  text-align: center;
}

td:nth-of-type(4), th:nth-of-type(4),
td:nth-of-type(8), th:nth-of-type(8) {
  border-right: 3px solid black;
}
tr:nth-of-type(3), tr:nth-of-type(6), tr:nth-of-type(9) {
  border-top: 3px solid black;
}
th:nth-of-type(1),
tr:nth-child(1) td:nth-of-type(2),
tr:nth-child(2) td:nth-of-type(3),
tr:nth-child(3) td:nth-of-type(4),
tr:nth-child(4) td:nth-of-type(5),
tr:nth-child(5) td:nth-of-type(6),
tr:nth-child(6) td:nth-of-type(7),
tr:nth-child(7) td:nth-of-type(8),
tr:nth-child(8) td:nth-of-type(9),
tr:nth-child(9) td:nth-of-type(10),
tr:nth-child(10) td:nth-of-type(11),
tr:nth-child(11) td:nth-of-type(12) {
  background-color: #ffc4c4;
}
</style>
