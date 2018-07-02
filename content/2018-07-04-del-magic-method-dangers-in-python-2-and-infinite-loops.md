Title: __del__ magic method dangers in Python 2 and infinite loops
Date: 2018-07-04 9:00
Tags: lang:en, python, gotcha, recursion, infinite-loop, oui.sncf, garbage-collection, prog
Slug: del-magic-method-dangers-in-python-2-and-infinite-loops
---
Yesterday I've stumbled upon a very surprising bug in some Python 2 code,
related to the use of the `__del__` method in a vendor library we employ at work.

Here is some minimal code that reproduces the issue I met:
```python
class MyClass:
    def __init__(self):
        raise RuntimeError('Woops')

    def __del__(self):
        try:
            raise_recursion_error()
        except RuntimeError:
            print('Recursion error caught')

def raise_recursion_error():
    raise_recursion_error()

MyClass()
```

What do you think will happen ? Take a moment to make a guess.

---

If you execute this code, you will witness a never-ending repetition of the `Recursion error caught` message in your terminal.

Interestingly, if we replace the recursion error by a simple `RuntimeError`, the problem vanishes !

I don't quite understand why this recursion error, despite being caught, causes this strange behaviour.
Somehow I think the `try` / `catch` does not "entirely" suppress the exception,
and that it still bubbles up "enough" to cause the Python interpreter to call `__del__` again.

![A guy keeps opening a Matryoshka that seems to never end](/lucas/wwcb/photos/Infinite_loop_Matryoshka.gif)

If you remove the `try` / `catch` around `raise_recursion_error()`, you'll get the same behaviour, with a different message:
```
Exception RuntimeError: 'maximum recursion depth exceeded' in <bound method MyClass.__del__ of <__main__.MyClass instance at 0x6ffffebd758>> ignored
```

This kind of "exception ignored" messages disappeared in Python 3, which handles this case very smoothly, by halting immediately and displaying this:
```
Traceback (most recent call last):
  File "del_recurse_infinite_loop.py", line 36, in <module>
    MyClass()
  File "del_recurse_infinite_loop.py", line 24, in __init__
    raise RuntimeError('Woops')
RuntimeError: Woops
Recursion error caught
```

In the real world code where I saw this behaviour, the recursion error was due to a `__getattr__` method calling itself.
The following class presents the same behaviour:

```python
class MyClass:
    def __init__(self):
        raise RuntimeError('Woops')

    def __del__(self):
        try:
            self.foo()
        except RuntimeError:
            print('Recursion error caught')

    def __getattr__(self, name):
        return self.uninitialized_attribute
```

Not also that in its original form, I wasn't even able to stop the process with **CTRL+C** !
The `KeyboardInterrupt` exceptions were ignored.

My key takeaways from this painful deep dive:

- Python 3 is safer than Python 2
- recursion error are a special breed of `RuntimeError`, and are sometimes handled differently in Python 2
(even if they are not identified by a named subclass)
- a typo in the code of a `__getattr__` method can lead to infinite recursion
- stay away from `__del__`

I'm not the first to warn about the `__del__` method by the way:

- [Python Gotchas 1: __del__ is not the opposite of __init__](http://www.algorithm.co.il/blogs/programming/python/python-gotchas-1-__del__-is-not-the-opposite-of-__init__/)
- [Python destructor drawbacks](http://www.andy-pearce.com/blog/posts/2013/Apr/python-destructor-drawbacks/)
- [An Interesting Fact About The Python Garbage Collector](https://www.holger-peters.de/an-interesting-fact-about-the-python-garbage-collector.html)

This last one even mentions that it can generate memory leaks.

Let me know in the comments section if ever you have more information to explain this strange quirk !
