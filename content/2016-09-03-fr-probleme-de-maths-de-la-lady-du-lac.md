Title: [FR] Problème de maths de la lady du lac
Date: 2016-09-03 11:09
Tags: tangente, maths, canvas, web, trigonometry
Slug: fr-probleme-de-maths-de-la-lady-du-lac
---
Dans [le numéro 171 du magazine tangente](http://www.tangente-mag.com/numero.php?id=131), page 47, un intéressant petit problème mathématique est posé au lecteur.

> Une jeune femme était en vacances au bord du lac Circulaire, un grand plan d’eau artificiel ainsi nommé pour sa forme circulaire précise. Pour échapper à un soupirant envahissant qui la harcelait, elle monta dans une barque et rama jusqu’à un radeau ancré au centre du lac. Son poursuivant décida de l’attendre sur le rivage, sachant qu’elle devrait revenir à terre. Il pouvait marcher quatre fois plus vite qu’elle pouvait ramer, et pensait pouvoir la joindre dès que son bateau toucherait le bord du lac.
Mais la jeune femme, major de mathématiques au Radcliffe College et sportive de haut niveau, savait qu’une fois à terre, elle pourrait distancer le fâcheux. Il était seulement nécessaire de mettre au point une stratégie pour accoster à un point du rivage avant qu’il ne puisse y arriver. Elle trouva rapidement un plan assez simple.
**Quelle était la stratégie de la jeune femme ?**
On suppose qu’elle connaît à tout moment sa position exacte sur le lac.

Cependant, la solution proposée par _tangente_ ne me satisfait pas vraiment. L'énoncé de la question laisse un peu de liberté d'interprétation, et la solution du magazine comporte, je crois, une petite incohérence.

Afin de visualiser les différentes solutions possibles selon les règles que l'on choisit de fixer, j'ai développé **un petit simulateur web**: [https://chezsoi.org/lucas/maths/lady\_of\_the\_lake.html](https://chezsoi.org/lucas/maths/lady_of_the_lake.html)

La configuration par défaut correspond à la solution de _tangente_ :
<img src="/lucas/blog/content/images/2016/09/SolutionTangente.png" style="width: 50%">

Cete solution prend comme postulat que la direction du soupirant est **invariante**, c'est-à-dire qu'il choisit une direction pour tourner autour du lac au départ, et **qu'il n'en change jamais ensuite**.

Néanmoins, avec un tel postulat, une solution bien **plus simple** est de prendre le soupirant **à contre-pied** :
<img src="/lucas/blog/content/images/2016/09/ContrePied.png" style="width: 50%">

Au-contraire, si on considère que le poursuivant **adapte sa direction** afin de se rapprocher systématiquement de la lady, alors **la solution de _tangente_ ne fonctionne pas**:
<img src="/lucas/blog/content/images/2016/09/SolutionTangenteAvecSoupirantChangeantDeDirection.png" style="width: 50%">

Essayons maintenant de simuler une lady qui **s'adapte véritablement et dynamiquement** à la position de son poursuivant, <cite>"de sorte que le centre du lac soit toujours compris entre elle et son poursuivant sur le rivage, les trois points étant alignés"</cite>, comme propose la solution de _tangente_ :
<img src="/lucas/blog/content/images/2016/09/FullAdaptiveWithRatio4.png" style="width: 50%">

**Que se passe-t-il ??**

Avec un rapport de vitesses de 4, la lady **ne peut pas échapper à son poursuivant**. Elle est bloquée au centre du lac, sans pouvoir le prendre de vitesse.
Il est intéressant de remarquer que sa trajectoire semble converger vers un cercle de rayon _r_ / 4 (où _r_ est le rayon du lac).

Enfin, on peut essayer des rapports de vitesses plus petits, pour essayer de déterminer quand il devient possible pour la lady de gagner.
Les valeurs obtenues avec le simulateur web sont sensibles au "pas" de simulation, mais avec un rapport de **3.6** on peut par exemple observer que la lady bat son poursuivant de vitesse :
<img src="/lucas/blog/content/images/2016/09/FullAdaptiveWithRatio3.6.png" style="width: 50%"

Qu'en pensez-vous ? N'hésitez pas à laisser votre avis sur ce problème en commentaire !