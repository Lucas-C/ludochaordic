Title: Numberphile question 6
Date: 2016-08-30 05:08
Tags: lang:en, maths
Slug: numberphile-question-6
Status: draft
---
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=AM_HTMLorMML,Safe"></script>

A couple of weeks ago, I watched the latest [Numberphile](http://www.numberphile.com) video in which a very interesting Maths problem was described :

<iframe width="800" height="450" src="https://www.youtube.com/embed/Y30VF3cSIYQ" allowfullscreen></iframe>
<br>

Given how much emphasis Simon Pampena put on the problem difficulty in this video, I have to admit I'm quite proud to have found a solution :)
Alright, teenage mathematicians that tackled this enigma were only given an hour and a half in average to solve it, but it only took me a few hours ! ^^

The problem was given in the International Mathematical Olympiads of 1988 in this form:

\`"Given " (a, b) in NN² " such as " ab+1 " divides " a²+b² ","\`
\`"prove that " (a²+b²)/(ab+1) " is a square."\`

As soon as I saw the question, I stopped the video and started scribbling.
Soon I realized I needed example values for **a & b**, so I wrote the following Python script:
```python
for a in range(1, 10000):
    for b in range(a, 10000):
        if (a**2 + b**2) % (a*b + 1) == 0:
            print('a=', a, 'b=', b, 'g²=', (a**2 + b**2) // (a*b + 1))
```

This gave me only 31 solutions. Some of the most interesting ones:
```
a= 1 b= 1 g²= 1
a= 2 b= 8 g²= 4
a= 8 b= 30 g²= 4
```

I was suspecting a trick in the question: maybe there were simply NO such couple of integers satisfying the premises of the demonstration (the integral ratio) ?
But such couples existed indeed. And while rares, they all satisfied the problem strange property: the integral ratio was always the square of an integer.

I started looking for a pattern between _(a, b)_ and that square, **g²**. Thanks to this Python script, I quickly got a hint to the solution: **_g_ was the greatest common denominator of _a & b_**.
Lets check this hypothesis programmatically:
```python
from fractions import gcd
for a in range(1, 10000):
    for b in range(a, 10000):
        if (a**2 + b**2) % (a*b + 1) == 0:
            print('a=', a, 'b=', b, 'g²=', (a**2 + b**2) // (a*b + 1), 'gcd(a, b)²=', gcd(a, b)**2)
```
Outputs:
```
a= 1 b= 1 g²= 1 gcd(a, b)²= 1
a= 2 b= 8 g²= 4 gcd(a, b)²= 4
a= 8 b= 30 g²= 4 gcd(a, b)²= 4
```
Sounds promising !

Now lets prove this.

<hr>

\`"Given " (a, b) in NN² " such as " ab+1 " divides " a²+b² " (1),"\`
\`"Lets define " g = gcd(a, b) "."\`
\`g² " divides " a² " and " b² " and hence also divides " a² + b² "."\`
\`"Then given (1) :" EE K in NN " such as " a²+b² = Kg²(ab+1) "."\`
\`"By definition of " g " : " gcd(g, ab + 1) = 1 " and hence " gcd(g², ab + 1) = 1 "."\`
\`"Consequently " K " divides " a²+b² "(2) ."\`

<style>
article iframe { display: block; margin: 1rem auto; }
</style>
