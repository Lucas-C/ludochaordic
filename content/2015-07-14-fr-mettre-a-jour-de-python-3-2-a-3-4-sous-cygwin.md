Title: [FR] Mettre à jour de Python 3.2 à 3.4 sous Cygwin
Date: 2015-07-14 11:07
Tags: python, pip, cygwin, apt-cyg
Slug: fr-mettre-a-jour-de-python-3-2-a-3-4-sous-cygwin
---
Depuis mai 2015, [Python 3.4 est disponoble sous Cygwin](https://www.cygwin.com/ml/cygwin/2015-05/msg00080.html).

Si vous aviez précédement installé Python 3.2, voici comment passer à la version 3.4.

Tout d'abord, je vous recommande l'excellent gestionnaire de package [apt-cyg](https://github.com/transcode-open/apt-cyg). C'est tout simplement une interface en ligne de commande équivalente au `setup-x86.exe` (ou `setup-x86_64.exe`) classique de Cygwin, servant à l'installation et la mise à jours de package.
Voici comment l'installer simplement:
```
mkdir ~/bin && echo 'export PATH=$PATH:~/bin' >> ~/.bashrc
lynx -source rawgit.com/transcode-open/apt-cyg/master/apt-cyg > apt-cyg
install apt-cyg ~/bin/ && rm apt-cyg
```

Maintenant il vous suffit simplement de désinstaller puis de réinstaller le package `python3`, qui se réinstallera avec la nouvelle version 3.4 par défaut:
```
apt-cyg remove python3
apt-cyg install python3
```

Enfin, pour obtenir la commande `pip3.4` :
```
python3 -m ensurepip
```

Et je vous recommande chaudement de supprimer également les fichiers `/usr/bin/pip3.2` désormais inutilisable, et `/usr/bin/pip` dont l'usage peut porter à confusion.
