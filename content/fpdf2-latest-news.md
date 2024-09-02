Title: fpdf2 latest news
Date: 2024-??-?? ??:??
Tags: lang:en, libre-software, open-source, python, library, release, pdf, fpdf2, FastAPI, pygal, harfbuzz, mistletoe, livereload, bezier, markdown, html, prog
Status: draft
---
I wrote [my last post on `fpdf2`](tag/fpdf2.html) more than a year ago.
We released **7 more versions** since then.

This article will present some of the major features introduced since **v2.7.3** to **v2.7.10** of `fpdf2`:

* organizational changes: `fpdf2` joined the [@py-pdf GitHub org](https://github.com/py-pdf) + arrival of two new maintainers: Georg Mischler ([@gmischler](https://github.com/gmischler)) and Anderson Herzogenrath da Costa ([@andersonhc](https://github.com/andersonhc)).

* [`FPDF.set_text_shaping()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.set_text_shaping): new method to perform text shaping using **Harfbuzz** - [documentation](https://py-pdf.github.io/fpdf2/TextShaping.html) - thanks to @andersonhc

* quadratic & cubic Bezier curves with [`FPDF.bezier()`](https://py-pdf.github.io/fpdf2/fpdf/Shapes.html#fpdf.fpdf.FPDF.bezier) - thanks to @awmc000

* Free Text annotations: [documentation](https://py-pdf.github.io/fpdf2/Annotations.html#free-text-annotations) thanks to @MarekT0v - cf. [#1039](https://github.com/py-pdf/fpdf2/pull/1039)

* [`FPDF.mirror()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.mirror) - New method: [documentation page](https://py-pdf.github.io/fpdf2/Transformations.html) - Contributed by @sebastiantia

* `text_columns()` allows to render text within a single or multiple columns, including height balancing: [documentation](https://py-pdf.github.io/fpdf2/TextColumns.html) - thanks to @gmischler

* improvement regarding the HTML rendered: CSS page breaks properties; support for `start` & `type` attributes of `<ol>` tags, and `type` attribute of `<ul>` tags; `tag_styles` to control the font, color & size of most HTML elements; `tag_indents` to control the indent of many elements; `li_prefix_color`

* improvement regarding tables: links, padding & vertical alignment in cells with `v_align`; `gutter_height`, `gutter_width` and `wrapmode`; outer border width; multiple heading rows; `repeat_headings`; custom `cell_fill_mode` logic; cells that span multiple rows via the `rowspan` attribute, which can be combined with `colspan`;

* improvement regarding support for vector images (SVG) : support for `<image>` elements; support for `<defs>` and `<clipPath>` tags anywhere in the document, and for `<path>` children of `<clipPath>`;

* other improvements regarding existing methods:
    + New AES-256 encryption: [documentation](https://py-pdf.github.io/fpdf2/Encryption.html#encryption-method) - thanks to @andersonhc in [PR #872](https://github.com/py-pdf/fpdf2/pull/872)
    + [`FPDF.multi_cell()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.multi_cell): has a new optional `center` parameter to position the cell horizontally at the center of the page
    + `split_only` optional parameter of [`FPDF.multi_cell()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.multi_cell), which is replaced by two new distincts optional parameters: `dry_run` & `output`
    + optional `wrapmode` in templates: default `"WORD"` can optionally be set to `"CHAR"` to support wrapping on characters for scripts like Chinese or Japanese

* performance improvements: faster `FPDF.start_section()`, _cf._ [issue #1092](https://github.com/py-pdf/fpdf2/issues/1092); [`FPDF.multi_cell()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.multi_cell) generates fewer PDF component objects thanks to @mjasperse

* new tutorials : [Polski](https://py-pdf.github.io/fpdf2/Tutorial-pl.html) thanks to @DarekRepos; in Dutch: [Handleiding](https://py-pdf.github.io/fpdf2/Tutorial-nl.md) thanks to @Polderrider; Khmer language: [ភាសខ្មែរ](https://py-pdf.github.io/fpdf2/Tutorial-km.html) thanks to @kuth-chi; [日本語](https://py-pdf.github.io/fpdf2/Tutorial-ja.html) thanks to @alcnaka

* more guides on combining `fpdf2` with other libraries:
    + with [mistletoe](https://pypi.org/project/kaleido/) in order to [generate PDF documents from Markdown (link)](https://py-pdf.github.io/fpdf2/CombineWithMistletoeoToUseMarkdown.html)
    + with `livereload` to enable a "watch" mode with PDF generation: [Combine with livereload](https://py-pdf.github.io/fpdf2/CombineWithLivereload.html)
    + documentation on how to embed `graphs` and `charts` generated using `Pygal` lib: [documentation section](https://py-pdf.github.io/fpdf2/Maths.html#using-pygal) - thanks to @ssavi-ict
    + documentation on how to use `fpdf2` with [FastAPI](https://fastapi.tiangolo.com/): <https://py-pdf.github.io/fpdf2/UsageInWebAPI.html#FastAPI> - thanks to @KamarulAdha

* uniformization:
    + [`FPDF.write_html()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.write_html) now uses the new [`FPDF.table()`](https://py-pdf.github.io/fpdf2/Tables.html) method to render `<table>` tags.
    + font aliases are deprecated (`Arial` → `Helvetica`, `CourierNew` → `Courier`, `TimesNewRoman` → `Times`). They will be removed in a later release.
    + to improve naming consistency, the `txt` parameters of `FPDF.cell()`, `FPDF.multi_cell()`, `FPDF.text()` & `FPDF.write()` have been renamed to `text`.
    + an obscure and undocumented [feature](https://github.com/py-pdf/fpdf2/issues/1198) of [`FPDF.write_html()`](https://py-pdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.write_html), which used to magically pass local variables as arguments.

Mention PyConFr

+ https://github.com/py-pdf/fpdf2/discussions/1232 -> 1000 stars!

Employer une grid: https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Grids
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

+ des <dialog> : https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog

<dialog id="demo">
  <p>Greetings, one and all!</p>
  <form method="dialog">
    <button>OK</button>
  </form>
</dialog>

<script>
$("demo").show()
</script>
