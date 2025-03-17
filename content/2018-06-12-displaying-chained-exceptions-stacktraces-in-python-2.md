Title: Displaying chained exceptions stacktraces in Python 2
Date: 2018-06-12 14:00
Lang: en
Tags: lang:en, python, backward-compatibility, exception, stacktrace, mysql, oui.sncf, prog
Slug: displaying-chained-exceptions-stacktraces-in-python-2
---

At work we have a component not yet migrated to Python 3,
and we recently had some difficulties diagnosing a problem with the MySQL connector.

Because we were catching the `mysql.connector.errors.Error` and raising a custom exception,
we were loosing the underlying stacktrace and hence couldn't troubleshoot the root cause of the issue.

![Grandman says: Program exit with error -11! But where is the stacktrace ?](images/2018/06/program-exit-with-11-but-where-is-the-stacktrace.jpg)

Raising custom exceptions isn't the issue here :
this practice ensure you have a proper [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns),
meaning in practice your code do not raise exceptions coming from third-party libraries <sup><a id="ref1" href="javascript:;" onclick="document.location.hash='fn1';">[1]</a></sup>
and that you control what kind of exception your class or module can raise,
while adding useful contextual information in the new custom one raised.

No, the real solution here is to display the full stacktrace.

![Scene from the film Inception : That's not enough, we have to go deeper](images/2018/06/inception-thats-not-enough-we-have-to-go-deeper.png)

In this article, I'll show how to handle such situation in Python 2.

---

Let's take this piece of Python 3 code :
```
class CustomException(Exception):
    pass

try:
    raise ValueError('Wooops')
except ValueError as err:
    raise CustomException('Badaboum') from err
```

If you execute it, you'll get this output :
```
Traceback (most recent call last):
  File "test_reraise_py3.py", line 5, in <module>
    raise ValueError('Wooops')
ValueError: Wooops

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "test_reraise_py3.py", line 7, in <module>
    raise CustomException('Badaboum') from err
__main__.CustomException: Badaboum
```

Very handy !

In fact, this behaviour comes from [PEP 3134](https://www.python.org/dev/peps/pep-3134/).

But in Python 2, there is no `raise ... from ...` construct.

Two packages (at least) provide a backward compatibile workaround :

- [six](https://pypi.org/project/six/), but the implementation is [empty](https://github.com/benjaminp/six/blob/master/six.py#L736)
- [future](https://pypi.org/project/future/), bringing more interesting [code](https://github.com/PythonCharmers/python-future/blob/master/src/future/utils/__init__.py#L422)

What happens if we use the function they provide ?
```
from future.utils import raise_from

class CustomException(Exception):
    pass

try:
    raise ValueError('Wooops')
except ValueError as err:
    raise_from(CustomException('Badaboum'), err)
```

We get this output:
```
Traceback (most recent call last):
  File "test_reraise_py2.py", line 10, in <module>
    raise_from(CustomException('Badaboum'), err)
  File "/home/lucas_cimon/.local/share/virtualenvs/infralib-py2/lib/python2.7/site-packages/future/utils/__init__.py", line 454, in raise_from
    raise e
__main__.CustomException: Badaboum
```

Hmm... Quite frustrating !

Why that ?

The answer lies in the PEP mentioned above :

> In the traceback module, the `format_exception`, `print_exception`, `print_exc`, and `print_last` functions will be updated to accept an optional `chain` argument, `True` by default.
> When this argument is `True`, these functions will format or display the entire chain of exceptions as just described.
> When it is `False`, these functions will format or display only the outermost exception.

What this means is that, with the `future.utils.raise_from` implementation, we miss 2 things :

- while `__cause__` & `__context__ ` attributes are already set, the `__traceback__` one isn't
- the code that display the _tracebacks_ should use those attributes

For the first issue, you can use the patched version of `raise_from` in [this pull request](https://github.com/PythonCharmers/python-future/pull/341).

For the second one, we cannot safely modify the _builtin_ standard `format_exception` / `print_exception` / `print_exc` / `print_last` functions.
A workaround is to define a `__str__` method on your exceptions, as follows:
```
class CustomException(Exception):
    def __str__(self):
        out = Exception.__str__(self)
        if hasattr(self, '__cause__') and self.__cause__ and hasattr(self.__cause__, '__traceback__') and self.__cause__.__traceback__:
            out += '\n\nThe above exception was the direct cause of the following exception:\n\n'
            out += ''.join(traceback.format_tb(self.__cause__.__traceback__) + ['{}: {}'.format(self.__cause__.__class__.__name__, self.__cause__)])
        return out
```

With those 2 fixes, there is the stacktrace we get when executing our original code using `raise_from` in Python 2 :
```
Traceback (most recent call last):
  File "test_reraise_py2.py", line 45, in <module>
    raise_from(CustomException('Badaboum'), err)
  File "test_reraise_py2.py", line 33, in raise_from
    raise e
__main__.CustomException: Badaboum

The above exception was the direct cause of the following exception:

  File "test_reraise_py2.py", line 43, in <module>
    raise ValueError('Wooops')
ValueError: Wooops
```

---

<a id="fn1" href="javascript:;" onclick="document.location.hash='ref1';">1.</a> Bubbling up external libraries exceptions isn't always a bad practice,
especially for critical ones. But if your code uses various libs that all can raise very common and different exceptions,
this will force the users of your code to `import` all those exceptions systematically and is a clear violation of S.o.C.

<style>
article img { max-height: 20rem; }
</style>
