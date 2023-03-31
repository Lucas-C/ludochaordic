Title: fpdf2 latest new features
Date: 2023-04-02 12:00
Tags: lang:en, libre-software, open-source, python, library, release, pdf, fpdf2, prog
Status: draft
---
I wrote my latest post on the subject almost a year ago.
As we just released a new version of `fpdf2`, [v2.7](https://github.com/PyFPDF/fpdf2/blob/master/CHANGELOG.md),
this is the perfect time to mention some recent additions to this library! 😊

This article will present some of the major features introduced between v2.5.3 & v2.7.1 of `fpdf2`.

## Tables
One major addition of **v2.7.0** of `fpdf2` has the new method `.table()`,
that now makes very easy the generation of tables in PDF documents.

We documented how to use it in this documentation page: https://pyfpdf.github.io/fpdf2/Tables.html



## Images
- `FPDF.image()`: `keep_aspect_ratio` & `align="C"`
- `round_corners`
- image ICC Profiles
- documentation on how to control objects transparency: [link to docs](https://pyfpdf.github.io/fpdf2/Transparency.html)

## Fonts & text
- `fpdf2` now uses [fontTools](https://fonttools.readthedocs.io/en/latest/) to read and embed fonts in the PDF
- subscript, superscript, nominator and denominator
- new method [`FPDF.set_fallback_fonts()`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.set_fallback_fonts)

## Signing & encrypting documents

## Annotations
- [`FPDF.ink_annotation()`](https://pyfpdf.github.io/fpdf2/Annotations.html#ink-annotations): new method added to add path annotations
- [`embed_file()`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.embed_file) & [`file_attachment_annotation()`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.file_attachment_annotation)

## Documentation & translated tutorials
- demonstration Jupyter notebook: [tutorial/notebook.ipynb](https://github.com/PyFPDF/fpdf2/blob/master/tutorial/notebook.ipynb)

## What's coming next?
**Governance**:
During the year 2022, I became the unique maintainer of `fpdf2`.
Move to py-pdf to join forces -> link to fpdf2 issue

TODO: mention authors of feature PRs

<!-- Com' :
* [ ] https://news.ycombinator.com
* [ ] https://www.reddit.com/r/programming/
* [ ] https://www.reddit.com/r/Python/
* [ ] https://dev.to/lucasc/
-->
