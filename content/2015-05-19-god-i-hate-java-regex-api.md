Title: God I hate Java Regex API
Date: 2015-05-19 16:05
Lang: en
Tags: lang:en, python, java, regexp, api, matcher, prog
Slug: god-i-hate-java-regex-api
---
Pourquoi, mais pourquoi faut-il **3 lignes** en Java pour juste extraire un groupe d'une expression régulière qui "match" ???

```
Matcher matcher = Pattern.compile("o?k(b|i)s+").matcher("kiss");
matcher.matches();
assert matcher.group(1) == "i";
```

<img alt="Angry face" src="images/wwcb/rage-comic-angry.jpg">

En Python:

```
assert re.match("o?k(b|i)s+", "kiss").group(1) == "i";
```

La cerise sur le gateau: il existe en Java une méthode `.groupCount()` qui retourne ["le nombre de groupes de capture dans Pattern associé au Matcher"](http://docs.oracle.com/javase/7/docs/api/java/util/regex/Matcher.html#groupCount()).
**Mais pourquoi diable est-ce que cette méthode est définie dans la classe `Matcher` et PAS dans la classe `Pattern` ???**

<img alt="Aaaargh" src="images/wwcb/Aaaargh.gif">

Voilà, c'était le coup de gueule du jour. Même en Javascript l'API est plus pratique ! Alors OK 2 lignes de plus c'est pas la fin du monde, mais je trouve que ça illustre bien la différence entre ces deux langages en terme d'élégance. Et comme on dit: "The Devil is in the detail"...
