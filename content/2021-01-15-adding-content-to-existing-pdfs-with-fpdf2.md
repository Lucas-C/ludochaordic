Title: Adding content to existing PDFs with fpdf2
Date: 2021-01-15 12:30
Lang: en
Tags: lang:en, python, source-code, pdf, fpdf2, pdfrw, prog
Slug: adding-content-to-existing-pdfs-with-fpdf2
---

`fpdf2`, the library I mentioned in my [previous post](fpdf2-release-2-2-0.html), cannot **parse** existing PDF files.

However, other Python libraries can be combined with `fpdf2`
in order to add new content to existing PDF files.

**[EDIT 2024/12/17]** : those examples are now included in the official `fpdf2` documentation:

* [Combine with pdfrw](https://py-pdf.github.io/fpdf2/CombineWithPdfrw.html)
* [Combine with pypdf](https://py-pdf.github.io/fpdf2/CombineWithPypdf.html)

## Demo

In order to demonstrate this using an actual example,
I first generated a PDF of some code snippet using the [`src2pdf` bash function described in an old article on syntax coloring](convert-code-to-pdf-with-syntax-coloring.html):

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
