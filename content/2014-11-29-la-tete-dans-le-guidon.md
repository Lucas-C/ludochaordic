Title: La tête dans le guidon
Date: 2014-11-29 16:11
Tags: lang:fr, makefile, yagni, kiss, time-management, organisation, prog
Slug: la-tete-dans-le-guidon
---
En anglais, le titre pourrait se traduire par _"The head to the grindstone"_, soit littéralement "la tête sur la meule à aiguiser".
Rigolo non ?

Au vu du sujet cependant, _"Tales of a lost afternoon"_ sonnerait mieux je trouve. En effet, cet article va traiter d'organisation personnelle du temps. Le sujet est vaste, et il ne s'agira pas ici de parler de [procrastination](/lucas/blog/images/2014/Dec/Levels_of_Procrastination.jpg) ou d'outils de gestion de projet (j'ai déjà écris à propos d'[Etherpad](/lucas/blog/2014/10/10/en-setting-up-etherpad-in-a-server-subdirectory-aka-apache-config-hell)). Il s'agit simplement de partager mon expérience personnelle, et de suggérer quelques astuces pour tout ceux qui ont déjà perdu un peu trop de temps à coder "la tête dans le guidon" comme moi.

Pas forcément passionnant à priori donc. Mais bon, quitte à perdre son temps, autant en profiter pour apprendre de ses erreurs !

### Un Makefile récalcitrant
Vendredi après-midi, alors que je refactorisais le contenu du Makefile de mon projet actuel, je me suis mis en tête de créer une cible `help`, de manière à pouvoir détailler le rôle de chaque cible sur un simple `make help $targetname`.

Un [Makefile](http://fr.wikipedia.org/wiki/Makefile) est un outil d'automatisation assez ancien, mais toujours très utile et souvent employé, et je pensais que le temps investi sur ce problème serait rentabilisé en réutilisant cette nouvelle "recette" dans mes projets futurs...

<img src="images/2014/Dec/JonHamm_YeahSure.gif" title="Ouiii, c'est ça..." alt="JonHamm"/>

Cette idée faisait suite à ma trouvaille pour afficher les messages de Makefile en couleur, utilisée dans [mon article précédent](https://chezsoi.org/lucas/blog/2014/11/27/en-javascript-testing-adapting-testling-in-browser-tap-rendering/).
Cela peut sembler un peu vain, mais je trouve qu'un peu de couleur améliore énormément la lisibilité en fenêtre console.

Pour me conformer au principe DRY ([Don't Repeat Yourself](http://fr.wikipedia.org/wiki/Ne_vous_r%C3%A9p%C3%A9tez_pas)), je voulais réutiliser le même message pour `help` et pour la cible elle-même, pour éviter une duplication redondante :

```
COMPILER := bob
SRC_FILES := roley.c travis.c lofty.c scoop.c
OUT_FILE := home_sweet_home

print = /bin/echo -e "\x1b[36m\#\# $(1)\x1b[0m"
.PHONY: build

build: $(OUT_FILE)
    @:

$(OUT_FILE): $(SRC_FILES)
    @$(call print,"Bob is starting building")
    $(COMPILER) $(SRC_FILES)

help:
    @$(call print,"build: Guess what ? Bob's gonna build !")

```

Ma première approche fut d'essayer de définir une variable d'environnement dans la cible `help` qui rendrait inactives les autres commandes, puis d'invoquer la cible passée en argument. Comme les Makefiles ne semblent pas posséder de telle option, j'ai songé à préfixer toutes les commandes à passer sous silence par une variable qui serait transformée en `#` par la cible `help`.

```
build: $(SRC_FILES)
    @$(call print,"Bob is starting building")
    $(_)$(COMPILER) $(SRC_FILES)

help: _=\#
help: $(wordlist 2,3,$(MAKECMDGOALS))
    @:
```

Comme ça me semblait excessivement complexe et un peu fastidieux de préfixer toutes les commandes par `$(_)`, j'ai envisagé une autre solution.

J'ai réalisé qu'un simple `grep -A1 $targetname Makefile` était suffisant pour récupérer le message associé à chaque cible :

```
help:
    @grep -A1 $(wordlist 2,3,$(MAKECMDGOALS)) Makefile | tail -n 1
```

Les inconvénients ? Pas de couleurs, il fallait encore supprimer le hideux préfixe `@$(call print` de la ligne extraite, et cela forçait à rajouter des messages aux cibles "façades" comme `build`.

Dernière alternative: invoquer récursivement `$(MAKE) --dry-run`, ce qui résulte en une sortie inutilement verbeuse et sans couleurs.

Quelle que soit la solution adoptée, il restait un gros problème: comment désactiver l'interprétation des arguments en ligne commande par `make`, considérés comme des cibles supplémentaire à exécuter ?

C'est après avoir implémenté [ce magnifique hack trouvé sur StackOverflow](http://stackoverflow.com/a/14061796/636849), que j'ai enfin réalisé que je perdais complètement mon temps.

### 5 raisonnements qui font perdre du temps
Je vais essayer de disséquer ce qui me passe par la tête lorsque je perds plusieurs heures de mon temps ainsi:

1. **"maintenant ou jamais"** : je refuse de reporter la tâche à plus tard, en me disant que si je ne le fais pas MAINTENANT, je ne le ferai jamais.

2. **"ça ne prendra que 10min"** : j'ai tendance à sous-estimer l'étendue des ramifications du problème, et le temps qu'il va me falloir pour arriver à une solution acceptable.

3. **"autant commencer par ça puisque je suis motivé"**, plutôt que les tâches bien plus urgentes que je rechigne à faire. Et puis je prends ce bout de code qui refuse de fonctionner comme un vrai défi personnel...

4. **"c'est toujours utile à savoir faire"** : ça me resservira sûrement dans le futur de savoir ça. Il faut toujours continuer à apprendre non ?

5. quitte à la faire proprement, **"autant faire une solution générique"**.
<img src="images/2014/Dec/xkcd_the_general_problem.png" title="xkcd.com/974" alt="xkcd.com/974"/>


### Quelques astuces pour éviter ces écueils
Ces cinq points sont des exemples parfaits de biais cognitifs. Je ne suis pas le premier développeur à penser qu'[il est important de savoir les reconnaître](http://www.kitchensoap.com/2012/10/25/on-being-a-senior-engineer/) :

1. **"maintenant ou jamais"** : il y a deux aspects ici:
    * on surévalue l'importance d'une tâche mineure : est-ce si grave de ne pas la réaliser ? Lorsqu'on a la tête dans le guidon, on met de côté l'importance d'accomplir l'objectif global : quel que soit son urgence et la satisfaction personnelle bien plus grande qu'on en retirera, on ne voit qu'à court terme le défi technique qui nous fait face.
Pour s'en prévenir, une règle d'or: **YAGNI**, [You Ain't Gonna Need It](//fr.wikipedia.org/wiki/YAGNI). Si cette tâche n'est **pas nécessaire** à la réalisation de l'objectif, **ne perdez pas votre temps** avec !
    * on a peur d'oublier, de ne pas avoir le temps plus tard. Pour éviter ça, rien de plus simple : **notez-la dans une liste de tâches annexes**. Plus tard, avec le recul nécessaire, vous pourrez relire cette liste et reprioriser les plus urgentes. C'est aussi un très bon moyen de l'exorciser: la savoir notée quelque part me donne la tranquilité d'esprit nécessaire pour la chasser de mes pensées. Salvatore Sanfilippo, l'auteur de [Redis](http://redis.io), a écrit un très intéressant article sur ce sujet : ["la programmation par report de tâche"](http://antirez.com/news/51).

2. **"ça ne prendra que 10min"** :
    * ce biais cognitif là est dénommé _"[Planning fallacy](//en.wikipedia.org/wiki/Planning_fallacy)"_ chez nos confrères anglophones. Estimer la durée d'une tâche, c'est difficile. Et de manière générale, on a tendance à sous-estimer.
    * si on ne fait pas attention au temps qui passe, 10min deviennent facilement 60.
    * ce schéma peut se répéter à la prochaine difficulté rencontrée, et entraîner une succession de "tâches digressives" façon boule de neige.
<img src="images/2014/Dec/TeteDansLeGuidon_spiral.png" title="Réalisé avec zwibbler.com" alt="Spiral of side-tasks digression"/>
Pour éviter cet écueil, il faut se forcer à ne pas partir dans la moindre "tâche digressive"  : souvenez vous, utilisez un journal de tâches annexes, et YAGNI !
Et pour éviter les sous-estimations, une seule solution: devenir meilleur à estimer les durées de tâches. Le livre _"[The Pragmatic Programmer](http://blog.codinghorror.com/a-pragmatic-quick-reference/)"_ recommande de garder un suivi de ses estimations, pour apprendre de ses erreurs.
Une solution didactique pour s'y entraîner : la [technique _Pomodoro_](//fr.wikipedia.org/wiki/Technique_Pomodoro).

3. **"autant commencer par ça puisque je suis motivé"** : là, je prétends qu'il s'agit d'une tâche de grande importante, voir même "bloquante", alors qu'en vérité je trouve juste ça bien plus passionnant que d'autres choses que j'ai à faire. De plus, et je me réfère là à l'excellent _"Reality is Broken"_ de Jane McGonigal, une telle "tâche digressive" se compose souvent d'une succession de petits défis techniques, stimulants intellectuellement et générateur d'adrénaline, et formant au final une spirale addictive. Chaque solution trouvée entrouvre la porte d'un autre problème annexe, que l'on s'empresse d'attaquer par curiosité, goût du défi et envie de peaufiner notre solution.
Au fond, il s'agit essentiellement d'un problème de **motivation** et de **discipline**. Pour garder l'envie de programmer, il faut se garder du temps pour écrire du code plus _fun_; mais il faut aussi être conscient qu'atteindre ses objectifs requiert de la discipline personnelle, et de parfois faire des choses moins intéressantes : "d'abord le boulot, après les loisirs" comme disait mon père !

4. **"c'est toujours utile à apprendre"** : là, c'est illusion de l'apprentissage comme une fin et pas comme un moyen. Comprenez-moi bien : je suis un partisant 100% convaincu de l'apprentissage continu tout au long de la vie; mais apprendre peut devenir une addiction, et il est trompeur de penser que toutes les sources de connaissance sont aussi enrichissantes et utiles les unes que les autres.
En pratique : deux douzaines de réponses détaillées sur _StackOverflow_ ont bien moins de valeur que de suivre un cours entier de _Coursera_ ou _Codeademy_ sur un sujet nouveau.
Il n'est pas utile de connaître tous les _hacks_ du monde, parfois mieux vaut réfléchir par soi-même à une solution plus simple.
<img src="images/2014/Dec/A_mindless_worker_is_a_happy_worker.jpg" alt="Futurama: shut up and do your job !">

5. **"autant faire une solution générique"**  : là, c'est l'_[Over-engineering](//en.wikipedia.org/wiki/Overengineering)_ qui guète.
La solution la plus simple et rapide est parfois la meilleure, pas besoin de tomber dans l'écueil de la solution inutilement générique.
Autrement dit : KISS, [Keep It Simple, Stupid](//fr.wikipedia.org/wiki/Principe_KISS) !
Et puis YAGNI aussi !
Au passage, ce _webcomic_ XKCD a d'ailleurs une "suite" intéressante: [xkcd.com/1205](http://xkcd.com/1205).

En conclusion, il vaux mieux s'arrêter quelques minutes pour prendre du recul, s'extraire de la frénésie du [_flow_](//en.wikipedia.org/wiki/Flow_%28psychology%29) et reconsidérer l'importance de chaque tâche.
**Dans le doute, prenez une pause !**

Il faut être préparé à ressentir un peu de frustration à abandonner une tâche passionnante, mais je vous mets au défi d'essayer, vous ne regretterez pas !

### [Tl;dr](http://fr.wikipedia.org/wiki/Liste_de_termes_d%27argot_Internet#T.2C_U.2C_V)
Mon humble avis:

- rester concentré requiert [un minimum d'organisation](http://www.edudemic.com/age-distraction/)
- KISS & YAGNI + noter les idées d'amélioration non-urgentes dans un fichier
- se forcer à prendre une pause de 10 minutes toutes les 2 heures, ou alors de changer de tâche


### Epilogue

Quant au Makefile, j'ai opté pour le strict minimum :

```
build: $(OUT_FILE)
    @:

$(OUT_FILE): $(SRC_FILES)
    # Bob is starting building
    $(COMPILER) $(SRC_FILES)

help:
    # make -n target           # --dry-run : get targets description
    # make -B target           # --always-make : force execution of targets commands, even if dependencies are satisfied
    # make DEBUG=0             # variable override
    # make --debug[=abijmv]    # enable variants of make verbose output
```

Pas de `make help $targetname`: juste de simples commentaires affichés à l'exécution et sur un `make --dry-run $targetname`.

Au revoir également l'appel au `print` coloré : la coloration se fera désormais côté console par [`grc`](http://michaelheap.com/grc/), configuré dans _/usr/share/grc/conf.gcc_ pour mettre en couleur les commentaires :

```
.........
# comments
regexp=^#.*
colours=green
count=stop
```

<br>
<hr>
<br>

### Digression n°1 : une commande `pomodoro` ?

Suite à la découverte de la technique _Pomodoro_ et de la lecture de _"Reality is Broken"_ de Jane McGonigal, les doigts me brûlent de créer un utilitaire en ligne de commande `pomodoro-karma` avec les caractéristiques suivantes :

- tâche configurée au départ avec un objectif + un délai (par exemple 1h)
- au bout du délai impartit, l'application s'affiche au premier plan en plein écran (bloque même le bureau ?) pour vérifier si la tâche a été réalisée
- inspiré par les idées de *ludification* de Jane McGonigal : score de Karma: +1 si l'utilisateur fait bien une pause de 5min; +1 s'il a accompli sa tâche; +0 sinon
- on peut indiquer à l'application que la tâche a été effectuée plus tôt
- l'application fournira également des statistiques sur l'exactitude et l'évolution des estimations de l'utilisateur

Techniquement:

- Python 3
- persitence des données basique : <https://docs.python.org/3/library/persistence.html>
- rendu à travers le navigateur ? Pros: portable, _user-friendly_. Cons: plus complexe à coder que d'autres solutions basées sur des bibliothèques existantes d'interaction-utilisateur ?

Maaaais... il existe déjà des centaines de projets similaires, donc je ne le coderai pas :)
<https://github.com/search?q=pomodoro> : 1273 résultats, 148 en Python.
Je vais juste essayer [ce package sous Ubuntu](http://askubuntu.com/a/190675/185582).

<br>
<hr>
<br>

### Digression n°2 : qu'est-ce qui a sa place sur un blog ?

Je suis loin d'être le premier à écrire ce type de _mea culpa_. Des tas de développeurs s'y sont essayé, y compris des "personnalités" du domaine. Niveau originalité donc, on repassera. Pourquoi alors, pondre un énième pamphlet dégoulinant de recommandations déjà entendues mille fois ?

- est-ce que ça excuse les heures de boulot perdues ?
- est-ce un sujet intéressant, utile à mes lecteurs ? Selon quels critères ?
- quelle image ça donne de moi ?

Je n'ai pas de réponse à ces questions, mais voilà quelques unes de mes raisons :

- c'est un excellent exercice de communication & de didactique
- de manière générale, coucher mes idées par écrit m'aide à clarifier mes idées, et me force à justifier certaines hypothèses que je tenais pour acquises
- je ne veux pas que ce blog soit exclusivement technique. La programmation a de nombreux aspects humains, et devenir un meilleur développeur signifie aussi se pencher sur les aspects de communication, de travail d'équipe et d'organisation.
- en écrivant à propos de ces erreurs, je m'engage en quelque sorte à ne pas les reproduire
