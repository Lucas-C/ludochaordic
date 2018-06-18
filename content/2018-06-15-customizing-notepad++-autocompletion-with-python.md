Title: Customizing Notepad++ autocompletion with Python
Date: 2018-06-15 14:00
Tags: lang:en, python, vim, notepad++, pelican, blog, plugin, prog
Slug: customizing-notepad++-autocompletion-with-python
---

When [I migrated this blog to Pelican](https://chezsoi.org/lucas/blog/migration-du-blog-de-ghost-a-pelican.html),
I noted one thing that I missed from Ghost: tags autocompletion, to help reusing tags I already defined in other articles.

Because nowadays I mostly use Notepad++ or `vim` to write my blog posts,
I found out an easy solution that works for both: using a [Ctags](https://en.wikipedia.org/wiki/Ctags) file.

![Notepad++ logo](images/2018/06/notepad++_logo.jpg)

Quoting Wikipedia:

> Ctags is a programming tool that generates an index (or tag) file of names found in source and header files of various programming languages.
> These tags allow definitions to be quickly and easily located by a text editor or other utility.

First off, I wrote [a simple Pelican plugin](https://github.com/getpelican/pelican-plugins/pull/1038) to generate
a file containing all articles tags and following [the Ctags format spec](http://ctags.sourceforge.net/FORMAT).

`vim` natively supports Ctags, however Notepad++ does not.
I tried all [Notepad++ plugins](http://docs.notepad-plus-plus.org/index.php?title=Plugin_Central) that provide support for Ctags,
and while some work fine (`CCompletion` Ctags parser however is a bit picky / limited),
none really blended with Notepad++ native autocompletion as well as I wanted.

Then I discovered Dave Brotherstone awesome [PythonScript](https://github.com/bruderstein/PythonScript) plugin for Notepad++.

Once installed, the following short code snippet is enough to parse a Ctags file and trigger the editor autocompletion:
```
import os
ctags_filepath = os.path.join(os.path.dirname(notepad.getCurrentFilename()), 'tags')
if os.path.exists(ctags_filepath):
    with open(ctags_filepath) as ctags_file:
        ctags = set(line.split('\t')[0] for line in ctags_file.readlines() if not line.startswith('!'))
editor.autoCShow(0, ' '.join(sorted(ctags)))
```

You can for example bound this script to `CTRL+SHIFT+C` in `Settings > Shortcut Mapper > Plugins Commands > Run Previous Script`.
It will show a typical Notepad++/Scintilla autocompletion list, but based on the content of the `tags` file in the current file directory.

This script will also work if the `tags` file simply contains one word per line.

This PythonScript plugin can make Notepad++ really powerful,
able to perform IDE-style refactoring easily.

For example, one could combine it with code refactoring tools like [python-rope/rope](https://github.com/python-rope/rope), [PyCQA/redbaron](https://github.com/PyCQA/redbaron),
[google/pasta](https://github.com/google/pasta) or even code style autofixers like [ambv/black](https://github.com/ambv/black),
to modify the code you just selected in Notepad++ on a simple keystroke.

<style>
    article img {
        display: block;
        margin: 0 auto;
        max-height: 20rem;
    }
</style>
