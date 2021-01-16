Title: Adding content to existing PDFs with fpdf2
Date: 2021-01-15 12:30
Tags: lang:en, python, source-code, pdf, fpdf2, pdfrw, prog
Slug: adding-content-to-existing-pdfs-with-fpdf2
---

`fpdf2`, the library I mentioned in my [previous post](fpdf2-release-2-2-0.html), cannot **parse** existing PDF files.

However, other Python libraries can be combined with `fpdf2`
in order to add new content to existing PDF files.

This page provides several examples of doing so using [`pdfrw`](https://github.com/pmaupin/pdfrw),
a great zero-dependency pure Python library dedicated to reading & writing PDFs,
with numerous examples and a very clean set of classes modelling the PDF internal syntax.


## Adding content onto an existing PDF page

```python
import sys
from fpdf import FPDF
from pdfrw import PageMerge, PdfReader, PdfWriter

IN_FILEPATH = sys.argv[1]
OUT_FILEPATH = sys.argv[2]
ON_PAGE_INDEX = 1
UNDERNEATH = False  # if True, new content will be placed underneath page (painted first)

def new_content():
    fpdf = FPDF()
    fpdf.add_page()
    fpdf.set_font("helvetica", size=36)
    fpdf.text(50, 50, "Hello!")
    reader = PdfReader(fdata=bytes(fpdf.output()))
    return reader.pages[0]

writer = PdfWriter(trailer=PdfReader(IN_FILEPATH))
PageMerge(writer.pagearray[ON_PAGE_INDEX]).add(new_content(), prepend=UNDERNEATH).render()
writer.write(OUT_FILEPATH)
```


## Adding a page to an existing PDF

```python
import sys
from fpdf import FPDF
from pdfrw import PdfReader, PdfWriter

IN_FILEPATH = sys.argv[1]
OUT_FILEPATH = sys.argv[2]
NEW_PAGE_INDEX = 1  # set to None to append at the end

def new_page():
    fpdf = FPDF()
    fpdf.add_page()
    fpdf.set_font("helvetica", size=36)
    fpdf.text(50, 50, "Hello!")
    reader = PdfReader(fdata=bytes(fpdf.output()))
    return reader.pages[0]

writer = PdfWriter(trailer=PdfReader(IN_FILEPATH))
writer.addpage(new_page(), at_index=NEW_PAGE_INDEX)
writer.write(OUT_FILEPATH)
```

This example relies on [_Pull Request_ #216](https://github.com/pmaupin/pdfrw/pull/216)
in order to be able to specify `at_index` (currently `pdfrw` only allows to **append** pages).
Until it is merged, you can install a forked version of `pdfrw` including the required patch:

    pip install git+https://github.com/PyPDF/pdfrw.git@addpage_at_index


## Demo

In order to demonstrate this using an actual example,
I first generated a PDF of the 1st code snippet above using the [`src2pdf` bash function described in an old article on syntax coloring](convert-code-to-pdf-with-syntax-coloring.html):

<a href="images/2021/01/add_on_page.pdf">
  <figure>
    <img alt="PDF Logo" src="images/2021/01/add_on_page-thumbnail.pdf.png">
    <figcaption><code>add_on_page.pdf</code> (PDF 1 page 30 Ko)</figcaption>
  </figure>
</a>

And then I added the following official Python logo to it:

![Python logo](images/2021/01/python-logo.png)

There is the `new_content` function I used:

```python
def new_content():
    fpdf = FPDF()
    fpdf.add_page()
    fpdf.image("python-logo.png", x=0, y=120)
    reader = PdfReader(fdata=bytes(fpdf.output()))
    return reader.pages[0]
```

And there is the result: [add_on_page_with_python_logo.pdf (41 Ko)](images/2021/01/add_on_page_with_python_logo.pdf).
