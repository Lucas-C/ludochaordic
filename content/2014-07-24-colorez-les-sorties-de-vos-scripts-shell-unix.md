Title: Colorez les sorties de vos Makefile & scripts shell unix
Date: 2014-07-24 16:07
Tags: lang:fr, bash, unix, couleur, script, shell, makefile, prog
Slug: colorez-les-sorties-de-vos-scripts-shell-unix
---
Malgré leurs nombreux défauts <sup><a href="#fn1" id="ref1">[1]</a></sup>, les scripts _shell_ restent bien pratiques. Pourquoi ? Parce qu'ils fonctionnent **exactement** comme l'interpréteur de ligne de commande de votre terminal Linux. Ils sont donc la solution la plus simple et rapide pour automatiser des enchaînement de commandes <sup><a href="#fn2" id="ref2">[2]</a></sup>.

Comme les scripts _shell_ sont très sujets aux erreurs d'exécution, il leur faudrait un article dédié pour détailler toutes les bonnes pratiques de programmation qui leur sont associées. Pour débuter, voici simplement comment ajouter rapidement et facilement de la couleur aux sorties de vos scripts.

Copiez le code suivant dans un fichier _bash\_colors.sh_ :

```
# This is a minimal set of ANSI/VT100 color codes
_END=$'\x1b[0m'
_BOLD=$'\x1b[1m'
_UNDER=$'\x1b[4m'
_REV=$'\x1b[7m'

# Colors
_GREY=$'\x1b[30m'
_RED=$'\x1b[31m'
_GREEN=$'\x1b[32m'
_YELLOW=$'\x1b[33m'
_BLUE=$'\x1b[34m'
_PURPLE=$'\x1b[35m'
_CYAN=$'\x1b[36m'
_WHITE=$'\x1b[37m'

# Inverted, i.e. colored backgrounds
_IGREY=$'\x1b[40m'
_IRED=$'\x1b[41m'
_IGREEN=$'\x1b[42m'
_IYELLOW=$'\x1b[43m'
_IBLUE=$'\x1b[44m'
_IPURPLE=$'\x1b[45m'
_ICYAN=$'\x1b[46m'
_IWHITE=$'\x1b[47m'

```

Ensuite, utilisez votre nouvelle palette de couleurs ainsi:
```
source ./bash_colors.sh
echo "${_BOLD}${_UNDER}${_ICYAN}Hello World${_END}"
```
Et voici la sortie obtenue:
<pre><span style="font-weight:bold;"></span><span style="text-decoration:underline;font-weight:bold;"></span><span style="background-color:teal;text-decoration:underline;font-weight:bold;">Hello World</span>
</pre>

Cette astuce est complètement indépendante du type de _shell_, et devrait fonctionner avec [tous les descendants du vénérable `sh`](http://hyperpolyglot.org/unix-shells), y compris [`dash`](//wiki.ubuntu.com/DashAsBinSh).

Bien que très simple, cette technique est quelque peu limitée: pas moyen d'obtenir du texte <strike>barré</strike> ou <em>italique</em> car certains terminaux supportent ces styles, mais pas tous <sup><a href="#fn3" id="ref3">[3]</a></sup>.

Si vous avez des besoin plus complexes, je vous invite à jeter un oeil au manuel de la commande `tput` qui est bien plus expressive et portable. Vous obtiendrez le même résultat que ci-desssus en l'utilisant ainsi:

```
echo "$(tput bold)$(tput smul)$(tput setab 6)Hello World$(tput sgr0)"
```

Dernière astuce: la commande `aha` permet de convertir les couleurs ANSI en HTML !

```
# echo "${_BOLD}${_UNDER}${_ICYAN}Hello World${_END}" | aha --no-header
<span style="font-weight:bold;"></span><span style="text-decoration:underline;font-weight:bold;"></span><span style="background-color:teal;text-decoration:underline;font-weight:bold;">Hello World</span>
```

<br><hr><br>

**EDIT [26/11/2014]** : En complément, voici comment appliquer cette astuce à `make`. Vous pouvez tester le code ci-dessous en le plaçant dans une fichier _Makefile_, puis en exécutant `make` :

```
cyan = /bin/echo -e "\x1b[36m\#\# $1\x1b[0m"

all:
    @$(call cyan,"Hello world !")
```

<br><hr><br>

<sup id="fn1">1. Entre autres limitations, les scripts _shell_ ne fournissent pas de gestion sûre des exceptions/erreurs d'execution, ne sont pas portables sous Windows nativement (vive [Cygwin](//www.cygwin.com) ! Une autre alternative : [Batsh](//github.com/BYVoid/Batsh)), ne fournissent pas de concepts de programmation de "haut niveau" (classes, modules, closures...)  et sont notoirement difficile à maintenir dès que le code devient un peu long. <a href="#ref1">↩</a></sup>

<sup id="fn2">2. Préférez néanmoins d'autres language pour des scripts robustes. [sh.py](//amoffat.github.io/sh) par exemple est une excellente solution pour bénéficier à la fois de la simplicité des scripts shells et de tous les avantages du language Python. <a href="#ref2">↩</a></sup>

<sup id="fn3">3. `gnome-terminal` supporte par exemple ces deux styles, mais pas [`tilda`](//github.com/lanoxx/tilda). Pour plus de détails sur les séquences de contrôle ANSI/VT100, jettez un oeil à l'article de [FLOZz' MISC](http://misc.flogisoft.com/bash/tip_colors_and_formatting) et au `man terminfo` <a href="#ref3">↩</a></sup>
