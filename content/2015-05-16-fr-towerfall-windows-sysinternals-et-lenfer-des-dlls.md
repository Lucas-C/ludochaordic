Title: [FR] Problème avec Windows Update & .NET, Sysinternals et l'enfer des DLLs
Date: 2015-05-16 16:05
Tags: windows, sysinternals, dll, -net
Slug: fr-towerfall-windows-sysinternals-et-lenfer-des-dlls
---
Cette après-midi, j'ai enfin résolu un problème d'installation de Microsoft .NET Framework qui datait de presque un an.

Dans l'espoir que ça puisse aider quelqu'un qui rencontre la même erreur, et parce que j'ai appris à utiliser un outil intéressant au passage, je me fends d'un petit article de blog pour expliquer cette mésaventure.

J'ai Windows Seven en dual-boot, et ne l'utilise plus très souvent désormais, essentiellement pour jouer à des jeux vidéos de temps en temps.
En relisant mes notes de debug d'août 2014, où ce problème m'a explosé à la tronche pour la première fois, je vois **beaucoup** de détresse.

<img src="https://chezsoi.org/lucas/wwcb/photos/computer-smash-Mark-Wahlberg-angry.gif">

J'ai passé plusieurs dizaines d'heures à essayer de résoudre le souci, pour finalement abandonner.
Tout a commencé par une erreur 0x80073712 systématique de Windows Update, empêchant toute mise à jour du sytème. Je retranscris ici l'intégralité de mes périgrinations, peut-être que quelqu'un y reconnaîtra des symptômes:

- `Store corruption detected in function [...] MissingWinningComponentKey` dans le `Windows\Logs\CBS\CBS.log`
- [Microsoft Safety Scanner](http://www.microsoft.com/security/scanner/en-us/default.aspx), [Farbar Service Scanner](http://www.bleepingcomputer.com/download/farbar-service-scanner/dl/62), `sfc /scannow` et Microsoft [CheckSUR/SURT](https://www.microsoft.com/en-us/download/details.aspx?id=20858) ne détectent rien
- des threads sur [sysnative.com](http://www.sysnative.com) et [sevenforums.com](http://www.sevenforums.com) me poussent à soupçonner `mscorwks.dll` et le framework .NET.
- j'essaye [l'outil de réparation du framework .NET de Microsoft](http://support.microsoft.com/kb/2698555) ainsi que [celui d'Aaron Stebner](http://blogs.msdn.com/b/astebner/archive/2008/10/13/8999004.aspx), chaudement recommandé sur plusieurs forums, sans succès
- après bien d'autres essais infructueux, je finis par identifier et résoudre le problème initial de Windows Update ! [Le manifeste Services à base de composants (CBS) était endommagé](http://support.microsoft.com/kb/957310/fr). Solution: mettre à jour Windows à partir du CD d'installation, ce qui nécessite 17Go d'espace libre, me prend 2 heures puis nécessite une MAJ de GRUB pour rétablir le dual-boot.
- **mais** toujours pas moyen de mettre à jour .NET en version 4 :(

Mais cette après-midi donc, voulant pouvoir jouer à [Towerfall Ascension](http://store.steampowered.com/app/251470) que je venais d'acquérir, je me repenche sur le problème, et trouve un article de blog expliquant la solution : [MERCI mille fois Soumitra Mondal !!!](http://blogs.msdn.com/b/vsnetsetup/archive/2013/09/30/error-25003-error-occurred-while-initializing-fusion.aspx).

<a href="https://xkcd.com/979/"><img src="http://imgs.xkcd.com/comics/wisdom_of_the_ancients.png" title="xkcd/979 : Wisdom of the Ancients"></a>

L'origine du problème ? Des DLLs corompues (ou aux permissions incorrectes, allez savoir).
Mais le plus intéressant dans cette histoire, ça a été la réponse de `atverweij` sur [ce thread du support Microsoft](https://social.msdn.microsoft.com/Forums/vstudio/en-US/ae70d0f8-2dcb-4ff5-9d9f-94efd30455c3/incorrect-function-during-install-of-net-40-on-windows-2008-x64-sp2), indiquant qu'il avait identifié les fichiers posant problème grâce au Process Monitor des **Sysinternals**.

Les Sysinternals sont de fantastiques outils, [fournis par Microsoft](https://technet.microsoft.com/en-us/sysinternals/bb545021.aspx) mais pas installés par défaut, permettant de véritablement **comprendre** et **résoudre** de nombreux comportements obscurs de Windows. Le genre de bugs incompréhensibles pour lesquels mes seuls alliés auparavant étaient Google et les fantastiques communautés d'internautes des forums d'aide Windows.

En voici quelques uns (j'utilise les 3 régulièrement comme dev ou gamer) :

- [Process Explorer](https://technet.microsoft.com/en-us/sysinternals/bb896653) a depuis longtemps remplacé l'explorateurs de processus Windows de base sur mon PC. Il est bien plus complet, fournissant entre autres des graphes d'utilisation CPU / IO et **une arborescence des processus** (à la `pstree` sous Linux). Il permet ausi de lister les fichiers ouverts par des programmes, et ainsi de trouver cet enfoiré de @#%£&§ de processus qui empêche la suppression d'un fichier.
- [TCPView](https://technet.microsoft.com/en-us/sysinternals/bb897437) est l'équivalent d'un `netstat` sous Linux. Très utile pour déterminer quel processus utilise quel port !
- [Processus Monitor](https://technet.microsoft.com/en-us/sysinternals/bb896645) enfin, permet entre autres de déterminer les tentatives d'ouverture de fichier râtées d'un processus. C'est un peu l'équivalent d'un `strace` sous Linux.

Grâce à ce dernier outil, j'ai bien vérifié qu'il m'aurait été possible de déterminer à cause de quel fichier récalcitrant mon installateur de Microsoft .NET Framework 4 plantait systématiquement.

Ce post n'a pas pour but de décrire comment se servir de tous les outils, mais je vous recommande [cet article de HowToGeek](http://www.howtogeek.com/school/sysinternals-pro/lesson1/) qui est une bonne introduction aux Sysinternals.