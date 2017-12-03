Title: Solarized mindmaps with Python and graphviz
Date: 2017-02-22 12:02
Tags: lang:en, solarized, mindmap, python, graphviz, prog
Slug: solarized-mindmaps-with-python-and-graphviz
---
This week I wrote [a small Python script](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/mindmaps/graphviz_mindmap.py), heavily inspired by [this Treemap plugin for Zim wiki](https://github.com/jaap-karssenberg/zim-wiki/wiki/TreeMap-plugin-(converted-Text2mindmap-custom-tool)), and using [Ethan Schoonover solarized palette](http://ethanschoonover.com/solarized), that can generate a mindmap from a simple indented text input like this:
<pre>Winter
    december
    january
    february
Spring
    march
    april
    may
Summer
    june
    july
    august
Autumn
    september
    october
    november
</pre>

The command: `./graphviz_mindmap.py seasons.txt`.

The results, with various `layout` parameters:

![default layout](images/2017/02/seasons_twopi.png)

![sfdp layout](images/2017/02/seasons_sfdp.png)

![dot layout](images/2017/02/seasons_dot.png)

Another, deeper, example:
<pre>Types of Chocolate
    Baking Chocolate
        contains nothing but chocolate liquor
    Cocoa Powder
        cocoa solids remain when most of the pressed into liquor.
    Chocolate liquor
        center(nib) of the cocoa bean, ground until liquifies, no alcohol.
    Milk Chocolate-
        contains 10% chocolate Liquor, most commonly eaten.
    White Chocolate
        contains no cocoa powder or chocolate liquor.
    Dutch-Pressed Cocoa
        has a darker color but milder chocolate flavor.
    Bittersweet Chocolate
        the darkest of eating chocolate liquor, has the highest %
        may contain extra cocoa butter
    Semi Sweet Chocolate
        often referred to as dark chocolate, 35-45% Chocolate liquor
</pre>

![default layout](images/2017/02/chocolates_twopi.png)

A last one:
<pre>The Bubonic Plague
    What is it?
        Some may know it as 'The Black Death'
        It is a disease that once hit Europe in the Middle Ages
        In just two years, 25 million people died of the plague. In ten years, the plague had killed over 1/3 of Europe's population.
    Religious beliefs
        Many people had thought that it was God punishing them for being wicked.
    How did it spread?
        Infected rats carried the disease.
        The Bubonic Plague started in Asia and then struck Africa and Europe.
    How did people react to this disease?
        People locked their doors to protect themselves from the awful disease.
        Others had burnt the hours filled with the dead and the sky was filled with ashes.
    Sarah Bernal 8AE
    1348-1349
</pre>

![default layout](images/2017/02/plague_twopi.png)
