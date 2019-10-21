Title: Battledev de RegionJobs : Python vs Java
Date: 2016-04-14 20:04
Tags: lang:fr, python, java, battledev, performances, interpreter, pythonchallenge, algorithms, prog
Slug: battledev-de-regionjobs-python-vs-java
---
En mars dernier, j'ai participé à la Battledev de RegionJobs.

Et c'était super fun.

Pour ceux qui ne connaissent pas, c'est une compétition de programmation en ligne, où l'on doit résoudre 5 questions de difficulté croissante en 2 heures.

J'ai eu l'occasion d'y participer avec quelques collègues, et ça a été à la fois un chouette challenge et moment sympa à passer ensemble.

Le 8 novembre prochaine, une nouvelle édition à lieu, alors [inscrivez-vous](https://battledev.blogdumoderateur.com) !
J'en serai :)

---

Toutefois, il y a un petit quelque chose qui m'est resté en travers de la gorge suite à cette battle : **pour la dernière question, les solutions étaient de complexité différente selon les langages**.

Je m'explique: lors de la BattleDev, chaque participant à le choix de formuler sa réponse dans la langue de son choix. Personnellement, j'ai participé en Python.

En fin de concours, la société Isograd qui a mit en place le challenge révèle des solutions possibles à chaque question. Celles-ci sont disponibles sur cette page: <http://www.isograd.com/FR/solutionconcours.php> (choisir "Battle Dev RegionsJob - Mars 2016").

Si vous allez y jeter un oeil, vous pourrez constater que selon les langages, la solution de la question 5 est plus ou moins complexe:

- `C`, `NodeJS`, `Ruby` : pas de solution proposée
- `C#`, `C++`, `Java` : solution "simple" ([exemple de la solution Java](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/battledev_regionsjobs_isograd_2016-03-22/challenge5_soluce.java)).
- `Python`, `PHP` : solution complexe à base de `RangeMinQuery` ([exemple de la solution Python](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/battledev_regionsjobs_isograd_2016-03-22/challenge5_soluce.py)).

Pourquoi ?
Je n'ai trouvé aucune justification officielle.
Mon hypothèse est la suivante: je pense que les interprêteurs des langages `PHP` et `Python` utilisé par Isograd dans son service d'évaluation des réponses sont bien moins performants que ceux pour `C#` / `C++` / `Java`. Probablement à cause la différence fondamentale entre ces 2 familles de langages : les uns sont compilés, les autres interprétés<sup><a href="#fn1" id="ref1" style="font-size: small">[1]</a></sup>.
Cette limitation impose d'être plus "malin" en terme d'algorithme pour les langages plus lents, d'où le recours à une classe `RangeMaxQuery` **très** bien pensée.

Néanmoins, il reste indéniable que les participants étaient fortement favorisés selon le langage choisi.

J'espère sincèrement que la prochaine édition de la BattleDev ne comportera pas ce genre d'inégalités linguistiques.

<img alt="Animation tirée de The Big Lebowsky" src="images/wwcb/OnlyOneToGiveAShitAboutRules.gif" style="width: 60%">

---

<sup id="fn1">1. Même si en fait un code Python est transcris en bytecode de la même manière qu'en Java. <a href="#ref1">↩</a></sup>

