Title: Visualisation des votes sur republique-numerique.fr
Date: 2015-10-18 23:10
Tags: lang:fr, statistics, data-visualization, republique-numerique, charts, prog
Slug: visualisation-des-votes-sur-republique-numeriquefr
---
Quelques essais de visualisation de données pour célébrer la fin de cette expérimentation de débat citoyen en ligne.

Première tentative, utilisant [Charted](//www.charted.co), pour visualiser la répartition des nombre de votes toutes propositions confondues :

<iframe width="853" height="480" src="https://www.charted.co/?{%22dataUrl%22%3A%22http%3A%2F%2Fchezsoi.org%2Flucas%2Frepublique-numerique%2Fvotes_counts_frequencies_histogram.csv%22%2C%22seriesNames%22%3A{%221%22%3A%22freq_no%22}%2C%22charts%22%3A[{%22type%22%3A%22line%22%2C%22rounding%22%3A%22off%22%2C%22title%22%3A%22Positive%2FNegative%2FReserved%20votes%20count%20frequencies%20distribution%22%2C%22note%22%3A%22Data%20from%20republique-numerique.fr%20on%202015%2F10%2F18%20at%20midnight%22}]}" frameborder="0" allowfullscreen></iframe>

Exemple de lecture de ce graph: 33 propositions ont reçu exactement 8 votes positifs.

Ce graph n'apporte pas vraiment d'éclairage intéressant, mais il a été amusant a réaliser :)

En voici deux autres, plus simples et plus clairs, utilisant [CanvaJS](http://canvasjs.com/) :

<iframe width="800" height="640" src="/lucas/republique-numerique/arguments_counts.html" frameborder="0" allowfullscreen></iframe>

Pour une véritable analyse des votes sur la plateforme republique-numerique.fr en cette fin de consultation citoyenne en ligne, [cf. ce passionant article de Rue89](http://rue89.nouvelobs.com/2015/10/18/loi-numerique-dernier-jour-sursaut-lobbys-261722).

Les sources de ces tests de visualisation sont accessibles [ici](//github.com/Lucas-C/republique-numerique-stats).
