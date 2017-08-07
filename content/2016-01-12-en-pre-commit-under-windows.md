Title: [EN] pre-commit under Windows
Date: 2016-01-12 19:01
Tags: bash, python, wget, windows, git, hooks, pre-commit, pip, cygwin, apt-cyg, lynx, pacman, msys2
Slug: en-pre-commit-under-windows
---
First, lets mention [Git Bash](//msysgit.github.com) (aka _msysgit_) : the old version was a PITA to extend with additional packages (e.g. adding common C libs like libxml), and the new one (renamed [Git for Windows](//git-for-windows.github.io)), is based on MSYS2, but does not include a package manager.

Hence, we were left with 2 alternatives, both very good :

- [Cygwin](//www.cygwin.com) (my personal favourite) and its great & simple package manager [apt-cyg](//github.com/transcode-open/apt-cyg). Make sure you use a recent enough Cygwin, with `$BASH_VERSION` at least 4.2 (because of [this bug](//github.com/transcode-open/apt-cyg/issues/71)). Then, there is how to install `apt-cyg` and the `pre-commit` command :
```
lynx -source rawgit.com/transcode-open/apt-cyg/v1/apt-cyg > apt-cyg
sudo install apt-cyg /usr/local/bin && rm apt-cyg
apt-cyg install wget

apt-cyg install git python gcc-g++ libxml2-devel libxslt-devel
curl --silent --show-error https://bootstrap.pypa.io/get-pip.py | python
pip install pre-commit
```

- [MSYS2](//msys2.github.io) and its built-in package manager `pacman` :

```
pacman -S git python gcc libxml2-devel libxslt-devel
curl --silent --show-error https://bootstrap.pypa.io/get-pip.py | python
pip install pre-commit
```

**EDIT [2016/02/11]**: sadly, Stephen Jungels transcode-open/apt-cyg has been subject to an [DMCA complaint](//github.com/github/dmca/blob/master/2016-01-26-apt-cyg.md). Incidentally, Github user [@svnpenn](//github.com/svnpenn) created a fork named [sage](//github.com/svnpenn/sage), but legal issues remain as can be observed in this [DMCA counter-claim](//github.com/github/dmca/blob/master/2016-01-27-apt-cyg-counternotice.md) & the sage project [issues](//github.com/svnpenn/sage/issues).