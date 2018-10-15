Title: Traduction du Temple du Non, une histoire interactive Twine du studio Crows Crows Crows
Date: 2018-06-18 9:00
Tags: lang:fr, python, storytelling, twine, l10n, i18n, open-source, jeux, prog
Slug: traduction-du-temple-du-non-une-histoire-interactive-twine-du-studio-crows-crows-crows
---

[Crows Crows Crows](https://crowscrowscrows.com) est un studio de jeu vidéo créé en 2015,
à l'origine entre autres du jeu complètement déjanté [Dr. Langeskov, The Tiger, and The Terribly Cursed Emerald: A Whirlwind Heist](https://crowscrowscrows.itch.io/dr-langeskov-the-tiger-and-the-terribly-cursed-emerald-a-whirlwind-heist) et le créateur du studio, William Pugh, est également un des auteurs de _The Stanley Parable_.

En 2016 ils ont sorti une courte "histoire dont vous êtes le héro", [Le Temple du Non](https://en.wikipedia.org/wiki/The_Temple_of_No).

<figure role="group">
  <img alt="Le Temple Du Non" src="images/2018/06/the-temple-of-no.png">
  <figcaption>Illustration de <a href="http://www.dominikjohann.de">Dominik Johann</a></figcaption>
</figure>

Ce court jeu - une dizaine de minute suffit pour le finir - est gratuit, jouable en ligne et a été réalisé avec [Twine](https://twinery.org).
Détail important également : l'intégralité des sources du jeu sont _open-source_ et sont [sur GitHub](https://github.com/CrowsCrowsCrows/the-temple-of-no/pulls).

J'ai **adoré** cette histoire loufoque et drôle, dans les lignées des autres jeux du studio.
L'écriture, tant des dialogues que de l'histoire générale, est absolument géniale.

Le 8 mai dernier, j'ai appris par la _newsletter_ de Crows Crows Crows qu'ils avaient fait une petite mise à jour du jeu,
pour introduire une fin cachée, avec même [une petite vidéo bande-annonce](https://www.youtube.com/watch?v=PYTyGJ2Xk5U) pour l'occasion.
Ça a été l'occasion de remettre le nez dedans, et je me suis alors mis en tête de traduire ce jeu en français.

Après plusieurs jours à m'arracher les cheveux pour traduire des références intraduisibles ([_Where's the trigger ?_](https://www.youtube.com/watch?v=xZ5cH1Dh2G0)),
et après plusieurs relectures de valeureux testeurs (merci Laëtitia, Alexandre et ma maman 🙏 😉),
je suis fier de vous présenter : [Le Temple du Non](https://chezsoi.org/lucas/le-temple-du-non/) ! _(cliquez sur le lien)_

J'espère que le jeu vous plaira !
Tout le mérite revient à ses génialissimes créateurs : Dominik Johann, William Pugh, Joe Finegold & Tom Schley.
N'hésitez pas à laisser un commentaire si vous avez apprécié, ou si vous avez repéré une maladresse dans la traduction.

---

Techniquement, comme le moteur des jeux Twine 1 est en Python,
et qu'il n'inclus pas de mécanisme de localisation,
j'ai écrit [quelques scripts Python](https://github.com/Lucas-C/the-temple-of-no/tree/master/l10n) pour y ajouter le support de [fichiers de traduction au format standard "gettext" `.po`](https://www.gnu.org/software/gettext/manual/gettext.html#PO-Files). Voici un example d'utilisation :
```
twine1_localizer.py translate the-temple-of-no.tws l10n/fr-FR.po the-temple-of-no_fr-FR.tws
```

Le fichier `l10n/fr-FR.po` contient toutes les traductions en français des phrases utilisées dans le jeu,
en utilisant comme clef l'identifiant de passage Twine. Le fichier `.tws` en sortie est ainsi localisé, et peu être exporté en HTML pour le rendu final.

Enfin, je souhaite encore faire quelques améliorations pour mettre le jeu aux normes d'accessibilité du web,
afin qu'il puisse être jouable uniquement à l'oreille par exemple. Je vous en reparlerai bientôt :)

---

PS: J'ai découvert qu'il y avait [un secret dans le jeu](https://www.reddit.com/r/crowscrowscrows/comments/8kcpbu/easteregg_in_the_temple_of_no/),
mais je ne l'ai pas encore déchiffré. Des idées ?? :)

<style>
    article img {
        display: block;
        margin: 0 auto;
        max-height: 20rem;
    }
    article figcaption {
        text-align: center;
    }
</style>
