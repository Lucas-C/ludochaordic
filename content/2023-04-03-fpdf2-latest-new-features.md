Title: fpdf2 latest new features
Date: 2023-04-03 17:00
Tags: lang:en, libre-software, open-source, python, library, release, pdf, fpdf2, prog
---
I wrote my latest [post on `fpdf2`](tag/fpdf2.html) almost a year ago.
As we just released a new version, [v2.7.3](https://github.com/PyFPDF/fpdf2/blob/master/CHANGELOG.md),
this is the time to mention some recent additions to this library! 😊

This article will present some of the major features introduced between **v2.5.3** & **v2.7.3** of `fpdf2`:

- [Tables](#tables)
- [Images & shapes](#images--shapes)
- [Fonts & text](#fonts--text)
- [Signing & encrypting documents](#signing--encrypting-documents)
- [Annotations](#annotations)
- [Documentation & translated tutorials](#documentation--translated-tutorials)
- [What's coming next?](#whats-coming-next)

## Tables
One major addition of **v2.7.0** of `fpdf2` has the new method `.table()`,
that now makes very easy the generation of **tables** in PDF documents.

We documented how to use this method in a dedicated documentation page: <https://pyfpdf.github.io/fpdf2/Tables.html>

Here is some snippet of demo code:
```python
from fpdf import FPDF

TABLE_DATA = (
    ("First name", "Last name", "Age", "City"),
    ...
)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=16)
with pdf.table(borders_layout="MINIMAL",
               col_widths=(30, 30, 10, 30),
               cell_fill_color=200,  # grey scale
               cell_fill_mode="ROWS",
               text_align="CENTER") as table:
    for data_row in TABLE_DATA:
        row = table.row()
        for datum in data_row:
            row.cell(datum)
pdf.output("table-demo.pdf")
```
And the result:
![Sample table rendered in a PDF document](images/2023/04/table-demo.jpg)


## Images & shapes
There has been several new features related to images:

- [`FPDF.image()`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.image)
  has two new optional parameters: `align="C"` to horizontally an image on a page,
  and `keep_aspect_ratio` which allows to preserve an image ratio.
  Related documentation section: [fitting an image inside a rectangle](https://pyfpdf.github.io/fpdf2/Images.html#fitting-an-image-inside-a-rectangle).

- thanks to a contribution by [@eroux](https://github.com/eroux) in [PR #709](https://github.com/PyFPDF/fpdf2/pull/709), [ICC Profiles](https://en.wikipedia.org/wiki/ICC_profile) of images inserted by `FPDF.image()` are now extracted an inserted in the PDF document: [doc](https://pyfpdf.github.io/fpdf2/Images.html#icc-profiles).

- rectangles drawn with [`FPDF.rect()`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.rect) can now have **rounded corners** using the new `round_corners` parameter. Check the documentation for examples: [Shapes: _rectangles with round corners_](https://pyfpdf.github.io/fpdf2/Shapes.html#rectangle).

- we documentated on how to control transparency of overlapping text, shapes and images through `stroke_opacity` & `fill_opacity`: [documentation](https://pyfpdf.github.io/fpdf2/Transparency.html).

![Example overlapping objects with transparency](https://pyfpdf.github.io/fpdf2/transparency.png)


## Fonts & text
- since **v2.5.7**, `fpdf2` now uses the popular [fontTools](https://fonttools.readthedocs.io/en/latest/) library to read and embed fonts in the PDF. This extended the range of font definition files supported by `fpdf2`, and also made the code used to parse & insert fonts a lot more robust. Thanks a lot to [@RedShy](https://github.com/RedShy) for this change made in [PR #477](https://github.com/PyFPDF/fpdf2/pull/477).

- [@andersonhc](https://github.com/andersonhc) introduced a **font fallback** mechanism controlled by a new method [`FPDF.set_fallback_fonts()`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.set_fallback_fonts) in [PR #669](https://github.com/PyFPDF/fpdf2/pull/669): [related documentation](https://pyfpdf.github.io/fpdf2/Unicode.html#fallback-fonts).

- [@gmischler](https://github.com/gmischler) provided support for subscript, superscript, nominator and denominator in [PR #520](https://github.com/PyFPDF/fpdf2/pull/520): [related documentation](https://pyfpdf.github.io/fpdf2/TextStyling.html#subscript-superscript-and-fractional-numbers).

![Usage example of subscript, superscript, nominator and denominator](https://pyfpdf.github.io/fpdf2/char_vpos.png)


## Signing & encrypting documents

- since **v2.5.6**, `fpdf2` allows to **sign** documents, using the companion [endesive](https://pypi.org/project/endesive/) package: [related documentation](https://pyfpdf.github.io/fpdf2/Signing.html).

- since **v2.6.1**, and thanks to [@andersonhc](https://github.com/andersonhc) work in [PR #609](https://github.com/PyFPDF/fpdf2/pull/609), `fpdf2` allows to **encrypt** documents using RC4 or AES-128 algorithms: [related documentation](https://pyfpdf.github.io/fpdf2/Encryption.html).


## Annotations
- since **v2.5.7**, [`embed_file()`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.embed_file) & [`file_attachment_annotation()`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.file_attachment_annotation) allow to **embed** other files into PDF documents: [related documentation](https://pyfpdf.github.io/fpdf2/FileAttachments.html).

- `FPDF.ink_annotation()` has been introduced in **v2.5.5** new to add path annotations: [related documentation](https://pyfpdf.github.io/fpdf2/Annotations.html#ink-annotations).

![Ink annotation example](https://pyfpdf.github.io/fpdf2/ink_annotation.png)


## Documentation & translated tutorials
A demonstration [**Jupyter notebook**](https://jupyter.org/) has been created: [tutorial/notebook.ipynb](https://github.com/PyFPDF/fpdf2/blob/master/tutorial/notebook.ipynb)

New translations of our [tutorial](https://pyfpdf.github.io/fpdf2/Tutorial.html) were also provided:

* Simplified Chinese in [PR #666](https://github.com/PyFPDF/fpdf2/pull/666) by [@Bubbu0129](https://github.com/Bubbu0129): [简体中文](https://pyfpdf.github.io/fpdf2/Tutorial-zh.html)

* Bengali in [PR #738](https://github.com/PyFPDF/fpdf2/pull/738) by [@ssavi-ict](https://github.com/ssavi-ict): [বাংলা](https://pyfpdf.github.io/fpdf2/Tutorial-bn.html)


## What's coming next?
We have several [enhancement proposals](https://github.com/PyFPDF/fpdf2/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement+) open (and mostly "up-for-grabs"),
and also an handful of [**good first issues**](https://github.com/PyFPDF/fpdf2/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22) dedicated to developpers would like to start contributing to `fpdf2` with a relatively easy task.

Among major projects, two contributors made very interesting & ambitious suggestions:

* [@gmischler](https://github.com/gmischler) has plans to enhance `fpdf2` text-rendering capacities: [discussion #339](https://github.com/PyFPDF/fpdf2/discussions/339). At the moment he is working on a general solution for organizing flowing text with [`TextRegion`](https://github.com/gmischler/fpdf2/tree/TextRegion) classes.

* [@andersonhc](https://github.com/andersonhc) suggested in [discussion #696](https://github.com/PyFPDF/fpdf2/discussions/696) to integrate the [harfbuzz](https://harfbuzz.github.io/) library to provide `fpdf2` with text shaping abilities

Finally, I am seriously considering to **move the `fpdf2` project to the [@py-pdf GitHub organization](https://github.com/py-pdf)**, in order to share ownership of several PDF-related Python libraries with other maintainers and join forces!
You can track this migration project and share your feedback in this GitHub discussion:
<https://github.com/PyFPDF/fpdf2/discussions/752>.

As always, I would be happy to receive your comments below 😊

<!-- Com' :
* [x] https://news.ycombinator.com/item?id=35424491
* [x] https://www.reddit.com/r/Python/comments/12amq5d/fpdf2_latest_new_features/
* [x] https://dev.to/lucasc/fpdf2-latest-new-features-4mn0
-->
