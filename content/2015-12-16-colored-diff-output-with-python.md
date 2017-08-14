Title: Colored diff output with Python
Date: 2015-12-16 12:12
Tags: lang:en, python, color, colorama, diff, prog
Slug: colored-diff-output-with-python
---
Say you are generating a colored diff output with the standard `difflib` Python package:
```
diff = difflib.ndiff(file1_lines, file2_lines)
print('\n'.join(diff))
```

Now, I'll show you how to write a simple `color_diff` function that you can use to color your diff like this:
```
diff = difflib.ndiff(file1_lines, file2_lines)
diff = color_diff(diff)
print('\n'.join(diff))
```

Here is the code:
```
try:
    from colorama import Fore, Back, Style, init
    init()
except ImportError:  # fallback so that the imported classes always exist
    class ColorFallback():
        __getattr__ = lambda self, name: ''
    Fore = Back = Style = ColorFallback()

def color_diff(diff):
    for line in diff:
        if line.startswith('+'):
            yield Fore.GREEN + line + Fore.RESET
        elif line.startswith('-'):
            yield Fore.RED + line + Fore.RESET
        elif line.startswith('^'):
            yield Fore.BLUE + line + Fore.RESET
        else:
            yield line
```
