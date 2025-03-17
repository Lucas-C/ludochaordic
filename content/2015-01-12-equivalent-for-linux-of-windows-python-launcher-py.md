Title: Equivalent for Linux of Windows Python launcher 'py'
Date: 2015-01-12 19:01
Lang: en
Tags: lang:en, bash, python, pep, windows, launcher, shorthand, mailing-list, prog
Slug: equivalent-for-linux-of-windows-python-launcher-py
---
Under Windows, CPython is shipped with a [very useful `py` command](https://docs.python.org/3/using/windows.html#python-launcher-for-windows).

[PEP-397](https://www.python.org/dev/peps/pep-0397/) describes in details its behaviour, and its C implementation can be found [in the CPYthon Mercurial repository](https://hg.python.org/cpython/file/8b3c609f3f73/PC/launcher.c).

<img src="images/wwcb/IronMan_INeedIt.gif" alt="IronMan_INeedIt.gif" title="python -m antigravity">

There has already been a lenghty discussion [in the "python-ideas" mailing list](https://mail.python.org/pipermail/python-ideas/2014-April/thread.html#27633) to write a Linux equivalent. I agree with what Éric Araujo wrote, that there isn't really a need for such a tool under Linux.

But I find it useful to use a `py -3.4 -m pip install $pkg` or `py 27 $file` shorthand, and hence I wrote a basic bash script equivalent : <https://github.com/Lucas-C/linux_configuration/blob/master/bin/py>

**EDIT [2018/06/18]**: there is also [Brett Cannon python-launcher written in Rust](https://crates.io/crates/python-launcher)
