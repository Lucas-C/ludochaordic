Title: Command history in a Python 3 virtualenv
Date: 2016-06-30 11:06
Tags: lang:en, bash, python, history, virtualenv, bug, pew
Slug: en-command-history-in-a-python-3-virtualenv
---
Due to a [long standing bug](https://github.com/pypa/virtualenv/issues/355), no history file will be kept of the commands you enter in an interactive shell when using a Python 3 virtualenv.

I found out a simple workaround. Simply put the following in your `~/.pythonrc` :
```python
import atexit, os, readline, sys
if sys.version_info >= (3, 0) and hasattr(sys, 'real_prefix'): # in a VirtualEnv
    PYTHON_HISTORY_FILE = os.path.join(os.environ['HOME'], '.python_history')
    if os.path.exists(PYTHON_HISTORY_FILE):
        readline.read_history_file(PYTHON_HISTORY_FILE)
        atexit.register(readline.write_history_file, PYTHON_HISTORY_FILE)
```

`.pythonrc` files are loaded at startup by defining a `PYTHONSTARTUP` environment variable pointing to them. I prefer to load mine only when launching a REPL, but never when passing parameters to the `python` command (like script names), so I use the following function definion in my `.bashrc` :
```bash
python () {
    if [ "$#" -eq 0 ]; then
        PYTHONSTARTUP=~/.pythonrc $(type -P python)
    else
        $(type -P python) "$@"
    fi
}
```