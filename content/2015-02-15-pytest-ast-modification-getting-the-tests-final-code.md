Title: Pytest AST-modification : getting the tests final code
Date: 2015-02-15 08:02
Lang: en
Tags: lang:en, python, unit-testing, ecovoit, pytest, ast, assert, assembly, parallelize, prog
Slug: pytest-ast-modification-getting-the-tests-final-code
---
[`Pytest`](http://pytest.org) is a very complete test framework for Python. I like how you can write a basic `unittest.TestCase` and the `py.test` test runner command will inject all its magic at runtime, without you having to directly  `import` anything: awesome separation of concerns.

This modularity comes at a cost though: `py.test` actually preprocess tests before running them, by parsing their [AST tree](//docs.python.org/2/library/ast.html) and replacing `assert` calls by custom exceptions "manually "raised. The final compiled `.pyc` binaries are then cached in a `__pycache__/` directory.

My curiosity got aroused by [this blog post from 2011](http://pybites.blogspot.fr/2011/07/behind-scenes-of-pytests-new-assertion.html) : wouldn't that be nice to peek into this process and check what the modified code look like exactly ?

I considered 2 solutions:

- either decompile the cached `.pyc` files, but I couldn't feed them to `uncompyle2` nor `pycdc` without raising bytecode format errors.
- take a glance at Pytest code base and find a way to invoke its custom AST-parsing method, then "AST-unparse" the resulting AST tree instead of compiling it down to bytecode.

This second solution revealed to be very easy to implement. I hesitated for a moment between two good-looking AST-unparser, namely [`astor`](https://github.com/berkerpeksag/astor) and [`astunparse`](https://github.com/simonpercivall/astunparse), and ended up with the following code:
```python
from _pytest.assertion.rewrite import rewrite_asserts
import ast, astunparse, sys

with open(sys.argv[1], 'r') as open_file:
    ast_tree = ast.parse(open_file.read())
rewrite_asserts(ast_tree)
print astunparse.unparse(ast_tree)
```

And that's it !
To test it, just write a dummy **stupid_test.py** file with:
```python
def dummy_test():
    assert False
```

And then `python pytest_rewrite.py stupid_test.py` :
```python
import __builtin__ as @py_builtins
import _pytest.assertion.rewrite as @pytest_ar

def dummy_test():
    if (not False):
        @py_format1 = (('' + 'assert %(py0)s') % {'py0': (@pytest_ar._saferepr(False) if (('False' in @py_builtins.locals()) or @pytest_ar._should_repr_global_name(False)) else 'False')})
        raise AssertionError(@pytest_ar._format_explanation(@py_format1))
```

<img src="images/wwcb/Mowgli-and-Kaa.jpg" alt="Mowgli hypnotized by Kaa">

Now, I want to conclude on a more nuanced tone: not everything is perfect in the Pytest world, and I have a few pain points to mention:

- Pytest terminal reports are rendered character by character, making it impossible to write log messages to stdout without messing everything
- Pytest wraps every module/class/object in your tests into [custom wrappers](//github.com/pytest-dev/pytest/blob/master/_pytest/python.py) and use generic callback hooks on at least 3 invocation levels : I had to scratch my head for some time to debug minor errors stacktraces and hack around it
- Pytest code base is very dense and not always following PEP code standards, making it very difficult to understand and contribute
- finally, I have a last minor complaint: when using `pytest-xdist` to parallelize tests, [you cannot write to _stdout_](//bitbucket.org/hpk42/pytest/issue/680/cannot-disable-capturing-with-dist). I guess it'd be difficult to collect the standard outputs of every process spawned by `pytest-xdist`, but it's still a PITA.
