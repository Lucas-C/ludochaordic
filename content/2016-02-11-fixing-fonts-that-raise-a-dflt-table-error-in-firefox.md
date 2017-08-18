Title: Fixing fonts that raise a "DFLT table doesn't satisfy the spec. LangSysCount is not zero" error in Firefox
Date: 2016-02-11 14:02
Tags: lang:en, sed, fonts, firefox, otf, ttf, ttx, dflt, xml, prog
Slug: fixing-fonts-that-raise-a-dflt-table-error-in-firefox
---


Did you ever got this infamous error message in Firefox debug console (with CSS error messages enabled) ?
```
downloadable font: Layout: DFLT table doesn't satisfy the spec. for script tag DFLT (font-family: "MyBeautifulFont" style:normal weight:normal stretch:normal src index:1) source: http://W.X.Y.Z/fonts/myfont.woff2
downloadable font: Layout: Failed to parse script table 0 (font-family: "MyBeautifulFont" style:normal weight:normal stretch:normal src index:1) source: http://W.X.Y.Z/fonts/myfont.woff2
downloadable font: GSUB: Failed to parse script list table (font-family: "MyBeautifulFont" style:normal weight:normal stretch:normal src index:1) source: http://W.X.Y.Z/fonts/myfont.woff2
```

In my case it was accompanied by an obvious visual bug: all of the text on my website was rendered with default "fallback" fonts (Arial, Helvetica...), not the ones specified in the CSS.

Why ? First, lets understand the origin of this message: under the hood, Firefox use [ot-sanitize](//github.com/khaledhosny/ots) to check fonts. Hence you get a similar error message using this tool:
```
$ ot-sanitise myfont.otf
ERROR: Layout: DFLT script doesn't satisfy the spec. LangSysCount is not zero: 1
ERROR: Layout: Failed to parse script table 0
ERROR: GSUB: Failed to parse script list table
Failed to sanitise file!
```

Miracle of the Internets, I found an explanation for this specific error [here](//github.com/khaledhosny/ots/blob/master/docs/HowToFix.md), in the spare documentation of this very same project.
Alas, without any suggestion for a fix :(

![Strip 979 de xkcd: Wisdom of the ancients](images/2016/02/xkcd_979_wisdom_of_the_ancients.png)

But now I will demonstrate how to fix an `.otf` file presenting this problem.
The following also works with `.ttf` / `.woff` / `.woff2` files, and by the way, [css3FontConverter](//github.com/zoltan-dulac/css3FontConverter) is **magic** to convert your font files to all the formats needed to be displayed nicely in old browsers as well as modern ones : it even generates the CSS declaration !

Here comes the magic `ttx` command (from the awesome [fonttools](//github.com/behdad/fonttools) Python package) and good old `sed` to the rescue:

```
pip install fonttools
ttx -o myfont.ttx myfont.otf
tr '\n' ' ' < myfont.ttx | sed 's~\(<GSUB>.\<ScriptTag value="DFLT"/>.\++</DefaultLangSys>\)\s\+<!-- LangSysCount=1 -->\s\+<LangSysRecord.\+</LangSysRecord>~\1~' > myfont_fixed.ttx
ttx -o myfont_fixed.otf myfont_fixed.ttx
```

You can now test the output file with `ot-sanitise` : the check should pass !

Now the explanation on what this `sed` voodoo does: it deletes any `<LangSysRecord>` tag under `ttFont > GSUB > ScriptList > ScriptRecord[ScriptTag="DFLT"] > Script` in the `.ttx` file, in order to conform to the spec.

It would be waaay cleaner to this with [`xml2`](http://www.ofb.net/~egnor/xml2) / [`xmlstarlet`](http://xmlstar.sourceforge.net/docs.php) / [any other CLI tool that manipulate XML](//stackoverflow.com/a/91801), but `sed` is very portable and can be found on any Unix system.
