Title: A review of HTML linters
Date: 2025-03-17 23:55
Lang: en
Tags: lang:en, html, linter, python, source-code, vnu, w3c, continuous-integration, gitlab-ci, github-actions, static-code-analysis, libre-software, open-source, java, typescript, eslint, prog
---

... and how to use them in CI pipelines.

- [Overview](a-review-of-html-linters.html#overview)
- [Introduction / motivation](a-review-of-html-linters.html#introduction--motivation)
- [HTML linters and their usage](a-review-of-html-linters.html#html-linters-and-their-usage)
    * [W3C v.Nu HTML checker](a-review-of-html-linters.html#w3c-v.nu-html-checker)
    * [html-tidy](a-review-of-html-linters.html#html-tidy)
    * [htmlhint](a-review-of-html-linters.html#htmlhint)
    * [html-validate](a-review-of-html-linters.html#html-validate)
    * [LintHTML](a-review-of-html-linters.html#linthtml)
    * [html-eslint](a-review-of-html-linters.html#html-eslint)
- [Evaluating HTML linters on reference pages](a-review-of-html-linters.html#evaluating-html-linters-on-reference-pages)
- [Conclusion](a-review-of-html-linters.html#conclusion)
    * [Related tools & readings](a-review-of-html-linters.html#related-tools--readings)

<figure>
  <img src="images/2025/03/HTML-Doctype.png" alt="">
  <figcaption>HTML Doctype - Author: Seobility - License: <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license">CC BY-SA 4.0</a></figcaption>
</figure>

## Overview

HTML linters: | [W3C v.Nu checker](https://validator.github.io/validator/) | [html-tidy](https://www.html-tidy.org/) | [htmlhint](https://htmlhint.com/) | [html-validate](https://html-validate.org/) | [LintHTML](https://linthtml.vercel.app/) | [html-eslint](https://html-eslint.org/)
-|-|-|-|-|-|-
Age | 20 years | > 22 years | 11 years | 7 years | 5 years <small>(fork of an 11 years old project)</small> | 5 years
Actively maintained? | [✅](https://github.com/validator/validator/commits/main/) | [❌](https://github.com/htacg/tidy-html5/commits/next/) | [✅](https://github.com/htmlhint/HTMLHint/commits/master/) | [✅](https://gitlab.com/html-validate/html-validate/-/commits/master?ref_type=heads) | [✅](https://github.com/linthtml/linthtml/commits/develop/) | [✅](https://github.com/yeonjuan/html-eslint/commits/main/)
Reported issues | 1361<br><small>(79% closed)</small> | 816<br><small>(77%&nbsp;closed)</small> | 299<br><small>(85%&nbsp;closed)</small> | 297<br><small>(82% closed)</small> | 69<br><small>(73% closed)</small> | 104<br><small>(84% closed)</small>
Number of rules | [>❔<](https://github.com/validator/validator/issues/1804) <small>(hundreds)</small> | [337](https://github.com/htacg/tidy-html5/blob/5.9.14-next/include/tidyenum.h#L108) | [37](https://github.com/htmlhint/HTMLHint/tree/master/src/core/rules) | [104](https://gitlab.com/html-validate/html-validate/-/tree/master/src/rules?ref_type=heads) | [65](https://github.com/linthtml/linthtml/tree/develop/packages/core/src/rules) | [50](https://github.com/yeonjuan/html-eslint/tree/main/packages/eslint-plugin/lib/rules)
Written in | Java | C | Typescript | Typescript | Typescript | Javascript
Version tested | 24.5.11 | 5.9.14 | 1.1.4 | 9.5.0 | 0.10.1 | 0.36.0
Fast? | ❌ | ✅ | ✅ | ✅ | ✅ | ❌
Auto-fix? | ❌ | ✅ | ❌ | ❌ | ❌ | only 2 rules
Allow custom rules / plugins | ❌ | ❌ | ✅ | ✅ | ✅ | ❔
Spot useful errors? | ✅ | ❌ | ❌ | ✅ | ❌ | ❌

The last criterion was estimated based on the tests performed in section "[Evaluating HTML linters on reference pages](#evaluating-html-linters-on-reference-pages)" below in this article.


## Introduction / motivation
I have started writing this blog article [4 years ago](https://github.com/Lucas-C/ludochaordic/commit/2542771e64366463e5c04e8ba05eb7248abf562c),
but never took the time to finish it until now.

Clearly, this is all about obsessive-compulsive [static code analysis](tag/static-code-analysis.html) 😅,
because checking HTML syntax is less necessary nowadays:

* when building websites, it has become common to use higher-level languages that get converted to "clean" HTML by intermediate tools: Markdown, reStructuredText, wiki markup, etc. Or even JSX/TSX templates for frontend developers. It's less frequent to write "bare" HTML directly.
* HTML parsers are very robust to errors: your current browser is perfectly able to render horribly broken HTML like this.

This other article dives more into this subject:  [Why is HTML linting not a common practice? @dev.to](https://dev.to/dandevri/why-is-html-linting-not-a-common-practice-4gme).

Now, we will have a look at the major open-source HTML linters,
and then analyse how they compare to each other.


## HTML linters and their usage

### W3C v.Nu HTML checker
[v.Nu, the Nu HTML Checker](https://validator.github.io/validator/) is maintained by the _World Wide Web Consortium_ (W3C).
While it's running on Java,
it is usable as Docker image or even directly as a binary.

Errors & warnings can be selectively ignored using a `.vnurc` file,
_cf_. [their _"Message filtering"_ wiki page](https://github.com/validator/validator/wiki/Message-filtering).

As an example, the following code snippet installs & runs it in a Gitlab CI pipeline:
```yaml
  install:
  - apt update -y && apt install -y curl unzip  # assume Debian distribution
  - |
    curl -ROLs https://github.com/validator/validator/releases/download/latest/vnu.linux.zip \
    && unzip vnu.linux.zip \
    && rm vnu.linux.zip \
    && vnu-runtime-image/bin/vnu --version
  script:
  - vnu-runtime-image/bin/vnu --filterfile .vnurc --Werror --skip-non-html root/html/dir/
```

Sadly, they do not perform frequent GitHub releases,
they only override a `latest` version: <https://github.com/validator/validator/releases/>.
This makes it difficult to "pin" a given recent version of this linter in a CI pipeline.


### html-tidy
I think that [html-tidy](https://www.html-tidy.org/) is the oldest HTML linter 🫡.

Sadly, it seems unmaintained: the [latest binaries are from 4 years ago](https://github.com/htacg/tidy-html5/issues/939).

It has an interesting "auto-fix" feature (with `-modify`),
making it the only linter I know able to auto-format HTML code.

The latest version allows to mute some **warnings**,
but [the exit code will still be non-zero](https://github.com/htacg/tidy-html5/issues/933),
making its usage in CI pipelines difficult.

As an example, the following code snippet installs & runs it in a Gitlab CI pipeline:
```yaml
  install:  # assume Debian distribution
  - wget -O tidy-html5.deb https://github.com/htacg/tidy-html5/releases/download/5.8.0/tidy-5.8.0-Linux-64bit.deb \
    && dpkg -i tidy-html5.deb \ \
    && rm tidy-html5.deb
    && tidy -version
  script:
  - tidy -errors -config htmltidy.conf *.html
```

Example of `htmltidy.conf`:
```
// cf. https://api.html-tidy.org/tidy/quickref_next.html
char-encoding: utf8
newline: lf
indent: auto
indent-spaces: 4
wrap: no
drop-empty-elements: false
warn-proprietary-attributes: no
# Display message ID's with error reports, useful to filter them out using "mute":
mute-id: yes
```
<!--
Note: on Lucas-C/jdr I ended up switching to the Nu HTML checker instead, because of the annoying `fix-style-tags` rule,
(cf. https://github.com/htacg/tidy-html5/issues/730 )
using the latest release, and the general lack of maintenance / answers on issues / new releases on the project
-->


### htmlhint
[htmlhint](https://htmlhint.com) is a more recent, JavaScript-based alternative.

It is relatively basic and straightforward to use,
but contains a relatively low number of HTML rules implemented.

As an example, the following code snippet installs & runs it in a Gitlab CI pipeline:
```yaml
  install:  # assume npm installed
  - npm install -g htmlhint
  script:
  - htmlhint
```

Example of `.htmlhintrc`:
```json
{
    "tagname-lowercase": true,
    "attr-lowercase": true,
    "attr-value-double-quotes": true,
    "doctype-first": true,
    "tag-pair": true,
    "spec-char-escape": true,
    "id-unique": true,
    "src-not-empty": true,
    "attr-no-duplication": true,
    "title-require": true
}
```


### html-validate
[html-validate](https://gitlab.com/html-validate/html-validate) is a serious contender
when it comes to recent & Javascript-based alternatives.

In my humble opinion, it's the best among the "fast" linters,
and comes second overall after the W3C v.Nu HTML checker.

As an example, the following code snippet installs & runs it in a Gitlab CI pipeline:
```yaml
  install:  # assume npm installed
  - npm install -g html-validate
  script:
  - html-validate
```
Example of `.htmlvalidate.json`:
```json
{
  "$schema": "https://html-validate.org/schemas/config.json",
  "extends": ["html-validate:recommended"],
  "rules": {
    "unique-landmark": "off"
  }
}
```


### LintHTML
LintHTML is a fork of the unmaintained [htmllint](https://github.com/htmllint/htmllint) project.

As an example, the following code snippet installs & runs it in a Gitlab CI pipeline:
```yaml
  install:  # assume npm installed
  - npm install -g @linthtml/linthtml
  script:
  - linthtml
```

`linthtml --init` should generate a starting point `.linthtmlrc` file.

⚠️ However I already spotted [some issue](https://github.com/linthtml/linthtml/issues/810)
with the config parser 😅


## html-eslint
[html-eslint](https://html-eslint.org/) is an ESLint plugin for formatting and linting HTML.

It doesn't contain many rules, and based on my tests mostly report indentation errors.

As an example, the following code snippet installs & runs it in a Gitlab CI pipeline:
```yaml
  install:  # assume npm installed
  - npm install -D -g eslint
  - npm install -D @html-eslint/parser @html-eslint/eslint-plugin
  script:
  - eslint *.html
```


## Evaluating HTML linters on reference pages
First, I tried to evaluate how much HTML checkers can be "picky" and produce "unnecessary" warnings by default,
when checking some somehow "standard" web pages.

All the HTML checkers considered provide a way to "silence" those warnings using a configuration file,
so even the "noisiest" HTML linter can be "tamed shut" 😄

The table below indicates how many rules are "triggered" by the HTML Linters considered,
when evaluating some reference HTML pages:

HTML linters: | [W3C v.Nu checker](https://validator.github.io/validator/) | [html-tidy](https://www.html-tidy.org/) | [htmlhint](https://htmlhint.com/) | [html-validate](https://html-validate.org/) | [LintHTML](https://linthtml.vercel.app/) | [html-eslint](https://html-eslint.org/)
-|-|-|-|-|-|-
[google.com](https://www.google.com/) | 6 | 12 | 1 <!-- attr-value-double-quotes --> | 9 | 6 | 6
[youtube.com](https://www.youtube.com) | 6 | 4 | 2 | 3 | 9 | 5
[MDN Learning Area](https://github.com/mdn/learning-area) | 3 | 1 | ✅ | 2 | ✅ | 2
[Bootstrap album example](https://getbootstrap.com/docs/5.0/examples/album/) | ✅ | 2 | ✅ | 2 | 8 | 3
[Foundation web framework](https://get.foundation) | 3 | 2 | ✅ | 4 | 4 | 5

Analysis details:
<details>
  <summary>google.com</summary>
  <pre><code>$ wget https://www.google.com -O google.com.html

$ vnu --Werror google.com.html
5.335-5.344: error: CSS: “display”: “inline-box” is not a “display” value.
10.410-10.410: error: Malformed byte sequence: “e9”.
10.923-10.923: error: Malformed byte sequence: “e8”.
7.909-7.929: error: The “bgcolor” attribute on the “body” element is obsolete. Use CSS instead.
10.43-10.48: error: Element “nobr” not allowed as child of element “div” in this context. (Suppressing further errors from this subtree.)
10.684-10.708: error: Attribute “width” not allowed on element “div” at this point.
10.709-10.714: error: Element “nobr” not allowed as child of element “div” in this context. (Suppressing further errors from this subtree.)
10.1180-10.1187: error: The “center” element is obsolete. Use CSS instead.
10.1188-10.1213: error: The “clear” attribute on the “br” element is obsolete. Use CSS instead.
10.1443-10.1481: error: The “cellpadding” attribute on the “table” element is obsolete. Use CSS instead.
10.1443-10.1481: error: The “cellspacing” attribute on the “table” element is obsolete. Use CSS instead.
10.1482-10.1498: error: The “valign” attribute on the “tr” element is obsolete. Use CSS instead.
10.1499-10.1514: error: The “width” attribute on the “td” element is obsolete. Use CSS instead.
10.1526-10.1554: error: The “align” attribute on the “td” element is obsolete. Use CSS instead.
10.1526-10.1554: error: The “nowrap” attribute on the “td” element is obsolete. Use CSS instead.
11.272-11.272: error: Malformed byte sequence: “e9”.
11.1080-11.1080: error: Malformed byte sequence: “e9”.
11.1162-11.1162: error: Malformed byte sequence: “c0”.
11.154-11.208: error: The “align” attribute on the “td” element is obsolete. Use CSS instead.
11.154-11.208: error: The “nowrap” attribute on the “td” element is obsolete. Use CSS instead.
11.154-11.208: error: The “width” attribute on the “td” element is obsolete. Use CSS instead.
11.960-11.987: error: Element “div” not allowed as child of element “span” in this context. (Suppressing further errors from this subtree.)
11.1444-11.1444: error: Malformed byte sequence: “e9”.
11.1340-11.1378: error: Element “p” not allowed as child of element “span” in this context. (Suppressing further errors from this subtree.)

$ tidy -errors google.com.html
line 10 column 30 - Info: value for attribute "id" missing quote marks
line 10 column 49 - Info: value for attribute "class" missing quote marks
line 10 column 76 - Info: value for attribute "class" missing quote marks
line 10 column 129 - Warning: unescaped & or unknown entity "&tab"
line 10 column 149 - Info: value for attribute "class" missing quote marks
line 10 column 201 - Warning: unescaped & or unknown entity "&tab"
line 10 column 219 - Info: value for attribute "class" missing quote marks
line 10 column 268 - Warning: unescaped & or unknown entity "&tab"
line 10 column 286 - Info: value for attribute "class" missing quote marks
line 10 column 350 - Info: value for attribute "class" missing quote marks
line 10 column 410 - Warning: replacing invalid UTF-8 bytes (char. code U+0009)
line 10 column 417 - Info: value for attribute "class" missing quote marks
line 10 column 484 - Info: value for attribute "class" missing quote marks
line 10 column 547 - Info: value for attribute "class" missing quote marks
line 10 column 684 - Info: value for attribute "id" missing quote marks
line 10 column 684 - Info: value for attribute "width" missing quote marks
line 10 column 715 - Info: value for attribute "id" missing quote marks
line 10 column 715 - Info: value for attribute "class" missing quote marks
line 10 column 745 - Info: value for attribute "id" missing quote marks
line 10 column 745 - Info: value for attribute "class" missing quote marks
line 10 column 775 - Info: value for attribute "id" missing quote marks
line 10 column 795 - Info: value for attribute "class" missing quote marks
line 10 column 878 - Info: value for attribute "class" missing quote marks
line 10 column 923 - Warning: replacing invalid UTF-8 bytes (char. code U+0008)
line 10 column 935 - Info: value for attribute "target" missing quote marks
line 10 column 935 - Info: value for attribute "id" missing quote marks
line 10 column 1011 - Warning: unescaped & or unknown entity "&passive"
line 10 column 1024 - Warning: unescaped & or unknown entity "&continue"
line 10 column 1057 - Warning: unescaped & or unknown entity "&ec"
line 10 column 935 - Info: value for attribute "class" missing quote marks
line 10 column 1105 - Info: value for attribute "class" missing quote marks
line 10 column 1105 - Info: value for attribute "style" missing quote marks
line 10 column 1139 - Info: value for attribute "class" missing quote marks
line 10 column 1139 - Info: value for attribute "style" missing quote marks
line 11 column 272 - Warning: replacing invalid UTF-8 bytes (char. code U+0009)
line 11 column 942 - Warning: missing &lt;/span&gt; before &lt;div&gt;
line 11 column 988 - Warning: inserting implicit &lt;span&gt;
line 11 column 988 - Warning: missing &lt;/span&gt; before &lt;div&gt;
line 11 column 1048 - Warning: inserting implicit &lt;span&gt;
line 11 column 1080 - Warning: replacing invalid UTF-8 bytes (char. code U+0009)
line 11 column 1162 - Warning: replacing invalid UTF-8 bytes (char. code U+0000)
line 11 column 1379 - Warning: inserting implicit &lt;span&gt;
line 11 column 1444 - Warning: replacing invalid UTF-8 bytes (char. code U+0009)
line 11 column 1505 - Warning: discarding unexpected &lt;/span&gt;
line 7 column 909 - Warning: &lt;body&gt; attribute "bgcolor" has invalid value "#fff"
line 11 column 988 - Warning: Implicit &lt;span&gt; anchor "footer" duplicated by Tidy.
line 11 column 1048 - Warning: Implicit &lt;span&gt; anchor "footer" duplicated by Tidy.
line 11 column 1379 - Warning: Implicit &lt;span&gt; anchor "footer" duplicated by Tidy.
line 7 column 909 - Warning: &lt;body&gt; attribute "bgcolor" not allowed for HTML5
line 10 column 1180 - Warning: &lt;center&gt; element removed from HTML5
line 10 column 1526 - Warning: &lt;td&gt; attribute "align" not allowed for HTML5
line 11 column 154 - Warning: &lt;td&gt; attribute "align" not allowed for HTML5
line 1 column 270 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 5 column 1070 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 7 column 909 - Warning: &lt;body&gt; attribute "bgcolor" not allowed for HTML5
line 7 column 930 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 10 column 43 - Warning: &lt;nobr&gt; is not approved by W3C
line 10 column 684 - Warning: &lt;div&gt; proprietary attribute "width"
line 10 column 709 - Warning: &lt;nobr&gt; is not approved by W3C
line 10 column 1188 - Warning: &lt;br&gt; attribute "clear" not allowed for HTML5
line 10 column 1443 - Warning: &lt;table&gt; attribute "cellpadding" not allowed for HTML5
line 10 column 1443 - Warning: &lt;table&gt; attribute "cellspacing" not allowed for HTML5
line 10 column 1482 - Warning: &lt;tr&gt; attribute "valign" not allowed for HTML5
line 10 column 1499 - Warning: &lt;td&gt; attribute "width" not allowed for HTML5
line 10 column 1526 - Warning: &lt;td&gt; attribute "align" not allowed for HTML5
line 10 column 1526 - Warning: &lt;td&gt; attribute "nowrap" not allowed for HTML5
line 10 column 2279 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 11 column 154 - Warning: &lt;td&gt; attribute "align" not allowed for HTML5
line 11 column 154 - Warning: &lt;td&gt; attribute "nowrap" not allowed for HTML5
line 11 column 154 - Warning: &lt;td&gt; attribute "width" not allowed for HTML5
line 11 column 347 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 11 column 1521 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 11 column 2042 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 11 column 2833 - Warning: &lt;script&gt; proprietary attribute "nonce"

$ htmlhint google.com.html
L10 |})();&lt;/script&gt;&lt;div id="mngb"&gt;&lt;div id=gbar&gt;&lt;nobr&gt;&lt;b class=gb1&gt;Recherche&lt;/b&gt; &lt;a class=gb1 href="https:/...
                                      ^ The value of attribute [ id ] must be in double quotes. (attr-value-double-quotes)
L10 |...ipt&gt;&lt;div id="mngb"&gt;&lt;div id=gbar&gt;&lt;nobr&gt;&lt;b class=gb1&gt;Recherche&lt;/b&gt; &lt;a class=gb1 href="https://www.googl...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...gbar&gt;&lt;nobr&gt;&lt;b class=gb1&gt;Recherche&lt;/b&gt; &lt;a class=gb1 href="https://www.google.com/imghp?hl=fr&tab=wi"&gt;I...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...le.com/imghp?hl=fr&tab=wi"&gt;Images&lt;/a&gt; &lt;a class=gb1 href="https://maps.google.fr/maps?hl=fr&tab=wl"&gt;Ma...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...google.fr/maps?hl=fr&tab=wl"&gt;Maps&lt;/a&gt; &lt;a class=gb1 href="https://play.google.com/?hl=fr&tab=w8"&gt;Play&lt;...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...ay.google.com/?hl=fr&tab=w8"&gt;Play&lt;/a&gt; &lt;a class=gb1 href="https://www.youtube.com/?tab=w1"&gt;YouTube&lt;/a&gt;...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |.../www.youtube.com/?tab=w1"&gt;YouTube&lt;/a&gt; &lt;a class=gb1 href="https://news.google.com/?tab=wn"&gt;Actualités&lt;...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...ws.google.com/?tab=wn"&gt;Actualités&lt;/a&gt; &lt;a class=gb1 href="https://mail.google.com/mail/?tab=wm"&gt;Gmail&lt;...
                                                  ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...il.google.com/mail/?tab=wm"&gt;Gmail&lt;/a&gt; &lt;a class=gb1 href="https://drive.google.com/?tab=wo"&gt;Drive&lt;/a&gt; ...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...//drive.google.com/?tab=wo"&gt;Drive&lt;/a&gt; &lt;a class=gb1 style="text-decoration:none" href="https://www.goo...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...&lt;u&gt;Plus&lt;/u&gt; &raquo;&lt;/a&gt;&lt;/nobr&gt;&lt;/div&gt;&lt;div id=guser width=100%&gt;&lt;nobr&gt;&lt;span id=gbn class=gbi&gt;&lt;/span&gt;&lt;spa...
                                                ^ The value of attribute [ id ] must be in double quotes. (attr-value-double-quotes)
L10 |...u&gt; &raquo;&lt;/a&gt;&lt;/nobr&gt;&lt;/div&gt;&lt;div id=guser width=100%&gt;&lt;nobr&gt;&lt;span id=gbn class=gbi&gt;&lt;/span&gt;&lt;span id=gbf ...
                                                ^ The value of attribute [ width ] must be in double quotes. (attr-value-double-quotes)
L10 |...div&gt;&lt;div id=guser width=100%&gt;&lt;nobr&gt;&lt;span id=gbn class=gbi&gt;&lt;/span&gt;&lt;span id=gbf class=gbf&gt;&lt;/span&gt;&lt;span ...
                                                ^ The value of attribute [ id ] must be in double quotes. (attr-value-double-quotes)
L10 |...v id=guser width=100%&gt;&lt;nobr&gt;&lt;span id=gbn class=gbi&gt;&lt;/span&gt;&lt;span id=gbf class=gbf&gt;&lt;/span&gt;&lt;span id=gbe&gt;...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...nobr&gt;&lt;span id=gbn class=gbi&gt;&lt;/span&gt;&lt;span id=gbf class=gbf&gt;&lt;/span&gt;&lt;span id=gbe&gt;&lt;/span&gt;&lt;a href="http://...
                                                ^ The value of attribute [ id ] must be in double quotes. (attr-value-double-quotes)
L10 |...pan id=gbn class=gbi&gt;&lt;/span&gt;&lt;span id=gbf class=gbf&gt;&lt;/span&gt;&lt;span id=gbe&gt;&lt;/span&gt;&lt;a href="http://www.goo...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...span&gt;&lt;span id=gbf class=gbf&gt;&lt;/span&gt;&lt;span id=gbe&gt;&lt;/span&gt;&lt;a href="http://www.google.fr/history/optout?h...
                                                ^ The value of attribute [ id ] must be in double quotes. (attr-value-double-quotes)
L10 |...tp://www.google.fr/history/optout?hl=fr" class=gb4&gt;Historique Web&lt;/a&gt; | &lt;a  href="/preferences?hl=fr"...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |... Web&lt;/a&gt; | &lt;a  href="/preferences?hl=fr" class=gb4&gt;Paramètres&lt;/a&gt; | &lt;a target=_top id=gb_70 href="htt...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...ces?hl=fr" class=gb4&gt;Paramètres&lt;/a&gt; | &lt;a target=_top id=gb_70 href="https://accounts.google.com/Servi...
                                                  ^ The value of attribute [ target ] must be in double quotes. (attr-value-double-quotes)
L10 |...lass=gb4&gt;Paramètres&lt;/a&gt; | &lt;a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=f...
                                                  ^ The value of attribute [ id ] must be in double quotes. (attr-value-double-quotes)
L10 |...tinue=https://www.google.com/&ec=GAZAAQ" class=gb4&gt;Connexion&lt;/a&gt;&lt;/nobr&gt;&lt;/div&gt;&lt;div class=gbh style=lef...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...class=gb4&gt;Connexion&lt;/a&gt;&lt;/nobr&gt;&lt;/div&gt;&lt;div class=gbh style=left:0&gt;&lt;/div&gt;&lt;div class=gbh style=right:0&gt;&lt;/...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...Connexion&lt;/a&gt;&lt;/nobr&gt;&lt;/div&gt;&lt;div class=gbh style=left:0&gt;&lt;/div&gt;&lt;div class=gbh style=right:0&gt;&lt;/div&gt;&lt;/div&gt;...
                                                ^ The value of attribute [ style ] must be in double quotes. (attr-value-double-quotes)
L10 |...v&gt;&lt;div class=gbh style=left:0&gt;&lt;/div&gt;&lt;div class=gbh style=right:0&gt;&lt;/div&gt;&lt;/div&gt;&lt;center&gt;&lt;br clear="all" ...
                                                ^ The value of attribute [ class ] must be in double quotes. (attr-value-double-quotes)
L10 |...ss=gbh style=left:0&gt;&lt;/div&gt;&lt;div class=gbh style=right:0&gt;&lt;/div&gt;&lt;/div&gt;&lt;center&gt;&lt;br clear="all" id="lgpd"&gt;...
                                                ^ The value of attribute [ style ] must be in double quotes. (attr-value-double-quotes)

$ html-validate google.com.html
 1:1     error  DOCTYPE should be uppercase                                                  doctype-style
 7:915   error  Attribute "bgcolor" is deprecated on &lt;body&gt; element                          no-deprecated-attr
10:35    error  Attribute "id" using unquoted value                                          attr-quotes
10:44    error  &lt;nobr&gt; is deprecated: use CSS instead                                        deprecated
10:44    error  &lt;nobr&gt; element is not permitted as content under &lt;div&gt;                       element-permitted-content
10:52    error  Attribute "class" using unquoted value                                       attr-quotes
10:79    error  Attribute "class" using unquoted value                                       attr-quotes
10:152   error  Attribute "class" using unquoted value                                       attr-quotes
10:222   error  Attribute "class" using unquoted value                                       attr-quotes
10:289   error  Attribute "class" using unquoted value                                       attr-quotes
10:353   error  Attribute "class" using unquoted value                                       attr-quotes
10:420   error  Attribute "class" using unquoted value                                       attr-quotes
10:487   error  Attribute "class" using unquoted value                                       attr-quotes
10:550   error  Attribute "class" using unquoted value                                       attr-quotes
10:560   error  Inline style is not allowed                                                  no-inline-style
10:689   error  Attribute "id" using unquoted value                                          attr-quotes
10:698   error  Attribute "width" using unquoted value                                       attr-quotes
10:710   error  &lt;nobr&gt; is deprecated: use CSS instead                                        deprecated
10:710   error  &lt;nobr&gt; element is not permitted as content under &lt;div&gt;                       element-permitted-content
10:721   error  Attribute "id" using unquoted value                                          attr-quotes
10:728   error  Attribute "class" using unquoted value                                       attr-quotes
10:751   error  Attribute "id" using unquoted value                                          attr-quotes
10:758   error  Attribute "class" using unquoted value                                       attr-quotes
10:781   error  Attribute "id" using unquoted value                                          attr-quotes
10:847   error  Attribute "class" using unquoted value                                       attr-quotes
10:908   error  Attribute "class" using unquoted value                                       attr-quotes
10:938   error  Attribute "target" using unquoted value                                      attr-quotes
10:950   error  Attribute "id" using unquoted value                                          attr-quotes
10:1069  error  Attribute "class" using unquoted value                                       attr-quotes
10:1110  error  Attribute "class" using unquoted value                                       attr-quotes
10:1120  error  Attribute "style" using unquoted value                                       attr-quotes
10:1120  error  Inline style is not allowed                                                  no-inline-style
10:1144  error  Attribute "class" using unquoted value                                       attr-quotes
10:1154  error  Attribute "style" using unquoted value                                       attr-quotes
10:1154  error  Inline style is not allowed                                                  no-inline-style
10:1181  error  &lt;center&gt; is deprecated: use CSS instead                                      deprecated
10:1181  error  &lt;center&gt; element is not permitted as content under &lt;body&gt;                    element-permitted-content
10:1192  error  Attribute "clear" is deprecated on &lt;br&gt; element                              no-deprecated-attr
10:1345  error  Inline style is not allowed                                                  no-inline-style
10:1450  error  Attribute "cellpadding" is deprecated on &lt;table&gt; element                     no-deprecated-attr
10:1466  error  Attribute "cellspacing" is deprecated on &lt;table&gt; element                     no-deprecated-attr
10:1483  error  Prefer to wrap &lt;tr&gt; elements in &lt;tbody&gt;                                      prefer-tbody
10:1486  error  Attribute "valign" is deprecated on &lt;tr&gt; element                             no-deprecated-attr
10:1503  error  Attribute "width" is deprecated on &lt;td&gt; element                              no-deprecated-attr
10:1530  error  Attribute "align" is deprecated on &lt;td&gt; element                              no-deprecated-attr
10:1545  error  Attribute "nowrap" is deprecated on &lt;td&gt; element                             no-deprecated-attr
10:1773  error  Inline style is not allowed                                                  no-inline-style
10:1807  error  &lt;input&gt; is missing recommended "type" attribute                              no-implicit-input-type
10:1825  error  Inline style is not allowed                                                  no-inline-style
10:1993  error  Inline style is not allowed                                                  no-inline-style
10:2113  error  Prefer to use &lt;button&gt; instead of &lt;input type="submit"&gt; when adding buttons  prefer-button
10:2271  error  Prefer to use &lt;button&gt; instead of &lt;input type="submit"&gt; when adding buttons  prefer-button
11:174   error  Attribute "align" is deprecated on &lt;td&gt; element                              no-deprecated-attr
11:187   error  Attribute "nowrap" is deprecated on &lt;td&gt; element                             no-deprecated-attr
11:197   error  Attribute "width" is deprecated on &lt;td&gt; element                              no-deprecated-attr
11:893   error  Inline style is not allowed                                                  no-inline-style
11:961   error  &lt;div&gt; element is not permitted as content under &lt;span&gt;                       element-permitted-content
11:965   error  Inline style is not allowed                                                  no-inline-style
11:993   error  Inline style is not allowed                                                  no-inline-style
11:1341  error  &lt;p&gt; element is not permitted as content under &lt;span&gt;                         element-permitted-content
11:1343  error  Inline style is not allowed                                                  no-inline-style

$ linthtml google.com.html
 13:1804  error    Incorrect indentation for `html` beginning at L13:C1804. Expected `&lt;\html&gt;` to be at an indentation of 0 but was found at 1803.      indent-style
  1:82    error    Incorrect indentation for `head` beginning at L1:C82. Expected `&lt;head&gt;` to be at an indentation of 4 but was found at 81.            indent-style
  1:88    error    Incorrect indentation for `meta` beginning at L1:C88. Expected `&lt;meta&gt;` to be at an indentation of 8 but was found at 87.            indent-style
  4:479   error    Incorrect indentation for `script` beginning at L4:C479. Expected `&lt;\script&gt;` to be at an indentation of 8 but was found at 478.     indent-style
  5:1     error    Incorrect indentation for `style` beginning at L5:C1. Expected `&lt;\style&gt;` to be at an indentation of 8 but was found at 0.           indent-style
  4:488   error    The tag &lt;style&gt; is banned and should not be used
                            tag-bans
  5:9     error    The tag &lt;style&gt; is banned and should not be used
                            tag-bans
  7:893   error    Incorrect indentation for `script` beginning at L7:C893. Expected `&lt;\script&gt;` to be at an indentation of 8 but was found at 892.     indent-style
  7:915   error    The attribute "bgcolor" attribute is cannot be used as it's banned
                            attr-bans
 13:1797  error    Incorrect indentation for `body` beginning at L13:C1797. Expected `&lt;\body&gt;` to be at an indentation of 4 but was found at 1796.      indent-style
  7:930   error    Incorrect indentation for `script` beginning at L7:C930. Expected `&lt;script&gt;` to be at an indentation of 8 but was found at 929.      indent-style
 10:38    error    The attribute "id" is not double quoted
                            attr-quote-style
 10:49    error    The tag &lt;b&gt; is banned and should not be used
                            tag-bans
 10:58    error    The attribute "class" is not double quoted
                            attr-quote-style
 10:85    error    The attribute "class" is not double quoted
                            attr-quote-style
 10:158   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:228   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:295   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:359   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:426   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:493   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:560   error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 10:556   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:698   error    The attribute "width" attribute is cannot be used as it's banned
                            attr-bans
 10:692   error    The attribute "id" is not double quoted
                            attr-quote-style
 10:704   error    The attribute "width" is not double quoted
                            attr-quote-style
 10:724   error    The attribute "id" is not double quoted
                            attr-quote-style
 10:734   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:754   error    The attribute "id" is not double quoted
                            attr-quote-style
 10:764   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:784   error    The attribute "id" is not double quoted
                            attr-quote-style
 10:853   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:914   error    The attribute "class" is not double quoted
                            attr-quote-style
 10:945   error    The attribute "target" is not double quoted
                            attr-quote-style
 10:953   error    The attribute "id" is not double quoted
                            attr-quote-style
 10:1075  error    The attribute "class" is not double quoted
                            attr-quote-style
 10:1120  error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 10:1116  error    The attribute "class" is not double quoted
                            attr-quote-style
 10:1126  error    The attribute "style" is not double quoted
                            attr-quote-style
 10:1154  error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 10:1150  error    The attribute "class" is not double quoted
                            attr-quote-style
 10:1160  error    The attribute "style" is not double quoted
                            attr-quote-style
 11:1512  error    Incorrect indentation for `center` beginning at L11:C1512. Expected `&lt;\center&gt;` to be at an indentation of 8 but was found at 1511.  indent-style
 10:1188  error    Incorrect indentation for `br` beginning at L10:C1188. Expected `&lt;br&gt;` to be at an indentation of 12 but was found at 1187.          indent-style
 10:1219  error    The value "XjhHGf" of attribute "id" does not respect the format: underscore
                            id-class-style
 10:1345  error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 10:1373  error    The attribute "width" attribute is cannot be used as it's banned
                            attr-bans
 11:881   error    Incorrect indentation for `form` beginning at L11:C881. Expected `&lt;\form&gt;` to be at an indentation of 12 but was found at 880.       indent-style
 11:288   error    Incorrect indentation for `table` beginning at L11:C288. Expected `&lt;\table&gt;` to be at an indentation of 16 but was found at 287.     indent-style
 11:283   error    Incorrect indentation for `tr` beginning at L11:C283. Expected `&lt;\tr&gt;` to be at an indentation of 20 but was found at 282.           indent-style
 10:1503  error    The attribute "width" attribute is cannot be used as it's banned
                            attr-bans
 10:1499  error    Incorrect indentation for `td` beginning at L10:C1499. Expected `&lt;td&gt;` to be at an indentation of 24 but was found at 1498.          indent-style
 10:1530  error    The attribute "align" attribute is cannot be used as it's banned
                            attr-bans
 11:149   error    Incorrect indentation for `td` beginning at L11:C149. Expected `&lt;\td&gt;` to be at an indentation of 24 but was found at 148.           indent-style
 10:1555  error    Incorrect indentation for `input` beginning at L10:C1555. Expected `&lt;input&gt;` to be at an indentation of 28 but was found at 1554.    indent-style
 10:1773  error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 10:1825  error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 10:1913  error    The attribute "value" requires a value
                            attr-req-value
 10:1993  error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 11:142   error    Incorrect indentation for `span` beginning at L11:C142. Expected `&lt;\span&gt;` to be at an indentation of 28 but was found at 141.       indent-style
 11:135   error    Incorrect indentation for `span` beginning at L11:C135. Expected `&lt;\span&gt;` to be at an indentation of 32 but was found at 134.       indent-style
 10:2171  error    Incorrect indentation for `input` beginning at L10:C2171. Expected `&lt;input&gt;` to be at an indentation of 36 but was found at 2170.    indent-style
 10:2190  error    The value "tsuid_Zy3YZ83uLebYkdUP0fCjoAw_1" of attribute "id" does not respect the format: underscore
                            id-class-style
 11:38    error    Incorrect indentation for `script` beginning at L11:C38. Expected `&lt;\script&gt;` to be at an indentation of 36 but was found at 37.     indent-style
 11:174   error    The attribute "align" attribute is cannot be used as it's banned
                            attr-bans
 11:197   error    The attribute "width" attribute is cannot be used as it's banned
                            attr-bans
 11:893   error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 11:965   error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 11:993   error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 11:1036  error    The value "WqQANb" of attribute "id" does not respect the format: underscore
                            id-class-style
 11:1343  error    The attribute "style" attribute is cannot be used as it's banned
                            attr-bans
 13:1781  error    Incorrect indentation for `script` beginning at L13:C1781. Expected `&lt;\script&gt;` to be at an indentation of 8 but was found at 1780.  indent-style

$ eslint google.com.html
...redacted for brevity...</code></pre>
</details>

<details>
  <summary>youtube.com</summary>
  <pre><code>$ wget https://youtube.com -O youtube.com.html

$ vnu --Werror youtube.com.html
1.16-1.195: error: Attribute “darker-dark-theme” not allowed on element “html” at this point.
1.16-1.195: error: Attribute “darker-dark-theme-deprecate” not allowed on element “html” at this point.
1.16-1.195: error: Attribute “system-icons” not allowed on element “html” at this point.
1.16-1.195: error: Attribute “typography” not allowed on element “html” at this point.
1.16-1.195: error: Attribute “typography-spacing” not allowed on element “html” at this point.
1.16-1.195: error: Attribute “refresh” not allowed on element “html” at this point.
1.686-1.739: info: Trailing slash on void elements has no effect and interacts badly with unquoted attribute values.
1.740-1.1023: error: Bad value “origin-trial” for attribute “http-equiv” on element “meta”.
1.740-1.1023: info: Trailing slash on void elements has no effect and interacts badly with unquoted attribute values.
12.728-12.796: error: Bad value “handheld” for attribute “media” on element “link”: The media “handheld” has been deprecated
21.417-21.473: error: Attribute “name” not allowed on element “script” at this point.
21.25747-21.25895: error: Attribute “autocorrect” not allowed on element “input” at this point.
21.25980-21.26033: error: Attribute “viewBox” not allowed on element “g” at this point.
21.30451-21.30472: error: Duplicate ID “youtube-paths”.
21.27048-21.27069: info warning: The first occurrence of ID “youtube-paths” was here.
23.15-23.210: error: Attribute “name” not allowed on element “link” at this point.
23.3336-23.3350: error: Duplicate ID “menu”.
21.25980-21.26033: info warning: The first occurrence of ID “menu” was here.

$ tidy -errors youtube.com.html
line 21 column 337 - Warning: unescaped & or unknown entity "&family"
line 21 column 371 - Warning: unescaped & or unknown entity "&display"
line 21 column 25502 - Error: &lt;ytd-app&gt; is not recognized! Did you mean to enable the custom-tags option?
line 21 column 25502 - Warning: discarding unexpected &lt;ytd-app&gt;
line 21 column 25511 - Error: &lt;ytd-masthead&gt; is not recognized! Did you mean to enable the custom-tags option?
line 21 column 25511 - Warning: discarding unexpected &lt;ytd-masthead&gt;
line 21 column 32909 - Warning: discarding unexpected &lt;/ytd-masthead&gt;
line 21 column 34720 - Warning: discarding unexpected &lt;/ytd-app&gt;
line 1 column 16 - Warning: &lt;html&gt; proprietary attribute "darker-dark-theme"
line 1 column 16 - Warning: &lt;html&gt; proprietary attribute "darker-dark-theme-deprecate"
line 1 column 16 - Warning: &lt;html&gt; proprietary attribute "system-icons"
line 1 column 16 - Warning: &lt;html&gt; proprietary attribute "typography"
line 1 column 16 - Warning: &lt;html&gt; proprietary attribute "typography-spacing"
line 1 column 16 - Warning: &lt;html&gt; proprietary attribute "refresh"
line 1 column 202 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 1 column 1024 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 2 column 153 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 11 column 10 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 12 column 1487 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 12 column 1643 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 17 column 10 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 17 column 139 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 17 column 310 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 17 column 475 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 17 column 618 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 17 column 783 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 17 column 887 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 20 column 10 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 20 column 114 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 20 column 247 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 20 column 404 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 20 column 525 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 10 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 139 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 242 - Warning: &lt;link&gt; proprietary attribute "nonce"
line 21 column 417 - Warning: &lt;script&gt; proprietary attribute "name"
line 21 column 417 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 615 - Warning: &lt;link&gt; proprietary attribute "nonce"
line 21 column 766 - Warning: &lt;link&gt; proprietary attribute "nonce"
line 21 column 893 - Warning: &lt;link&gt; proprietary attribute "nonce"
line 21 column 1097 - Warning: &lt;style&gt; proprietary attribute "nonce"
line 21 column 1424 - Warning: &lt;style&gt; proprietary attribute "nonce"
line 21 column 4559 - Warning: &lt;style&gt; proprietary attribute "nonce"
line 21 column 5413 - Warning: &lt;style&gt; proprietary attribute "nonce"
line 21 column 6312 - Warning: &lt;style&gt; proprietary attribute "nonce"
line 21 column 6837 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 6940 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 24741 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 24867 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 24969 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 25080 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 25747 - Warning: &lt;input&gt; proprietary attribute "autocapitalize"
line 21 column 25747 - Warning: &lt;input&gt; proprietary attribute "autocorrect"
line 21 column 44980 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 45083 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 45188 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 45296 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 45401 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 45607 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 45715 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 45823 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 45927 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 46029 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 46361 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 21 column 82820 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 23 column 15 - Warning: &lt;link&gt; proprietary attribute "name"
line 23 column 15 - Warning: &lt;link&gt; proprietary attribute "nonce"
line 23 column 4056 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 23 column 4159 - Warning: &lt;script&gt; proprietary attribute "nonce"
line 23 column 4304 - Warning: &lt;script&gt; proprietary attribute "nonce"

$ htmlhint youtube.com.html
L21 |... height="18" viewBox="0 0 104 18"&gt;&lt;defs&gt;&lt;clipPath id="clip0_161_5084"&gt;&lt;rect width="104" height="18"/&gt;...
                                                ^ The html element name of [ clipPath ] must be in lowercase. (tagname-lowercase)
L21 |...61_5084"&gt;&lt;rect width="104" height="18"/&gt;&lt;/clipPath&gt;&lt;/defs&gt;&lt;g clip-path="url(#clip0_161_5084)"&gt;&lt;path d...
                                                ^ The html element name of [ clipPath ] must be in lowercase. (tagname-lowercase)
L21 |... height="18" viewBox="0 0 111 18"&gt;&lt;defs&gt;&lt;clipPath id="clip0_161_5078"&gt;&lt;rect width="111" height="18"/&gt;...
                                                ^ The html element name of [ clipPath ] must be in lowercase. (tagname-lowercase)
L21 |...61_5078"&gt;&lt;rect width="111" height="18"/&gt;&lt;/clipPath&gt;&lt;/defs&gt;&lt;g clip-path="url(#clip0_161_5078)"&gt;&lt;path d...
                                                ^ The html element name of [ clipPath ] must be in lowercase. (tagname-lowercase)
L21 |...18" stroke="grey" stroke-width="0.5"/&gt;&lt;g id="youtube-paths"&gt;&lt;path d="M30.125 0.570001V17.57H32.915V11...
                                                ^ The id value [ youtube-paths ] must be unique. (id-unique)
L23 |...or"&gt;&lt;/div&gt;&lt;div class="flex-1"&gt;&lt;/div&gt;&lt;div id="menu"&gt;&lt;div class="menu-button skeleton-bg-color"&gt;&lt;/div&gt;&lt;...
                                                ^ The id value [ menu ] must be unique. (id-unique)

$ html-validate youtube.com.html
 1:22     error  Inline style is not allowed                                              no-inline-style
 1:738    error  Expected omitted end tag &lt;meta&gt; instead of self-closing element &lt;meta/&gt;  void-style
 1:1022   error  Expected omitted end tag &lt;meta&gt; instead of self-closing element &lt;meta/&gt;  void-style
21:25183  error  &lt;iframe&gt; is missing required "title" attribute                           element-required-attributes
21:34920  error  Inline style is not allowed                                              no-inline-style
21:35340  error  Inline style is not allowed                                              no-inline-style
21:35760  error  Inline style is not allowed                                              no-inline-style
21:36180  error  Inline style is not allowed                                              no-inline-style
21:36600  error  Inline style is not allowed                                              no-inline-style
21:37020  error  Inline style is not allowed                                              no-inline-style
21:37440  error  Inline style is not allowed                                              no-inline-style
21:37860  error  Inline style is not allowed                                              no-inline-style
21:38280  error  Inline style is not allowed                                              no-inline-style
21:38700  error  Inline style is not allowed                                              no-inline-style
21:39120  error  Inline style is not allowed                                              no-inline-style
21:39540  error  Inline style is not allowed                                              no-inline-style
21:39960  error  Inline style is not allowed                                              no-inline-style
21:40380  error  Inline style is not allowed                                              no-inline-style
21:40800  error  Inline style is not allowed                                              no-inline-style
21:41220  error  Inline style is not allowed                                              no-inline-style
21:41640  error  Inline style is not allowed                                              no-inline-style
21:42060  error  Inline style is not allowed                                              no-inline-style
21:42480  error  Inline style is not allowed                                              no-inline-style
21:42900  error  Inline style is not allowed                                              no-inline-style
21:43320  error  Inline style is not allowed                                              no-inline-style
21:43740  error  Inline style is not allowed                                              no-inline-style
21:44160  error  Inline style is not allowed                                              no-inline-style
21:44580  error  Inline style is not allowed                                              no-inline-style

$ linthtml youtube.com.html
...redacted for brevity...

$ eslint youtube.com.html
...redacted for brevity...</code></pre>
</details>

<details>
  <summary>MDN Learning Area</summary>
  <pre><code>$ vnu --Werror mdn-learning-area/html/forms/datetime-local-picker-fallback/index.html
1.1-4.86: error: Non-space characters found without seeing a doctype first. Expected “&lt;!DOCTYPE html&gt;”.
1.1-4.86: error: Element “head” is missing a required instance of child element “title”.
1.1-4.86: info warning: Consider adding a “lang” attribute to the “html” start tag to declare the language of this document.

$ tidy -errors mdn-learning-area/html/forms/datetime-local-picker-fallback/index.html
line 29 column 7 - Warning: trimming empty &lt;span&gt;

$ html-validate mdn-learning-area/html/forms/datetime-local-picker-fallback/index.html
 1:1  error  DOCTYPE should be uppercase               doctype-style
25:4  error  &lt;form&gt; element must have a submit button  wcag/h32

$ eslint mdn-learning-area/html/forms/datetime-local-picker-fallback/index.html
...redacted for brevity...</code></pre>
</details>

<details>
  <summary>Bootstrap album example</summary>
  <pre><code>$ tidy -errors bootstrap-5.0.2-examples/album/index.html
line 64 column 9 - Warning: trimming empty &lt;span&gt;
line 63 column 7 - Warning: trimming empty &lt;button&gt;
line 91 column 13 - Warning: &lt;svg&gt; proprietary attribute "focusable"
line 107 column 13 - Warning: &lt;svg&gt; proprietary attribute "focusable"
line 123 column 13 - Warning: &lt;svg&gt; proprietary attribute "focusable"
line 140 column 13 - Warning: &lt;svg&gt; proprietary attribute "focusable"
line 156 column 13 - Warning: &lt;svg&gt; proprietary attribute "focusable"
line 172 column 13 - Warning: &lt;svg&gt; proprietary attribute "focusable"
line 189 column 13 - Warning: &lt;svg&gt; proprietary attribute "focusable"
line 205 column 13 - Warning: &lt;svg&gt; proprietary attribute "focusable"
line 221 column 13 - Warning: &lt;svg&gt; proprietary attribute "focusable"

$ htmlhint bootstrap-5.0.2-examples/album/index.html
 1:1  error  DOCTYPE should be uppercase  doctype-style
 13:1  error  Trailing whitespace         no-trailing-whitespace
 34:1  error  Trailing whitespace         no-trailing-whitespace
 37:1  error  Trailing whitespace         no-trailing-whitespace
254:1  error  Trailing whitespace         no-trailing-whitespace

$ linthtml bootstrap-5.0.2-examples/album/index.html
...redacted for brevity...

$ eslint bootstrap-5.0.2-examples/album/index.html
...redacted for brevity...</code></pre>
</details>

<details>
  <summary>Foundation web framework</summary>
  <pre><code>$ vnu --Werror foundation-sites-templates/index.html
4.5-4.28: info: Trailing slash on void elements has no effect and interacts badly with unquoted attribute values.
5.5-5.76: info: Trailing slash on void elements has no effect and interacts badly with unquoted attribute values.
39.11-39.68: error: An “img” element must have an “alt” attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.
51.11-51.68: error: An “img” element must have an “alt” attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.
63.11-63.68: error: An “img” element must have an “alt” attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.
75.11-75.68: error: An “img” element must have an “alt” attribute, except under certain conditions. For details, consult guidance on providing text alternatives for images.
107.7-107.71: error: Bad value “navigation” for attribute “role” on element “ul”.

$ tidy -errors foundation-sites-templates/index.html
line 39 column 11 - Warning: &lt;img&gt; lacks "alt" attribute
line 51 column 11 - Warning: &lt;img&gt; lacks "alt" attribute
line 63 column 11 - Warning: &lt;img&gt; lacks "alt" attribute
line 75 column 11 - Warning: &lt;img&gt; lacks "alt" attribute
line 113 column 9 - Warning: trimming empty &lt;li&gt;

$ htmlhint foundation-sites-templates/index.html
 1:1   error  DOCTYPE should be uppercase                                              doctype-style
 4:27  error  Expected omitted end tag &lt;meta&gt; instead of self-closing element &lt;meta/&gt;  void-style
 5:75  error  Expected omitted end tag &lt;meta&gt; instead of self-closing element &lt;meta/&gt;  void-style
 39:12  error  &lt;img&gt; is missing required "alt" attribute                               wcag/h37
 51:12  error  &lt;img&gt; is missing required "alt" attribute                               wcag/h37
 63:12  error  &lt;img&gt; is missing required "alt" attribute                               wcag/h37
 75:12  error  &lt;img&gt; is missing required "alt" attribute                               wcag/h37
107:30  error  Prefer to use the native &lt;nav&gt; element                                  prefer-native-element

$ linthtml foundation-sites-templates/index.html
  2:13  error    The value "no-js" of attribute "class" does not respect the format: underscore                                                  id-class-style
  3:3   error    Incorrect indentation for `head` beginning at L3:C3. Expected `&lt;head&gt;` to be at an indentation of 4 but was found at 2.         indent-style
  4:5   error    Incorrect indentation for `meta` beginning at L4:C5. Expected `&lt;meta&gt;` to be at an indentation of 8 but was found at 4.         indent-style
  5:5   error    Incorrect indentation for `meta` beginning at L5:C5. Expected `&lt;meta&gt;` to be at an indentation of 8 but was found at 4.         indent-style
  6:5   error    Incorrect indentation for `title` beginning at L6:C5. Expected `&lt;title&gt;` to be at an indentation of 8 but was found at 4.       indent-style
  7:5   error    Incorrect indentation for `link` beginning at L7:C5. Expected `&lt;link&gt;` to be at an indentation of 8 but was found at 4.         indent-style
  9:3   error    Incorrect indentation for `body` beginning at L9:C3. Expected `&lt;body&gt;` to be at an indentation of 4 but was found at 2.         indent-style
 11:5   error    Incorrect indentation for `Comment` beginning at L11:C5. Expected `&lt;Comment&gt;` to be at an indentation of 8 but was found at 4.  indent-style
 12:5   error    Incorrect indentation for `div` beginning at L12:C5. Expected `&lt;div&gt;` to be at an indentation of 8 but was found at 4.          indent-style
 12:16  error    The value "top-bar" of attribute "class" does not respect the format: underscore                                                id-class-style
 13:7   error    Incorrect indentation for `div` beginning at L13:C7. Expected `&lt;div&gt;` to be at an indentation of 12 but was found at 6.         indent-style
 13:18  error    The value "top-bar-left" of attribute "class" does not respect the format: underscore                                           id-class-style
 14:9   error    Incorrect indentation for `ul` beginning at L14:C9. Expected `&lt;ul&gt;` to be at an indentation of 16 but was found at 8.           indent-style
 15:11  error    Incorrect indentation for `li` beginning at L15:C11. Expected `&lt;li&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 15:21  error    The value "menu-text" of attribute "class" does not respect the format: underscore                                              id-class-style
 18:7   error    Incorrect indentation for `div` beginning at L18:C7. Expected `&lt;div&gt;` to be at an indentation of 12 but was found at 6.         indent-style
 18:18  error    The value "top-bar-right" of attribute "class" does not respect the format: underscore                                          id-class-style
 19:9   error    Incorrect indentation for `ul` beginning at L19:C9. Expected `&lt;ul&gt;` to be at an indentation of 16 but was found at 8.           indent-style
 20:11  error    Incorrect indentation for `li` beginning at L20:C11. Expected `&lt;li&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 21:11  error    Incorrect indentation for `li` beginning at L21:C11. Expected `&lt;li&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 22:11  error    Incorrect indentation for `li` beginning at L22:C11. Expected `&lt;li&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 23:11  error    Incorrect indentation for `li` beginning at L23:C11. Expected `&lt;li&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 27:5   error    Incorrect indentation for `Comment` beginning at L27:C5. Expected `&lt;Comment&gt;` to be at an indentation of 8 but was found at 4.  indent-style
 29:5   error    Incorrect indentation for `div` beginning at L29:C5. Expected `&lt;div&gt;` to be at an indentation of 8 but was found at 4.          indent-style
 30:7   error    Incorrect indentation for `div` beginning at L30:C7. Expected `&lt;div&gt;` to be at an indentation of 12 but was found at 6.         indent-style
 30:18  error    The value "text-center" of attribute "class" does not respect the format: underscore                                            id-class-style
 31:9   error    Incorrect indentation for `h1` beginning at L31:C9. Expected `&lt;h1&gt;` to be at an indentation of 16 but was found at 8.           indent-style
 35:5   error    Incorrect indentation for `div` beginning at L35:C5. Expected `&lt;div&gt;` to be at an indentation of 8 but was found at 4.          indent-style
 36:7   error    Incorrect indentation for `div` beginning at L36:C7. Expected `&lt;div&gt;` to be at an indentation of 12 but was found at 6.         indent-style
 36:18  error    The value "medium-8" of attribute "class" does not respect the format: underscore                                               id-class-style
 37:9   error    Incorrect indentation for `div` beginning at L37:C9. Expected `&lt;div&gt;` to be at an indentation of 16 but was found at 8.         indent-style
 37:20  error    The value "blog-post" of attribute "class" does not respect the format: underscore                                              id-class-style
 38:11  error    Incorrect indentation for `h3` beginning at L38:C11. Expected `&lt;h3&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 39:11  error    Incorrect indentation for `img` beginning at L39:C11. Expected `&lt;img&gt;` to be at an indentation of 20 but was found at 10.       indent-style
 39:11  error    The "alt" attribute must be set for &lt;img&gt; tag                                                                                   img-req-alt
 40:11  error    Incorrect indentation for `p` beginning at L40:C11. Expected `&lt;p&gt;` to be at an indentation of 20 but was found at 10.           indent-style
 41:11  error    Incorrect indentation for `div` beginning at L41:C11. Expected `&lt;div&gt;` to be at an indentation of 20 but was found at 10.       indent-style
 42:13  error    Incorrect indentation for `ul` beginning at L42:C13. Expected `&lt;ul&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 43:15  error    Incorrect indentation for `li` beginning at L43:C15. Expected `&lt;li&gt;` to be at an indentation of 28 but was found at 14.         indent-style
 44:15  error    Incorrect indentation for `li` beginning at L44:C15. Expected `&lt;li&gt;` to be at an indentation of 28 but was found at 14.         indent-style
 49:9   error    Incorrect indentation for `div` beginning at L49:C9. Expected `&lt;div&gt;` to be at an indentation of 16 but was found at 8.         indent-style
 49:20  error    The value "blog-post" of attribute "class" does not respect the format: underscore                                              id-class-style
 50:11  error    Incorrect indentation for `h3` beginning at L50:C11. Expected `&lt;h3&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 51:11  error    Incorrect indentation for `img` beginning at L51:C11. Expected `&lt;img&gt;` to be at an indentation of 20 but was found at 10.       indent-style
 51:11  error    The "alt" attribute must be set for &lt;img&gt; tag                                                                                   img-req-alt
 52:11  error    Incorrect indentation for `p` beginning at L52:C11. Expected `&lt;p&gt;` to be at an indentation of 20 but was found at 10.           indent-style
 53:11  error    Incorrect indentation for `div` beginning at L53:C11. Expected `&lt;div&gt;` to be at an indentation of 20 but was found at 10.       indent-style
 54:13  error    Incorrect indentation for `ul` beginning at L54:C13. Expected `&lt;ul&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 55:15  error    Incorrect indentation for `li` beginning at L55:C15. Expected `&lt;li&gt;` to be at an indentation of 28 but was found at 14.         indent-style
 56:15  error    Incorrect indentation for `li` beginning at L56:C15. Expected `&lt;li&gt;` to be at an indentation of 28 but was found at 14.         indent-style
 61:9   error    Incorrect indentation for `div` beginning at L61:C9. Expected `&lt;div&gt;` to be at an indentation of 16 but was found at 8.         indent-style
 61:20  error    The value "blog-post" of attribute "class" does not respect the format: underscore                                              id-class-style
 62:11  error    Incorrect indentation for `h3` beginning at L62:C11. Expected `&lt;h3&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 63:11  error    Incorrect indentation for `img` beginning at L63:C11. Expected `&lt;img&gt;` to be at an indentation of 20 but was found at 10.       indent-style
 63:11  error    The "alt" attribute must be set for &lt;img&gt; tag                                                                                   img-req-alt
 64:11  error    Incorrect indentation for `p` beginning at L64:C11. Expected `&lt;p&gt;` to be at an indentation of 20 but was found at 10.           indent-style
 65:11  error    Incorrect indentation for `div` beginning at L65:C11. Expected `&lt;div&gt;` to be at an indentation of 20 but was found at 10.       indent-style
 66:13  error    Incorrect indentation for `ul` beginning at L66:C13. Expected `&lt;ul&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 67:15  error    Incorrect indentation for `li` beginning at L67:C15. Expected `&lt;li&gt;` to be at an indentation of 28 but was found at 14.         indent-style
 68:15  error    Incorrect indentation for `li` beginning at L68:C15. Expected `&lt;li&gt;` to be at an indentation of 28 but was found at 14.         indent-style
 73:9   error    Incorrect indentation for `div` beginning at L73:C9. Expected `&lt;div&gt;` to be at an indentation of 16 but was found at 8.         indent-style
 73:20  error    The value "blog-post" of attribute "class" does not respect the format: underscore                                              id-class-style
 74:11  error    Incorrect indentation for `h3` beginning at L74:C11. Expected `&lt;h3&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 75:11  error    Incorrect indentation for `img` beginning at L75:C11. Expected `&lt;img&gt;` to be at an indentation of 20 but was found at 10.       indent-style
 75:11  error    The "alt" attribute must be set for &lt;img&gt; tag                                                                                   img-req-alt
 76:11  error    Incorrect indentation for `p` beginning at L76:C11. Expected `&lt;p&gt;` to be at an indentation of 20 but was found at 10.           indent-style
 77:11  error    Incorrect indentation for `div` beginning at L77:C11. Expected `&lt;div&gt;` to be at an indentation of 20 but was found at 10.       indent-style
 78:13  error    Incorrect indentation for `ul` beginning at L78:C13. Expected `&lt;ul&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 79:15  error    Incorrect indentation for `li` beginning at L79:C15. Expected `&lt;li&gt;` to be at an indentation of 28 but was found at 14.         indent-style
 80:15  error    Incorrect indentation for `li` beginning at L80:C15. Expected `&lt;li&gt;` to be at an indentation of 28 but was found at 14.         indent-style
 85:7   error    Incorrect indentation for `div` beginning at L85:C7. Expected `&lt;div&gt;` to be at an indentation of 12 but was found at 6.         indent-style
 85:37  error    The attribute "data-sticky-container" requires a value                                                                          attr-req-value
 85:18  error    The value "medium-3" of attribute "class" does not respect the format: underscore                                               id-class-style
 86:9   error    Incorrect indentation for `div` beginning at L86:C9. Expected `&lt;div&gt;` to be at an indentation of 16 but was found at 8.         indent-style
 86:29  error    The attribute "data-sticky" requires a value                                                                                    attr-req-value
 87:11  error    Incorrect indentation for `h4` beginning at L87:C11. Expected `&lt;h4&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 88:11  error    Incorrect indentation for `ul` beginning at L88:C11. Expected `&lt;ul&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 89:13  error    Incorrect indentation for `li` beginning at L89:C13. Expected `&lt;li&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 90:13  error    Incorrect indentation for `li` beginning at L90:C13. Expected `&lt;li&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 91:13  error    Incorrect indentation for `li` beginning at L91:C13. Expected `&lt;li&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 92:13  error    Incorrect indentation for `li` beginning at L92:C13. Expected `&lt;li&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 95:11  error    Incorrect indentation for `h4` beginning at L95:C11. Expected `&lt;h4&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 96:11  error    Incorrect indentation for `ul` beginning at L96:C11. Expected `&lt;ul&gt;` to be at an indentation of 20 but was found at 10.         indent-style
 97:13  error    Incorrect indentation for `li` beginning at L97:C13. Expected `&lt;li&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 98:13  error    Incorrect indentation for `li` beginning at L98:C13. Expected `&lt;li&gt;` to be at an indentation of 24 but was found at 12.         indent-style
 99:13  error    Incorrect indentation for `li` beginning at L99:C13. Expected `&lt;li&gt;` to be at an indentation of 24 but was found at 12.         indent-style
100:13  error    Incorrect indentation for `li` beginning at L100:C13. Expected `&lt;li&gt;` to be at an indentation of 24but was found at 12.        indent-style
106:5   error    Incorrect indentation for `div` beginning at L106:C5. Expected `&lt;div&gt;` to be at an indentation of 8but was found at 4.         indent-style
107:7   error    Incorrect indentation for `ul` beginning at L107:C7. Expected `&lt;ul&gt;` to be at an indentation of 12but was found at 6.          indent-style
108:9   error    Incorrect indentation for `li` beginning at L108:C9. Expected `&lt;li&gt;` to be at an indentation of 16but was found at 8.          indent-style
109:9   error    Incorrect indentation for `li` beginning at L109:C9. Expected `&lt;li&gt;` to be at an indentation of 16but was found at 8.          indent-style
109:41  error    The value "show-for-sr" of attribute "class" does not respect the format:underscore                                            id-class-style
110:9   error    Incorrect indentation for `li` beginning at L110:C9. Expected `&lt;li&gt;` to be at an indentation of 16but was found at 8.          indent-style
111:9   error    Incorrect indentation for `li` beginning at L111:C9. Expected `&lt;li&gt;` to be at an indentation of 16but was found at 8.          indent-style
112:9   error    Incorrect indentation for `li` beginning at L112:C9. Expected `&lt;li&gt;` to be at an indentation of 16but was found at 8.          indent-style
113:9   error    Incorrect indentation for `li` beginning at L113:C9. Expected `&lt;li&gt;` to be at an indentation of 16but was found at 8.          indent-style
114:9   error    Incorrect indentation for `li` beginning at L114:C9. Expected `&lt;li&gt;` to be at an indentation of 16but was found at 8.          indent-style
115:9   error    Incorrect indentation for `li` beginning at L115:C9. Expected `&lt;li&gt;` to be at an indentation of 16but was found at 8.          indent-style
116:9   error    Incorrect indentation for `li` beginning at L116:C9. Expected `&lt;li&gt;` to be at an indentation of 16but was found at 8.          indent-style
120:5   error    Incorrect indentation for `script` beginning at L120:C5. Expected `&lt;script&gt;` to be at an indentation of 8 but was found at 4.   indent-style
121:5   error    Incorrect indentation for `script` beginning at L121:C5. Expected `&lt;script&gt;` to be at an indentation of 8 but was found at 4.   indent-style
122:5   error    Incorrect indentation for `script` beginning at L122:C5. Expected `&lt;script&gt;` to be at an indentation of 8 but was found at 4.   indent-style

$ eslint foundation-sites-templates/index.html
...redacted for brevity...</code></pre>
</details>

Second, I fed the HTML linters some common & "problematic" HTML mistakes,
to see if they were able to detect them.

The HTML file tested can be found there: [horribly-broken-page.html](https://github.com/Lucas-C/ludochaordic/blob/master/content/test-html-linters/horribly-broken-page.html). It is served over HTTP there: [horribly-broken-page.html](https://chezsoi.org/lucas/blog/test-html-linters/horribly-broken-page.html).

The table below lists, for each issue of this HTML test file, if each linter is able to detect it:

HTML linters: | [W3C v.Nu checker](https://validator.github.io/validator/) | [html-tidy](https://www.html-tidy.org/) | [htmlhint](https://htmlhint.com/) | [html-validate](https://html-validate.org/) | [LintHTML](https://linthtml.vercel.app/) | [html-eslint](https://html-eslint.org/)
-|-|-|-|-|-|-
No `DOCTYPE` | ✅ | ✅ | ✅ | ❌ | ❌ | ❌
No `lang` attribute | ✅ | ❌ | ❌ | ❌ | ❌ | ❌
No `<title>` | ✅ | ❌ | ❌ | ❌ | ❌ | ❌
No explicit `<body>` | ❌ | ✅ | ❌ | ❌ | ❌ | ❌
`<link>` with missing required attributes | ✅ | ❌ | ❌ | ✅ | ❌ | ❌
Multiple `<main> blocks` | ✅ | ✅ | ❌ | ✅ | ❌ | ❌
Unknown HTML tag | ✅ | ✅ | ❌ | ✅ | ❌ | ❌
Tag in UPPERCASE | ❌ | ❌ | ✅ | ✅ | ✅ | ❌
Stray end tag | ✅ | ❌ | ❌ | ✅ | ❌ | ❌
Empty ID attribute | ✅ | ❌ | ❌ | ✅ | ✅ | ❌
Duplicate IDs | ✅ | ❌ | ✅ | ✅ | ✅ | ✅
Duplicate attribute | ✅ | ❌ | ✅ | ✅ | ✅ | ✅
Deprecated attribute | ✅ | ❌ | ❌ | ❌ | ✅ | ❌
Empty `<figure>` tag in body | ❌ | ❌ | ❌ | ❌ | ❌ | ❌
`figcaption` without `figure` parent | ✅ | ❌ | ❌ | ❌ | ❌ | ❌
Invalid item within list | ✅ | ❌ | ✅ | ✅ | ✅ | ✅
Improperly nested `div`, inside `p` | ❌ | ❌ | ❌ | ✅ | ❌ | ❌
`dt`/`dd` without correct parent | ✅ | ❌ | ❌ | ✅ | ❌ | ❌

Of course this is not exhaustive: some linters include hundreds of checks!
There is some "select bias" due to the fact that I selected some specific HTML issues.

Analysis details:
<details>
  <summary>horribly-broken-page.html</summary>
  <pre><code>$ vnu --Werror content/test-html-linters/run-all-html-linters.sh
1.34-2.7: error: Start tag seen without seeing a doctype first. Expected “&lt;!DOCTYPE html&gt;”.
1.34-2.7: error: Element “link” is missing one or more of the following attributes: “href”, “itemprop”, “property”, “rel”, “resource”.
1.34-2.7: error: A “link” element must have an “href” or “imagesrcset” attribute, or both.
5.1-5.6: error: Element “head” is missing a required instance of child element “title”.
6.1-6.6: error: A document must not include more than one visible “main” element.
9.1-9.7: error: Element “dummy” not allowed as child of element “body” in this context. (Suppressing further errors from this subtree.)
15.1-15.10: error: Stray end tag “section”.
18.1-18.11: error: Bad value “” for attribute “id” on element “div”: An ID must not be the empty string.
22.1-22.15: error: Duplicate ID “MyID”.
21.1-21.15: info warning: The first occurrence of ID “MyID” was here.
25.1-25.17: error: Duplicate attribute “foo”.
25.1-25.23: error: Attribute “foo” not allowed on element “p” at this point.
27.1-27.17: error: Attribute “bgcolor” not allowed on element “p” at this point.
32.1-32.12: error: Element “figcaption” not allowed as child of element “body” in this context. (Suppressing further errors from this subtree.)
37.3-37.5: error: Element “p” not allowed as child of element “ul” in this context. (Suppressing further errors from this subtree.)
47.1-47.4: error: No “p” element in scope but a “p” end tag seen.
49.1-49.4: error: Element “dt” not allowed as child of element “body” in this context. (Suppressing further errors from this subtree.)
53.1-53.4: error: Element “dd” not allowed as child of element “body” in this context. (Suppressing further errors from this subtree.)
1.34-2.7: info warning: Consider adding a “lang” attribute to the “html” start tag to declare the language of this document.

$ tidy -errors content/test-html-linters/horribly-broken-page.html
line 2 column 1 - Warning: missing &lt;!DOCTYPE&gt; declaration
line 5 column 1 - Warning: inserting implicit &lt;body&gt;
line 6 column 1 - Error: discarding unexpected &lt;main&gt;
line 6 column 37 - Error: discarding unexpected &lt;/main&gt;
line 9 column 1 - Error: &lt;dummy&gt; is not recognized!
line 9 column 1 - Error: discarding unexpected &lt;dummy&gt;
line 9 column 8 - Error: discarding unexpected &lt;/dummy&gt;

$ htmlhint content/test-html-linters/horribly-broken-page.html
L1 |&lt;!-- Empty `link` tag in body --&gt;
    ^ Doctype must be declared first. (doctype-first)
L12 |&lt;SPAN&gt;Tag in UPPERCASE&lt;/SPAN&gt;
     ^ The html element name of [ SPAN ] must be in lowercase. (tagname-lowercase)
L12 |&lt;SPAN&gt;Tag in UPPERCASE&lt;/SPAN&gt;
                           ^ The html element name of [ SPAN ] must be in lowercase. (tagname-lowercase)
L22 |&lt;div id="MyID"&gt;&lt;code&gt;div&lt;/code&gt; with ID &lt;code&gt;MyId&lt;/code&gt;&lt;/div&gt;
         ^ The id value [ MyID ] must be unique. (id-unique)
L25 |&lt;p foo="bar" foo="baz"&gt;This paragraph has a duplicate unknown attribute&lt;/p&gt;
                 ^ Duplicate of attribute name [ foo ] was found. (attr-no-duplication)
L41 |&lt;/ul&gt;
     ^ Tag must be paired, missing: [ &lt;/li&gt; ], start tag match failed [ &lt;li&gt; ] on line 40. (tag-pair)

$ html-validate content/test-html-linters/horribly-broken-page.html
 2:2   error  &lt;link&gt; is missing required "href" attribute                                                 element-required-attributes
 5:2   error  Landmarks must have a non-empty and unique accessible name (aria-label or aria-labelledby)  unique-landmark
 6:2   error  Multiple &lt;main&gt; elements present in document                                                no-multiple-main
 6:2   error  Landmarks must have a non-empty and unique accessible name (aria-label or aria-labelledby)  unique-landmark
 9:2   error  &lt;dummy&gt; is not a valid element name                                                         element-name
12:2   error  Element "SPAN" should be lowercase                                                          element-case
15:2   error  Stray end tag '&lt;/section&gt;'                                                                  close-order
18:6   error  element id "" must not be empty                                                             valid-id
18:6   error  Attribute "id" has invalid value ""                                                         attribute-allowed-values
22:10  error  Duplicate ID "MyID"                                                                         no-dup-id
25:14  error  Attribute "foo" duplicated                                                                  no-dup-attr
37:4   error  &lt;p&gt; element is not permitted as content under &lt;ul&gt;                                          element-permitted-content
40:4   error  Element &lt;li&gt; is implicitly closed by parent &lt;/ul&gt;                                           no-implicit-close
43:2   error  Element &lt;p&gt; is implicitly closed by adjacent &lt;div&gt;                                          no-implicit-close
47:2   error  Stray end tag '&lt;/p&gt;'                                                                        close-order
49:2   error  &lt;dt&gt; element requires a "dl &gt; dt" or "dl &gt; div &gt; dt" ancestor                               element-required-ancestor
53:2   error  &lt;dd&gt; element requires a "dl &gt; dd" or "dl &gt; div &gt; dd" ancestor                               element-required-ancestor

$ linthtml content/test-html-linters/horribly-broken-page.html
12:1  error    Invalid case for tag &lt;span&gt;, tag names must be written in lowercase                                                       tag-name-lowercase
18:6  error    The attribute "id" requires a value                                                                                       attr-req-value
21:6  error    The value "MyID" of attribute "id" does not respect the format:underscore                                                id-class-style
22:9  error    The id "MyID" is already used atL21:c9                                                                                   id-no-dup
22:6  error    The value "MyID" of attribute "id" does not respect the format:underscore                                                id-class-style
25:4  error    The attribute foo is duplicated                                                                                           attr-no-dup
27:4  error    The attribute "bgcolor" attribute is cannot be used as it's banned                                                        attr-bans
37:3  error    Incorrect indentation for `p` beginning at L37:C3. Expected `&lt;p&gt;` to be at an indentation of 4 but was found at 2.        indent-style
40:3  error    Incorrect indentation for `li` beginning at L40:C3. Expected `&lt;li&gt;` to be at an indentation of 4 but was found at 2.      indent-style
40:3  error    Tag is not closed                                                                                                        tag-close
44:3  error    Incorrect indentation for `p` beginning at L44:C3. Expected `&lt;\p&gt;` to be at an indentation of 0 but was found at 2.       indent-style
43:1  error    Tag is not closed                                                                                                        tag-close
47:1  error    Tag close does not match opened tag atC47:L1                                                                             tag-name-match
50:3  error    Incorrect indentation for `code` beginning at L50:C3. Expected `&lt;code&gt;` to be at an indentation of 4but was found at 2.  indent-style
54:3  error    Incorrect indentation for `code` beginning at L54:C3. Expected `&lt;code&gt;` to be at an indentation of 4 but was found at 2.  indent-style

$ eslint content/test-html-linters/horribly-broken-page.html
21:10  error  The id 'MyID' is duplicated                          @html-eslint/no-duplicate-id
22:10  error  The id 'MyID' is duplicated                          @html-eslint/no-duplicate-id
25:14  error  The attribute 'foo' is duplicated                    @html-eslint/no-duplicate-attrs
33:1   error  Expected indentation of 4 space but found 2 space    @html-eslint/indent
36:1   error  Missing closing tag for ul                           @html-eslint/require-closing-tags
37:1   error  Expected indentation of 4 space but found 2 space    @html-eslint/indent
38:1   error  Expected indentation of 8 space but found 4 space    @html-eslint/indent
39:1   error  Expected indentation of 4 space but found 2 space    @html-eslint/indent
40:1   error  Expected indentation of 4 space but found 2 space    @html-eslint/indent
40:3   error  Missing closing tag for li                           @html-eslint/require-closing-tags
43:1   error  Expected indentation of 8 space but found no indent  @html-eslint/indent
44:1   error  Expected indentation of 12 space but found 2 space   @html-eslint/indent
45:1   error  Expected indentation of 16 space but found 4 space   @html-eslint/indent
46:1   error  Expected indentation of 12 space but found 2 space   @html-eslint/indent
47:1   error  Expected indentation of 8 space but found no indent  @html-eslint/indent
49:1   error  Expected indentation of 8 space but found no indent  @html-eslint/indent
50:1   error  Expected indentation of 12 space but found 2 space   @html-eslint/indent
51:1   error  Expected indentation of 8 space but found no indent  @html-eslint/indent
53:1   error  Expected indentation of 8 space but found no indent  @html-eslint/indent
54:1   error  Expected indentation of 12 space but found 2 space   @html-eslint/indent
55:1   error  Expected indentation of 8 space but found no indent  @html-eslint/indent</code></pre>
</details>


## Conclusion
Overall, **I would recommend using the [W3C v.Nu checker](https://validator.github.io/validator/)**:
apart from its (relative) slowness,
it's actively maintained, easy to setup in a CI pipeline and to whitelist some issues,
while still getting relevant warnings with a wide range of checks.

However, note that "HTML linting" is very wide,
and can cover all of the following goals:

* homogenize HTML **code formatting**
* detect HTML syntax **critical issues**, that could "break" content rendering
* detect security issues in HTML code (_e.g._ related to `<script>` or `<iframe>` usages)
* detect [accessibility](https://en.wikipedia.org/wiki/Web_accessibility) issues in HTML code
* recommend "best practices", about HTML5 / document structure / accessibility / etc.

In the spirit of the _"Do one thing and do it well"_ Linux principle,
maybe the best approach should be to have "specialized" HTML linters that only address some of those specific areas, and combine them?

### Related tools & readings
* There are also linters for HTML sub-languages & templates (_e.g._ [pug-lint](https://github.com/pugjs/pug-lint), [djlint](https://www.djlint.com/fr/), [jinjalint](https://github.com/motet-a/jinjalint), [ejs-lint](https://www.npmjs.com/package/ejs-lint), [ember-template-lint](https://github.com/ember-template-lint/ember-template-lint)...) or even web frameworks (_e.g._ [bootlint](https://github.com/twbs/bootlint), [`ng lint`](https://angular.dev/cli/lint), [eslint-plugin-vuejs](https://eslint.vuejs.org/), [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) for `.jsx` & `.tsx` files...)
* it is very easy to add a `git` `pre-commit` hook that invokes the [W3C v.Nu checker](https://validator.github.io/validator/) using [the `pre-commit` CLI](https://pre-commit.com/): [example `.pre-commit-config.yaml`](https://framagit.org/atelier-coala/atelier-coala/-/blob/main/.pre-commit-config.yaml?ref_type=heads#L15)
* a collection of bad practices in HTML, copied from real websites: [htmhell.dev](https://htmhell.dev)
* a bookmarklet to help making semantic HTML: [Construct.css](https://t7.github.io/construct.css/)
* [Automated Accessibility Part 1: Linting @dev.to](https://dev.to/steady5063/automated-accessibility-part-1-linting-5378)


<script>
['article h2', 'article h3'].forEach(selector => {
  document.querySelectorAll(selector).forEach(title => {
    title.id = title.textContent.toLowerCase()
                    .replace(/[()?!:,'&@]/g, '')
                    .replace(/[à]/g, 'a')
                    .replace(/[ç]/g, 'c')
                    .replace(/[éêè]/g, 'e')
                    .replace(/[ï]/g, 'i')
                    .replace(/ /g, '-')
  })
})
</script>

<style>
article img { max-height: 20em; }
article table, article th, article td {
  border: 2px solid black;
  border-collapse: collapse;
  padding: .5rem 1rem;
}
article table { border-style: hidden; margin: 0 auto; }
</style>

<!-- Com'
* [x] https://news.ycombinator.com/item?id=43393994
* [x] https://news.humancoders.com/users/15727-lucas-c
* [x] https://www.reddit.com/r/programming/comments/1jdrgrh/a_review_of_html_linters/
      https://www.reddit.com/r/webdev/comments/1bkskf7/comment/micngv4/
* [ ] https://dev.to/lucasc/
* [ ] https://medium.com/@Lucas_C/
-->
