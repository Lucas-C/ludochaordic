Title: Useful short Python decorator to convert generators into lists
Date: 2016-02-11 12:02
Tags: lang:en, python, recipe, decorator, generators, list, vowels, yield
Slug: useful-short-python-decorator-to-convert-generators-into-lists
---
Python generators are awesome. Why ?

- their syntax is simple an concise
- they lazily generate values and hence are very memory efficient
- bonus point: since Python 3 you can chain them with `yield from`

Their drawback ? They can be iterated only once, and they hide the iterable length.

I took an habit of making a generator of every function I write that generates an iterable. Basically, it simply means using `yield`:
```
def list_vowels_before(char):
    for vowel in ('a', 'e', 'i', 'o', 'u', 'y'):
        if vowel >= char:
            return
        yield vowel
```

But now, if I want an iterable that I can iterate several times, I need to convert to a list the generator returned by this function **in every piece of code that invoke it**:
```
selected_vowels = list(list_vowels_before('t'))
```

But this isn't very good in terms of code readibility & maintainability: if one use this function but forget to do the conversion, the resulting object won't behave as expected. E.g. a simple conditional that test if the list is empty will evaluate to `True` :
```
selected_vowels = list_vowels_before('a')
if selected_vowels:
	print('AMAZING: there are vowels BEFORE the letter "a" !!')
```

In case you want to use the generators syntax, but ensure that a function always return a list, here is a simple recipe you can use:

```
# This @decorator is totally optional, but it is a recommended best practice
try:  # We try to import GrahamDumpleton/wrapt if available
	from wrapt import decorator
except ImportError:  # fallback to the standard, less complete equivalent
	from functools import wraps as decorator

@decorator
def aslist(generator):
    "Function decorator to transform a generator into a list"
    def wrapper(*args, **kwargs):
        return list(generator(*args, **kwargs))
    return wrapper
```

And now you just have to add a single line of code to your previously defined function:
```
@aslist
def list_vowels_before(char):
    for vowel in ('a', 'e', 'i', 'o', 'u', 'y'):
        if vowel >= char:
            return
        yield vowel
        
selected_vowels = list_vowels_before('a')
if selected_vowels:
	print('This will never be printed ;)')
```
