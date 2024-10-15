Title: fpdf2 latest news
Date: 2024-10-14 12:30
Tags: lang:en, libre-software, open-source, python, library, release, pdf, fpdf2, FastAPI, gunicorn, pygal, harfbuzz, mistletoe, livereload, bezier, hacktoberfest, pypi, retrospective, tutorial, markdown, html, prog
Image: images/2024/10/MyGodItsFullOfStars.jpg
---
I wrote [my last post on `fpdf2`](tag/fpdf2.html) 18 months ago.
We released **7 more versions** of `fpdf2` since then!

This article will present some of the major features introduced since **v2.7.3** to [**v2.8.1**](https://github.com/py-pdf/fpdf2/releases/tag/2.8.1) of `fpdf2`:
click on the buttons below to reveal the various changes brought to the library.

<dialog id="org-changes">

`fpdf2` joined the [**@py-pdf** GitHub organization](https://py-pdf.github.io/), that also hosts [pypdf](https://github.com/py-pdf/pypdf), [PyPDF-Builder](https://github.com/py-pdf/PyPDF-Builder), [pdfly](https://github.com/py-pdf/pdfly) and [pypdf_table_extraction](https://github.com/py-pdf/pypdf_table_extraction).
The reasons for this move were detailed in [discussion #752](https://github.com/py-pdf/fpdf2/discussions/752).

![py-pdf logo](https://py-pdf.github.io/images/pypdf-snake.png)

`fpdf2` also welcomes two new maintainers: **Anderson Herzogenrath da Costa** ([@andersonhc](https://github.com/andersonhc)) and **Georg Mischler** ([@gmischler](https://github.com/gmischler)).
More details about them in [discussion #896](https://github.com/py-pdf/fpdf2/discussions/896) & [discussion #898](https://github.com/py-pdf/fpdf2/discussions/898).

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="text-shaping">

A new [`FPDF.set_text_shaping()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.set_text_shaping) method has been introduced to perform text shaping using **Harfbuzz**, thanks to [@andersonhc](https://github.com/andersonhc): [documentation page on **text shaping**](https://py-pdf.github.io/fpdf2/TextShaping.html).

![Text shaping in fpdf2](https://py-pdf.github.io/fpdf2/text-shaping-ligatures.png)

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="bezier-curves">

Previously only supported when [rendering SVG images](https://py-pdf.github.io/fpdf2/SVG.html),
quadratic & cubic Bezier curves can now be directly rendered using the new **`FPDF.bezier()`** method, thanks to [@awmc000](https://github.com/awmc000): [documentation on Bezier curves](https://py-pdf.github.io/fpdf2/Shapes.html#bezier-curve).

![Quadratic & cubic Bezier curves with fpdf2](https://py-pdf.github.io/fpdf2/bezier-chaining.png)

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="free-text-annotations">

Support for **Free Text annotations** was added by [@MarekT0v](https://github.com/MarekT0v) in [PR #1039](https://github.com/py-pdf/fpdf2/pull/1039) : [documentation on Free Text annotations](https://py-pdf.github.io/fpdf2/Annotations.html#free-text-annotations).

![Free Text annotations with fpdf2](https://py-pdf.github.io/fpdf2/free-text-annotation.png)

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="other-additions">

+ new method [**`text_columns()`**](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.text_columns), contributed by [@gmischler](https://github.com/gmischler), allowing to render text within a single or multiple columns, including height balancing: [documentation page](https://py-pdf.github.io/fpdf2/TextColumns.html).
+ new **AES-256 encryption**, thanks to [@andersonhc](https://github.com/andersonhc) in [PR #872](https://github.com/py-pdf/fpdf2/pull/872): [documentation page](https://py-pdf.github.io/fpdf2/Encryption.html#encryption-method).
+ new method [**`FPDF.mirror()`**](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.mirror), contributed by [@sebastiantia](https://github.com/sebastiantia): _cf._ [documentation page on transformations](https://py-pdf.github.io/fpdf2/Transformations.html).
+ improvement regarding the **embedding of SVG images**: support for `<image>`, `<defs>` and `<clipPath>` tags anywhere in the document, and for `<path>` children of `<clipPath>`.
+ [`FPDF.multi_cell()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.multi_cell) has a new optional `center` parameter to position the cell horizontally at the center of the page.

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="combining-with-other-libs">

We added more guides detailing how to combine `fpdf2` with other libraries:

+ with [mistletoe](https://pypi.org/project/mistletoe/) in order to generate PDF documents from **Markdown**: [documentation page](https://py-pdf.github.io/fpdf2/CombineWithMistletoeoToUseMarkdown.html).
+ with `livereload` to enable a "watch" mode while performing PDF generation: [documentation page](https://py-pdf.github.io/fpdf2/CombineWithLivereload.html)
+ using `Pygal` to embed `graphs` and `charts`, thanks to [@ssavi-ict](https://github.com/ssavi-ict): [documentation section](https://py-pdf.github.io/fpdf2/Maths.html#using-pygal).
+ using `fpdf2` with [gunicorn](https://gunicorn.org/) ([documentation section](https://py-pdf.github.io/fpdf2/UsageInWebAPI.html#gunicorn)) or [FastAPI](https://fastapi.tiangolo.com/) ([documentation section](https://py-pdf.github.io/fpdf2/UsageInWebAPI.html#FastAPI)) - thanks to [@KamarulAdha](https://github.com/KamarulAdha).
+ using `fpdf2` with [Rough.js](https://roughjs.com/): [documentation page](https://py-pdf.github.io/fpdf2/CombineWithRoughJS.html).

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="tables">

Several improvements were made regarding [tables](https://py-pdf.github.io/fpdf2/Tables.html) :

* links, padding & vertical alignment in cells with `v_align`
* new parameters `gutter_height`, `gutter_width` and `wrapmode`
* control over outer border width
* allowing for multiple heading rows, and control over headings repetition over pages
* custom `cell_fill_mode` logic can now be provided
* cells that span multiple rows via the `rowspan` attribute, which can be combined with `colspan`

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="html">

Various improvements regarding our [basic HTML renderer](https://py-pdf.github.io/fpdf2/HTML.html):

* support for CSS page breaks properties
* support for `start` & `type` attributes of `<ol>` tags, and `type` attribute of `<ul>` tags
* `tag_styles` to control the font, color, size & indent of most HTML elements
* `li_prefix_color` to control the color of list prefixes (bullets & numbers)

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="performance-improvements">

* faster `FPDF.start_section()`, _cf._ [issue #1092](https://github.com/py-pdf/fpdf2/issues/1092)
* [`FPDF.multi_cell()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.multi_cell) generates fewer PDF component objects thanks to [@mjasperse](https://github.com/mjasperse), _cf._ [PR #1048](https://github.com/py-pdf/fpdf2/pull/1048)

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="uniformisation">

+ [`FPDF.write_html()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.write_html) now uses the new [`FPDF.table()`](https://py-pdf.github.io/fpdf2/Tables.html) method to render `<table>` tags.
+ font aliases are deprecated (`Arial` → `Helvetica`, `CourierNew` → `Courier`, `TimesNewRoman` → `Times`), they will be removed in a later release.
+ to improve naming consistency, the `txt` parameters of `FPDF.cell()`, `FPDF.multi_cell()`, `FPDF.text()` & `FPDF.write()` have been renamed to `text`.
+ the `split_only` optional parameter of [`FPDF.multi_cell()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.multi_cell) has been replaced by two new distincts optional parameters: `dry_run` & `output`.
+ `fpdf.TitleStyle` has been renamed into [`fpdf.TextStyle`](https://py-pdf.github.io/fpdf2/fpdf/fonts.html#fpdf.fonts.TextStyle).
+ we removed an obscure and undocumented [feature](https://github.com/py-pdf/fpdf2/issues/1198) of [`FPDF.write_html()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.write_html), which used to magically pass local variables as arguments.

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="pypi-trusted-publisher">

In order to do "our part" to contribute to a more secure Python ecosystem,
`fpdf2` releases are now performed using Pypi Trusted Publishers : [Pypi blog announcement](https://blog.pypi.org/posts/2023-04-20-introducing-trusted-publishers/).

  <form method="dialog"><button>Close</button></form>
</dialog>

<dialog id="new-tutorials">

New tutorials :

* [Polski](https://py-pdf.github.io/fpdf2/Tutorial-pl.html) thanks to [@DarekRepos](https://github.com/DarekRepos)
* Dutch: [Handleiding](https://py-pdf.github.io/fpdf2/Tutorial-nl.md) thanks to [@Polderrider](https://github.com/Polderrider)
* Khmer language: [ភាសខ្មែរ](https://py-pdf.github.io/fpdf2/Tutorial-km.html) thanks to [@kuth-chi](https://github.com/kuth-chi)
* [日本語](https://py-pdf.github.io/fpdf2/Tutorial-ja.html) thanks to [@alcnaka](https://github.com/alcnaka)
* [Indonesian](https://py-pdf.github.io/fpdf2/Tutorial-id.html) thanks to [@odhyp](https://github.com/odhyp)
* [Türkçe](https://py-pdf.github.io/fpdf2/Tutorial-tr.html), thanks to [@natgho](https://github.com/natgho)

  <form method="dialog"><button>Close</button></form>
</dialog>

<div class="grid">
  <button aria-label="Open modal with details" aria-controls="org-changes">Organizational changes</button>
  <button aria-label="Open modal with details" aria-controls="text-shaping">Text shaping with Harfbuzz</button>
  <button aria-label="Open modal with details" aria-controls="bezier-curves">Bezier curves</button>
  <button aria-label="Open modal with details" aria-controls="free-text-annotations">Free Text annotations</button>
  <button aria-label="Open modal with details" aria-controls="other-additions">Other additions</button>
  <button aria-label="Open modal with details" aria-controls="combining-with-other-libs">Combining with other libs</button>
  <button aria-label="Open modal with details" aria-controls="tables">Tables improvements</button>
  <button aria-label="Open modal with details" aria-controls="html">HTML</button>
  <button aria-label="Open modal with details" aria-controls="performance-improvements">Performance improvements</button>
  <button aria-label="Open modal with details" aria-controls="uniformisation">Uniformisation</button>
  <button aria-label="Open modal with details" aria-controls="pypi-trusted-publisher">Pypi Trusted Publisher</button>
  <button aria-label="Open modal with details" aria-controls="new-tutorials">New tutorials</button>
</div>

<br>

I would also like to celebrate that, as spotted by [@gmischler](https://github.com/gmischler) in [discussion #1232](https://github.com/py-pdf/fpdf2/discussions/1232), `fpdf2` has exceeded **1000 stars on GitHub**!
Yes, it's a bit superficial, but I'd like to thank all the programmers who have expressed their support for `fpdf2`: it makes me happy to know that this project is useful to you 🙂

<img alt="My God, it's full of stars!" src="images/2024/10/MyGodItsFullOfStars.jpg" style="width: 25rem">

<br>

Because such retrospective time is also an opportunity to reflect on things that did **not** go well,
I would like to mention a few failures:

* we've had a couple of _Pull Requests_ left unanswered for almost a year... 😞 I will try to be more vigilant about this, as I know not having feedback can really kill developers' motivation.

* I spotted a bug while using the excellent [`pdfly` CLI tool](https://github.com/py-pdf/pdfly) to extract pages from a PDF document built with `fpdf2`: the resulting file was excessively big. After adding a unit test to `pdfly` to investigate (in [PR #45](https://github.com/py-pdf/pdfly/pull/45)), I realized that this was due to a slightly invalid structure in the PDF documents produced by `fpdf2`. All the PDF readers I tested did not care, but the `pypdf` library (used by `pdfly`) was using this information to properly extract pages from a file. This is now all fixed!

* I initially performed a release for `fpdf2` version 2.8.0, but then erroneously removed it on [Pypi](https://pypi.org/), erroneously fearing a regression 😅 Versions 2.8.0 & 2.8.1 are exactly the same.

Finally, [Hacktoberfest](https://hacktoberfest.com/) is currently running, and we have many issues [up-for-grabs](https://github.com/py-pdf/fpdf2/issues?q=is%3Aissue+is%3Aopen+label%3Aup-for-grabs) at `fpdf2`, so come help and contribute some code! 🙂

<style>
dialog {
  margin: 8rem 1rem;
  padding: 1rem 2rem;
  border: 2px solid black;
  border-radius: 1rem;
}
@media (min-width:960px) {
  dialog {
    width: 60rem;
    margin-left: -30rem;
    margin-right: 0;
    left: 45%;
  }
}
dialog li { margin: .5rem 0; }
dialog img { max-height: 20rem; }
@media (min-width:768px) {
  dialog img { max-width: 25rem; }
}
.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}
@media (min-width:768px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
.grid button {
  background: #33cc66;
  padding: 1.5rem;
  border: 2px solid black;
  border-radius: 2rem;
}
</style>

<script>
document.querySelectorAll(".grid button").forEach(btn => {
  btn.onclick = () => document.getElementById(btn.getAttribute("aria-controls")).showModal();
});
</script>

<!--
Com':
* [x] https://dev.to/lucasc/fpdf2-latest-news-7pc
* [x] https://news.ycombinator.com/item?id=41838642
* [x] https://www.reddit.com/r/hacktoberfest/comments/1g3j2v1/
* [x] https://news.humancoders.com/ (submitted: published?)
* [ ] https://www.reddit.com/r/pythonnews/ (now requires access)
-->
