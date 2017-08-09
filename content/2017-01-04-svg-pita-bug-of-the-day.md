Title: svg PITA bug of the day
Date: 2017-01-04 14:01
Tags: lang:en, bug, html, svg, href, codepen, angry, angularjs
Slug: svg-pita-bug-of-the-day
---
Today I've been struggling to understand why this does not work in Firefox, but is OK in Chrome:
```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <base href="/">
  </head>
  <body>
    <svg>
      <symbol id="pretty-circle">
        <circle cx="15" cy="15" r="10"/>
      </symbol>
      <use xlink:href="#pretty-circle"></use>
    </svg>
  </body>
</html>
```
Here is a [codepen snippet](http://codepen.io/anon/pen/WRNqxg) to test if your browser display a circle or not.

I found the answer here: http://stackoverflow.com/a/18265336/636849

Yes, that innocuous `<base>` tag is the culprit.

<img src="/lucas/wwcb/photos/angry-must-resist.jpeg">

Beware of this bug, as now with Angular 2 a `base` meta tag has to be there by default.