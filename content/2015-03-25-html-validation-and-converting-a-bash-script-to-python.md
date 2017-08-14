Title: HTML validation and converting a shell script to Python
Date: 2015-03-25 21:03
Tags: lang:en, bash, script, shell, grep, stream, python, wget, sed, html, vnu, sh-py, jar, prog
Slug: html-validation-and-converting-a-bash-script-to-python
---
<img src="/lucas/wwcb/photos/AngryShouting_LionKing.gif" alt="">

### Die shell script, DIE !

In this post, I'll show how easy it ease to convert fragile shell scripts to Python scripts, using [sh.py](http://amoffat.github.io/sh/).
I'll use as an example a simple script to check your HTML code from the command-line, using the [W3C validator](http://validator.w3.org/).

Now you ask me, why the hell would Python be better than shell scripts ?
I love the simplicty of a short Bash script. But they are simply too brittle to be safely used in production:

- shell scripts miss some very useful features: exceptions and try/catch blocks, stack traces displayed in case of failure, classes and modules, built-in dictionaries, assertions, list-comprehensions...
- Python has more built-in static checks: uninitialized variables and undefined functions can be detected before execution, and horrific syntax errors like `foo () { = 42; }` (this is valid Bash code !) are not tolerated
- Python has a more easy to read & understand syntax, and Python code is generally easier to maintain
- Python comes with "batteries included", a HUGE community and has tens of thousands of PyPI packages, so you don't need to reinvent the wheel. On the other end, c ode reuse among shell scripts tends to be difficult.
- many Unix utility commands (awk, grep, sed...) can be replaced by simple Python code, meaning less commands invocations and faster execution
- finally, shell scripts can cause [this kind of issue](//github.com/valvesoftware/steam-for-linux/issues/3671)

To begin with, there is our initial Bash script:

```
#!/usr/bin/env bash

# USAGE: ./vnu_html_checker.sh $file.html
#    OR: ./vnu_html_checker.sh < $file.html

set -o pipefail -o errexit -o nounset

VNU_GITHUB=https://github.com/validator/validator
VNU_VERSION=20150207

download_vnu_jar () {
    local zip_filename=vnu-$VNU_VERSION.jar.zip
    wget $VNU_GITHUB/releases/download/$VNU_VERSION/$zip_filename
    unzip $zip_filename
    mv vnu/vnu.jar .
    rm -r vnu/ $zip_filename
}

filter_out_XUAcompat_line () {  # seen as an error by VNU
    grep -vF 'meta http-equiv="X-UA-Compatible"'
}

filter_out_mustaches () {
    sed -e 's/{[{%][^{}]\+[%}]}/DUMMY_MUSTACHE/g'
}

if ! [ -e vnu.jar ]; then
    download_vnu_jar
fi

cat "$@" | filter_out_XUAcompat_line \
		 | filter_out_mustaches \
         | java -jar vnu.jar -
```

To paraphrase the code, this script retrieves the [`vnu.jar` validator from Github](//github.com/validator/validator) on the first run, and use it to check the HTML code passed by standard input or filename.
Hence, the script downloads and uncompresses a ZIP archive file. Moreover, it filters out from the HTML file any [mustache](//mustache.github.io) string pattern.

Now, compare it to the following equivalent Python code:
```
#!/usr/bin/env python2.7

# INSTALL: python2.7 -m pip install --user sh
#   USAGE: ./vnu_html_checker.py $file.html
#      OR: ./vnu_html_checker.py < $file.html

import os.path, re  
from sys import argv, exit, stderr, stdin
import sh
sh = sh(_err=stderr)

VNU_GITHUB = 'https://github.com/validator/validator'  
VNU_VERSION = '20150207'

def download_vnu_jar():  
    zip_filename = 'vnu-{}.jar.zip'.format(VNU_VERSION)
    download_url = '{}/releases/download/{}/{}'.format(
            VNU_GITHUB, VNU_VERSION, zip_filename)
    sh.wget(download_url)
    sh.unzip(zip_filename)
    sh.mv('vnu/vnu.jar', '.')
    sh.rm('-r', 'vnu/', zip_filename)

def filter_out_xuacompat_line(input_pipe):  # seen as an error by VNU  
    return (l for l in input_pipe if 'meta http-equiv="X-UA-Compatible"' not in l)

def filter_out_mustaches(input_pipe):  
    return (re.sub('{[{%][^{}]+[%}]}', 'DUMMY_MUSTACHE', l) for l in input_pipe)

if not os.path.isfile('vnu.jar'):  
    download_vnu_jar()

if len(argv) > 1:  
    pipe = sh.cat(argv[1], _iter=True)
else:  
    pipe = sh.cat(_in=stdin, _iter=True)
pipe = filter_out_xuacompat_line(pipe)  
pipe = filter_out_mustaches(pipe)
parsed_html = ''.join(pipe).encode('utf8')
try:  
    sh.java('-jar', 'vnu.jar', '-', _in=parsed_html)
except sh.ErrorReturnCode as error:  
    exit(error.exit_code)
```

First observation: the code is definitively lengthier. 88% more characters exactly.
But look at the benefits !

- the script keeps its general structure: pipe-based, functional, applying simple filters on the input stream
- all commands are checked at import time so they are guaranteed to exist: `java`, `wget`... By the way, you are not limited to Linux _coreutils_, you can use **any** command on your system.
- **try/catch blocks** !!!
- in case of failure, you can inspect the objects at runtime with `pdb`
- finally, two commands invocation (`grep` and `awk`) have been replaced by native Python inline generators. I prefer avoiding unnecessary command calls, but in the process of migrating this script I initially sticked with them:

`return grep('-vF', 'meta http-equiv="X-UA-Compatible"', _in=input_pipe, _iter=True)`

`return sed('-e' 's/{[{%][^{}]\+[%}]}/DUMMY_MUSTACHE/g', _in=input_pipe, _iter=True)`

I hope I convinced you: next time you write a script, **think about Python** !

But BEWARE, even Python scripts can become [spaghetti code monsters](/lucas/wwcb/photos/Ill_just_write_a_quick_script...-catacrac.net.png).

**EDIT[17/08/2015]** : as long as the interpreter is installed on your system, you can run a standalone Python script just like a Bash script and easily benefit from the THOUSANDS libraries in Pypy, including `sh.py`, by invoking `pip` FROM YOUR SCRIPT !

```
import pip
pip.main(['install', '--user', 'retrying==1.3.3', 'requests==2.7.0' 'sh==1.11'])
# if you're using the logging module & a pip version newer or equal to 6.0, you'll need this bugfix (cf. https://github.com/pypa/pip/issues/3043) :
logging.root.handlers = []

import requests
from retrying import retry
from sh import grep, sed
```
