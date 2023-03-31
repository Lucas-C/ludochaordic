Title: fpdf2.3.0 Unbreakable! and PDF quines
Date: 2021-01-29 12:30
Tags: lang:en, libre-software, open-source, python, library, release, source-code, pdf, fpdf2, quine, NightShyamalan, prog
Slug: fpdf2-3-0-unbreakable-and-pdf-quines
---
![Unbreakable movie poster](images/2021/01/unbreakable.jpg)

Today, I am happy to announce **version 2.3.0 of fpdf2**, code name: **Unbreakable!**

<https://github.com/pyfpdf/fpdf2/> [![Pypi latest version](https://img.shields.io/pypi/v/fpdf2.svg)](https://pypi.python.org/pypi/fpdf2)
Doc: <https://pyfpdf.github.io/fpdf2/>

Why _Unbreakable_?

- As a tribute to [M. Night Shyamalan movie](https://en.wikipedia.org/wiki/Unbreakable_(film))
- Because using `fpdf2`, your Python code can never break!
<br>...<br>
Just kidding, I would be a fool to think the library contains **zero** bug 😅
- Because this release introduces a new `unbreakable()` method,
ensuring that inside this context manager, no page break will happen:

```python
with pdf.unbreakable() as pdf:
    for row in data:
        for datum in row:
            pdf.cell(col_width, line_height, datum", border=1)
        pdf.ln(line_height)
pdf.ln(line_height * 2)
```

Check the documentation page on [Page breaks](https://pyfpdf.github.io/fpdf2/PageBreaks.html)
for more details.

This release also brings a few other things:

- bug fixes for the `FPDF.alias_nb_pages` & `FPDF.set_font` methods
- new `FPDF.epw` & `FPDF.eph` `@property` methods, providing the effective page width & height
- several new documentation pages: feeding HTML, creating links, tables, text styling...

Check the [CHANGELOG.md](https://github.com/PyFPDF/fpdf2/blob/master/CHANGELOG.md) for more details!


## PDF quines

Since I have started working on `fpdf2`,
I have this idea in the back of my mind:
**could be possible to write a PDF quine?**

The term "quine" may not be well known, so I'll quote [the Wikipedia page on the subject](https://en.wikipedia.org/wiki/Quine_(computing)):

> A quine is a computer program which produces a copy of its own source code as its only output.

Example with Python 3.8+:

```python
exec(s:='print("exec(s:=%r)"%s)')
```

Or with [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)):
```shell
a(){ echo $2 \\$1 $1 $2 $1 ;};a \' ' a(){ echo $2 \\$1 $1 $2 $1 ;};a '
```

There is also the amazing [quinesnake](https://github.com/taylorconor/quinesnake), a quine in C language, that is also a video game !

[![Unbreakable movie poster](images/2021/01/quinesnake.gif)](https://github.com/taylorconor/quinesnake)

No, could it be possible to build **a PDF that displays its own source code?**

I have to admit that I haven't been able to craft one myself so far...

As a starting point, there is a really minimal PDF source code:
```
%PDF-1.3
%âãÏÓ
1 0 obj<</Pages 2 0 R>>endobj
2 0 obj<</Count 1 /Kids [3 0 R] /Type /Pages>>endobj
3 0 obj<</Contents 4 0 R /MediaBox [0 0 300 200] /Resources <</Font <</F <</BaseFont /Courier /Encoding /WinAnsiEncoding>>>>>> /Type /Page>>endobj
4 0 obj<</Length 50>>stream
BT /F 8 Tf 0 10 TD <25e2e3cfd3> Tj (%PDF-1.3) ' ETendstream endobj
xref
0 5
0000000000 65535 f
0000000014 00000 n
0000000045 00000 n
0000000097 00000 n
0000000244 00000 n
trailer<</Root 1 0 R /Size 5>>
startxref
340
%%EOF
```

If you paste this in a text file, and rename it with a `.pdf` extension,
you should be able to open it with a PDF viewer,
and the two first lines of this code snippet should be displayed.

So, as I was a bit stuck to go further, I built this **PDF that displays its own source code as Python**:

[![PDF](https://chezsoi.org/lucas/blog/images/2020/10/pdf-icon.png)](images/2021/01/quine.pdf)

What do you think, is it cheating? 😜

<!--
Com':
* [x] https://planetpython.org
* [x] https://www.reddit.com/r/Python/comments/kvbb4j/fpdf2_the_library_to_easily_generate_pdfs_got_a/
* [x] https://www.reddit.com/r/programming/comments/l7qok4/release_of_fpdf230_a_challenge_can_you_craft_a/
-->

<style>
.uk-article-content > p:nth-child(3) { /* Link to GitHub repo */
  display: block;
  text-align: center;
  border: 1px solid black;
  border-radius: 10rem;
  padding: 1rem;
  margin: 2rem 10vw;
}
</style>
