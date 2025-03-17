Title: A Python iterator to list all UTF8 characters
Date: 2016-04-14 12:04
Lang: en
Tags: lang:en, python, iteration, utf8, character, newline, line-feed, ascii, code-point, prog
Slug: a-python-iterator-to-list-all-utf8-characters
---
Last week, I made up a basic TCP server in Python, to receive log lines. To split log lines, I used the ascii line feed ascii character : \n aka 0xa in hexadecimal.

But then I wondered : could this byte appear elsewhere in the UTF8-encoded strings of text I was sending ?

To find out, I wrote a [small Python script](//github.com/Lucas-C/linux_configuration/blob/master/languages/python/utf8_iterator.py) that list all possible UTF8 characters. Here is its output:
```
$ time python3 utf8_iterator.py
4-bytes-max UTF8 potential characters count 2164864
4-bytes-max UTF8 decodable characters count 1112064
UTF8 characters containing the 0x0a newline byte: [b'\n']

real    0m8.003s
```

So, there is no other UTF8 character containing the 0x0a byte !
In fact, all 128 ASCII characters are encoded in the same way in UTF8. More important: **the bytes corresponding to the 128 ASCII characters never appear elsewhere in UTF8**.

Nice property isn't it ?
Now go get a glance on the [Wikipedia page](//en.wikipedia.org/wiki/UTF-8#History) to find out about this encoding intersting history.

<a href="//en.wikipedia.org/wiki/Office_Space"><img alt="Animation tirée du film Office Space" src="images/wwcb/YeahThanks-IfWeCouldGetbackToWorkNowThatdBeGreat.jpg"></a>

The Python script is certainly not the fastest for the task, but simple enough for my need, and could be useful to write tests for Python code processing byte strings: it can generate all the 1112064 valid UTF8 code points, plus some extra invalid ones.
