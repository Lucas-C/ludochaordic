Title: Solving peg solitaire in Python
Date: 2021-08-20 16:30
Tags: lang:en, problem-solving, algorithm, maths, python, gif, moviepy, prog, jeux
Slug: solving-peg-solitaire-in-python
---
<!-- Com'
* [x] https://fr.wikipedia.org/wiki/Solitaire_(casse-t%C3%AAte)#Solutions
* [ ] 
-->

The other day, while watching [_La Carte aux trésors_](https://fr.wikipedia.org/wiki/La_Carte_aux_tr%C3%A9sors)
at my elderly neighbor's house, I casually played [peg solitaire](https://en.wikipedia.org/wiki/Peg_solitaire) on a board she has.

After many failures at trying to get rid of all pawns but one, I started to wonder about the mathematics & algorithmics behind that game...

Back home, I was astonished to discover that **there is no solution to the European board with the initial hole centrally located**!
We could have been playing the game for a long, long time without knowing about this...
I was also delighted to discovered [Hans Zantema very elegant proof](https://en.wikipedia.org/wiki/Peg_solitaire#Strategy) of this.

Actually, the European board can be beaten by slightly shifting the initial hole position:

<figure>
  <img alt="European board shifted" src="images/2021/08/european_board_shifted.png">
  <figcaption>Game board shape by Wolfgang H. Wögerer - <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">CC BY-SA 3.0</a></figcaption>
</figure>

That's when I decided to write a Python solver in order to beat the game!

And I ended up by producing those GIFs:

<div class="side-by-side">
  <figure>
    <img alt="Best solution with 2 remaining pawns for the classic european board" src="images/2021/08/peg_solitaire_central_european_solution.gif">
    <figcaption>Best solution with 2 remaining pawns<br>for the classic european board</figcaption>
  </figure>
  <figure>
    <img alt="Best solution with 1 remaining pawn for the shifted european board" src="images/2021/08/peg_solitaire_alt_european_solution.gif">
    <figcaption>Best solution with 1 remaining pawn<br>for the shifted european board</figcaption>
  </figure>
</div>

The source code can be found here: [peg_solitaire_solver_gif.py](https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/peg_solitaire_solver_gif.py).
It is MIT licensed and the GIFs are under [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en).

The solver in itself is relatively simple, and the code not much worth commenting.
I used [Max Khrapov heuristic](https://github.com/mkhrapov/peg-solitaire-solver#algorithm):
without it, even while ignoring board symetries, I couldn't find a solution with less than 4 remaining pawns...
Even after testing more than 10.000.000 board configurations!
But now, it takes only a few seconds to complete on my computer.

The program relies on the [gizeh](https://pypi.org/project/gizeh/) & [moviepy](https://pypi.org/project/moviepy/) Pypi packages
in order to generate the GIFs, but those dependencies are not needed by the solver.

<style>
img { max-width: 16rem; }
.side-by-side {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: wrap;
}
@media (min-width:768px) {
  .side-by-side > * {
    max-width: 50%;
    margin: 0 1rem;
  }
}
</style>
