Title: gdb Python macros
Date: 2014-11-07 11:11
Tags: lang:en, python, gdb, configuration, rc, prompt, color, history, ptrace, symbol, macro, pgrep, debug
Slug: en-gdb-python-macros
---
This post aims to introduce a very useful tool to debug low-level issues in Python, how to enhance it and finally how to solve two annoying common problems.

### 1. Debugging Python with gdb
All the basics are there : https://wiki.python.org/moin/DebuggingWithGdb

Tl;dr :
```
gdb -p $(pgrep -f your_running_python_program_name)
```

### 2. Installing the macros for Python
<q>A set of GDB macros are distributed with Python that aid in debugging the Python process.</q> (from: https://wiki.python.org/moin/DebuggingWithGdb#GDB_Macros).

One-liner to install those macros:
```
curl --silent http://svn.python.org/projects/python/trunk/Misc/gdbinit >> ~/.gdbinit
```

There is a minor fix to the `lineno` macro to make:
```
sed -i 's/printf "%d", $__li/printf "%d", $__li + 1/' ~/.gdbinit
```

Usage example taken from the comments:

<blockquote>
<pre><code>(gdb) pyo apyobjectptr
&lt;module 'foobar' (built-in)&gt;
refcounts: 1
address    : 84a7a2c
$1 = void
</code></pre>
Quoted from: <cite><a href="http://svn.python.org/projects/python/trunk/Misc/gdbinit">Python SVN Misc/.gdbinit</a></cite>
</blockquote><br>

Some other useful macros: `pystack`, `printframe`, `pylocals`.
List them all with: `grep define ~/.gdbinit`.

### 3. Persistent history & colored prompt
The following command will append some lines to your _~/.gdbinit_ configuration file in order to keep a persistent history between your gdb sessions, and to set a very useful colored prompt:

```
cat <<END >> ~/.gdbinit

# Custom configuration by USER=$USER
## Persistent history:
set history save
set history filename ~/.gdb_history
## Colored prompt:
set prompt \001\033[1;32m\002(gdb)\001\033[0m\002\040
END
```

All the credit for this trick goes to [Peter Jay Salzman](http://web.archive.org/web/20140831120136/http://dirac.org/linux/gdb/03-Initialization,_Listing,_And_Running.php#the%3Ctt%3E.gdbinit%3C/tt%3Efile).
Here is also a more complete improved _.gdbinit_ : http://reverse.put.as/gdbinit/.

### 4. Solving: 'ptrace: Operation not permitted'

DO **NOT** SET THE SUID/SGID BIT :
<pre><code><del style="text-decoration: line-through;">sudo chmod +s /usr/bin/gdb
</del></pre></code>

As explained in the comments (thanks to Romain Geissler), this solution I initially recommended actually creates a **security vulnerability**.

A better solution looks to be :
```
echo 0 > /proc/sys/kernel/yama/ptrace_scope # to execute as root
```

Or setting `kernel.yama.ptrace_scope = 0` in _/etc/sysctl.d/10-ptrace.conf_.

### 5. Solving: 'No symbol "co" in current context'
This one is trickier. It's a known issue described in https://wiki.python.org/moin/DebuggingWithGdb#GDB_Macros. The recommended solution is to <q>Recompile python with make CFLAGS=-g -fno-inline -fno-strict-aliasing</q> (the alternative patch did not work for me).

Yeah, I know, *SIGH*...

But it's in fact not so difficult to built a stand-alone python interpreter:

```
dbg_py_v=2.7.8; dbg_py=Python-$dbg_py_v
mkdir /opt; cd /opt
curl -L http://python.org/ftp/python/$dbg_py_v/$dbg_py.tar.xz | tar xJvf -
cd $dbg_py
./configure --prefix=/usr/local --enable-unicode=ucs4 --disable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make -j3 "CFLAGS=-g -fno-inline -fno-strict-aliasing"
```

Then simply:
```
export PYTHONPATH=... # can be extracted from the original script with print('\n'.join(sys.path))
/opt/$dbg_py/python your_python_program
```

And no more "undefined symbol" error message in `gdb` !

<hr>

**EDIT**: Actually, if your `gdb` version has been compiled with python support (`gdb --batch --quiet -ex 'show configuration' | grep with-python`), no need to download any _.gdbinit_ file !
You can replace all those macros definition by this single line in your _.gdbinit_ (after manually replacing the _$dbg\_py_ variable) :
```
add-auto-load-safe-path /opt/$dbg_py/python-gdb.py
```

You now have access to all the following commands:

* py-bt
* py-list
* py-down / py-up
* py-locals
* py-print

On the other hand, the latest version of the _gdbinit_ file on the new Mercurial repository doesn't seem to work: https://hg.python.org/cpython/raw-file/default/Misc/gdbinit.
I get a _'No symbol "\_PyUnicode\_AsString" in current context.'_ error message.

**EDIT (2016/04/15):** a more recent article on the subject : http://podoliaka.org/2016/04/10/debugging-cpython-gdb/

The following commands taken from this article helped me once:
```
yum install python33-python-debuginfo glibc-debuginfo
# from base-debuginfo repository - can also be installed with: debuginfo-install ...
```

In `gdb` :
```
source /usr/lib/debug/opt/rh/python33/root/usr/lib64/libpython3.3m.so.1.0.debug-gdb.py
```