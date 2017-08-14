Title: Python 3 non consistent set & dict iteration gotcha
Date: 2014-12-08 19:12
Tags: lang:en, python, dict, security, perl, hash, iteration, gotcha, backward-compatibility, set, ministat, csvstat, prog
Slug: python-3-non-consistent-set-dict-iteration-gotcha
---
Consider the following Python expression:
```python
print("".join(set("ABCDE")))
```

What do you think it produces ?

<mark>Not necessarily "ABCDE".</mark>
Right, but you would expect the result to be consistent, isn't it ?

```bash
$ for i in {1..3}; do python2.7 -c 'print("".join(set("ABCDE")))'; done
ACBED
ACBED
ACBED
```

Great !

...

But with Python 3 :

```bash
$ for i in {1..3}; do python3.4 -c 'print("".join(set("ABCDE")))'; done
DECAB
CDBEA
DBACE
```

WHY ???

I found the answer in [this StackOverflow answer](http://stackoverflow.com/a/14959001/636849) :

<blockquote>This is the result of a security fix from 2012, which was enabled by default in Python 3.3. [...]
Hash randomization causes the iteration order of dicts and sets to be unpredictable and differ across Python runs.</blockquote>

<img src="/lucas/wwcb/photos/ACourtDArgument.gif" alt="[A court d'argument]" title="Fireflyyyyy !">


**EDIT [9/12/2014]** by curiosity, I checked if the hashes are uniformly distributed :
```bash
$ for i in {1..10000}; do python3.4 -c 'print("".join(set("ABCDE")))'; done > python3_set_iteration_abcde_10000
$ csvstat -H python3_set_iteration_abcde_10000
        Unique values: 120
        5 most frequent values:
                ABCDE:  317
                EABCD:  195
                BCDEA:  192
                BACDE:  192
                CDEAB:  165
```

Conclusion : all 120 possible ordering are generated, but the "ABCDE" ordering appears twice as often as any other.

And finally a minimalist terminal visualization of the distribution, using [`ministat`](https://github.com/thorduri/ministat) and a perl one-liner to convert the "ABCDE" strings into integers :
```
$ perl -ne 'if(!exists($s{$_})) {$s{$_}=scalar keys %s} print "$s{$_}\n"' python3_set_iteration_abcde_10000 | ministat -H 0.05 -w 60
x <stdin>
+------------------------------------------------------------+
|                       x                                    |
|                       x                                    |
|                       x                                    |
|                       x                                    |
|                       x                                    |
|                       x                                    |
|                       x         x                          |
|                       x         x                          |
| xx                    x         x                          |
| xx    x        x      x         x           x              |
| xx    x        x    x x         x           x              |
| xx    x        x x  xxx         x           xx             |
|xxx  x x x      x x  xxxxx x    xx x  xx     xx             |
|xxx xx x x  x   x xxxxxxxx x    xxxx  xx  x  xx  x    x  x  |
|xxxxxx x x  x x xxxxxxxxxxxx x  xxxx xxxx x xxx  x    x xx  |
|xxxxxxxxxxx xxx xxxxxxxxxxxx x xxxxx xxxxxxxxxx  x    xxxx  |
|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxxxx xxxxxxxxxxx xxxx xxxx  |
|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|           |--------------M-A---------------|               |
+------------------------------------------------------------+
    N       Min      Max      Median      Avg      Stddev
x 10000      0       119        53      55.4782   33.728675
```

(the graph is slightly skewed here because of the 60 characters width, but it follows the "x2 more frequent" initial observation if you use a 120 characters width)
