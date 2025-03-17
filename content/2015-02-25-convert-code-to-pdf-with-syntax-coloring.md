Title: Convert source code to PDF with syntax coloring
Date: 2015-02-25 23:02
Lang: en
Tags: lang:en, html, color, pdf, vim, syntastic, postscript, term, source-code, syntax-highlight, perl, python, pygmentize, wkhtmltopdf, prog
Slug: convert-code-to-pdf-with-syntax-coloring
---
Sometimes, it's useful to print some source code on paper. And PDF is a very common file format, that you can be sure your printer will accept, and that will let you preview the final page layout.
But how to quickly perform syntax-coloring and export to PDF ?

I've been experimenting with `pandoc`, GNU `highlight` and Latex/Xetex. Finally, I wrote the following simple bash function to do the job, using `pygmentize` and `wkhtmltopdf` :

```
src2pdf () {
    local noext="${1%.*}"
    pygmentize -O full -o "$noext.html" "$1"
    # enabling line wrapping in <pre> blocks
    perl -i -wpe '/<style.*>$/&&($_.="pre{white-space:pre-wrap;}\n")' "$noext.html"
    wkhtmltopdf "$noext.html" "$noext.pdf"
    rm "$noext.html"
}
```

There is an example of [PDF result, 133Ko](images/2015/Fev/UnixUsefulCmds.pdf).

Alternatively, if you have syntax coloring enabled in vim, e.g. with the great `syntastic` plugin, export to PostScript is trivial :

```
TERM=xterm-256color vim '+hardcopy >out.ps' +q code.src
```

Because with other values of `$TERM` environment variable the output colors can change, I prefer to set it explicitly.

You also may need to tweak your _.vimrc_ a little, here is my config :
```
set printfont=:h9
set printoptions=number:y,left:5pc
```

And [the final .ps file](/lucas/blog/images/2015/Fev/UnixUsefulCmds.ps).

<iframe width="560" height="315" src="https://www.youtube.com/embed/wudV1c9jLKM" allowfullscreen></iframe>

<style>
article iframe { display: block; margin: 1rem auto; }
</style>
