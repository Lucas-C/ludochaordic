Title: Server-less reveal.js slides
Date: 2016-10-12 11:10
Tags: lang:en, reveal-js, bash, http, local-server, slides, script
Slug: en-server-less-reveal-js-slides
---
I love [reveal.js](http://lab.hakim.se/reveal-js). I've been using it for years. But the other day, I was badly bitten by its requirement on a local HTTP server.

What happenned was that I was invited to make a short presentation in a youth and cultural center. I had prepared some slides with reveal.js, but once in their computer room, I realized a firewall was installed on each and every computer there, blocking any attempt to launch a simple local server with `python -m http.server` or a simple [Mongoose server](https://www.cesanta.com/products/binary). And no one had the admin rights over this firewall !

![](/lucas/wwcb/photos/daffy_tree_slam.gif)

There is currently [no](https://github.com/hakimel/reveal.js/issues/610) [plan](https://github.com/hakimel/reveal.js/issues/673) from the devs behind reveal.js to get rid of this requirement. Hence I developed a workaround !

With the markdown plugin, a typical usage of reveal.js looks like this (taken from their [base index.html](https://github.com/hakimel/reveal.js/blob/master/index.html)) :
```
<div class="reveal">
  <div class="slides">
    <section data-markdown="MySlides.md" data-separator="^\n\n\n" data-separator-vertical="^\n\n" data-notes="^Note:" data-charset="utf-8"></section>
  </div>
</div>
<script src="js/reveal.js"></script>
<script>
  Reveal.initialize({
    ...
    dependencies: [
      { src: 'plugin/markdown/marked.js' },
      { src: 'plugin/markdown/markdown.js' },
      ...
  });
</script>
```

The requirement for a local HTTP server actually comes from the [markdown plugin that performs an AJAX request](https://github.com/hakimel/reveal.js/blob/master/plugin/markdown/markdown.js#L222) to retrieve `MySlides.md`.

Hence, my idea for a workaround : convert `MySlides.md` into a `MySlides.js` script, so that no AJAX is needed any more !

Here is a 30-lines Bash script that does exactly that : [`reveal_md2js.sh`](https://github.com/Lucas-C/linux_configuration/blob/master/bin/reveal_md2js.sh)

In our exemple, you would just use it like this :

    ./reveal_md2js.sh MySlides.md
    MySlides.js has been successfully generated

Then, in your `index.html`, just replace the line :

    <section data-markdown="MySlides.md" ...></section>

by :

    <script src="MySlides.js" ...></script>

And TADAAA ! You now have some reveal.js slides that are  fully-functional with the `file://` procotol, e.g. if you directly open `index.html` with your browser.

**EDIT 2016/10/13** : actually an even simpler solution is to put your Markdown **directly** in a `<section>` in you `index.html`.