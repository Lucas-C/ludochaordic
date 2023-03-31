Title: fpdf2.4.0 and converting GIFs to PDFs
Date: 2021-06-12 10:40
Tags: lang:en, libre-software, open-source, python, library, release, source-code, pdf, fpdf2, gif, markdown, jpeg, accessibility, prog
Slug: fpdf2-4-0-and-converting-gifs-to-pdfs
Image: images/2021/06/exploding-cat.gif
---

`fpdf2` is a minimalist PDF creation library for Python that I am maintaining.

With the release yesterday of its `v2.4.0`, I'm going to present some of its notable new features since [the latest minor version](fpdf2-3-0-unbreakable-and-pdf-quines.html).

<https://github.com/pyfpdf/fpdf2/> [![Pypi latest version](https://img.shields.io/pypi/v/fpdf2.svg)](https://pypi.python.org/pypi/fpdf2)
Doc: <https://pyfpdf.github.io/fpdf2/>

## JPEG images take less space

<img class="left" alt="Glitched JPEG tombstone" src="images/2021/06/jpeg-tombstone.jpg">

`fpdf2` now uses the newly supported `DCTDecode` image filter for JPEG images, in order to improve the compression ratio without any image quality loss.

On test images, this **reduced** the size of embedded JPEG images by **90%**.

## Basic Markdown styling

<img class="right" alt="Markdown" src="images/2021/06/markdown.jpg">

`fpdf2` now allows to use basic Markdown-like styling: `**bold**, __italics__, --underlined--`.

Currently, this is only supported by the [`FPDF.cell` method](https://pyfpdf.github.io/fpdf2/fpdf/#fpdf.FPDF.cell),
using `markdown=True`, but I plan to also implement this for the `FPDF.multi_cell` & `FPDF.write` methods.

## Document outline & table of contents

<img class="left" alt="Screenshot from Sumatra PDF" src="images/2021/06/document-outline.png">

Quoting the [PDF format reference](https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/PDF32000_2008.pdf):
> A PDF document may optionally display a **document outline** on the screen, allowing the user to navigate interactively
> from one part of the document to another. The outline consists of a tree-structured hierarchy of outline items,
> which serve as a visual table of contents to display the document’s structure to the user.

Since `v2.3.3` you can define such outlines, as well as tables of contents !

Full documentation: [fpdf2 / Document outline & table of contents](https://pyfpdf.github.io/fpdf2/DocumentOutlineAndTableOfContents.md.html)

## Annotations

<img class="right" alt="Text annotation example" src="images/2021/06/text-annotation.png">

`fpdf2` now allows to add various PDF annotations, such as **text annotations**
or **links to directly open other PDF files** on the same file-system.

Full documentation: [fpdf2 / Annotations](https://pyfpdf.github.io/fpdf2/Annotations.html)

## Accessibility

<img class="left big" alt="fpdf2 logo with cursor showing an alternate description" src="images/2021/06/fpdf2-logo-with-text-alt.png">

Since `v2.3.1` alternative text descriptions can now be added by the `FPDF.image()` & `FPDF.link()` methods.

They allow [screen readers](https://en.wikipedia.org/wiki/Screen_reader) to extract readable descriptions
from images & links in the generated PDFs.

## Presentations

<img class="right" alt="Exploding cat GIF" src="images/2021/06/exploding-cat.gif">

In PDF readers, **presentation mode** can usually be enabled with the `CTRL + L` shortcut.

This release introduces support for **page transitions** in presentation mode:
[`FPDF.add_page()`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.add_page)
now accepts two new optional parameters, `duration` & `transition`,
to define how the viewer application should advances to the next page.

Full documentation: [fpdf2 / Presentations](https://pyfpdf.github.io/fpdf2/Presentations.html)

After introducing this feature, I realized that PDF page durations allowed to build **presentations that behave like GIFs**:
sequences of images, one per page, that move forward automatically.

Hence I wrote a little script, [`gif2pdf.py`](https://github.com/PyFPDF/fpdf2/blob/master/tutorial/gif2pdf.py),
to test this silly idea.
There are the result:

* [exploding-cat.pdf](images/2021/06/exploding-cat.pdf)
* [speechless-nathan-fillion.pdf](images/2021/06/speechless-nathan-fillion.pdf)
* [Smiling-Leo.pdf](images/2021/06/Smiling-Leo.pdf)

You can open those files in Adobe Acrobat Reader (page durations are ignored by some other PDF readers),
then press `CTRL+L` to launch presentation mode,
and then ENTER to admire the animation!

Of course PDF readers are not optimized for this kind of animated files,
so the animation may be pretty slow, despite being configured to execute at 25 frames per second.

---

That's it for the notable recent features of `fpdf2`!
You can also check the detailed [CHANGELOG](https://github.com/PyFPDF/fpdf2/blob/master/CHANGELOG.md)
for an exhaustive list of all changes: bug fixes, other minor improvements and deprecation notices.

As someone recently asked about it: if ever you want to support my work on this open-source Python library,
you can [buy one of the games I published on itch.io](https://lucas-c.itch.io).

Now I wish you to have a lot of fun building PDFs with `fpdf2`!

I recently used it myself to create an animated poem for my girlfriend 😉
I'd love to know what creations you have made using it,
so please add comment below if you want to share them!


<!-- Com' :
* [x] https://planetpython.org
* [x] https://www.reddit.com/r/Python/comments/nywfb7/new_release_of_fpdf2_markdown_styling_jpeg/
* [x] https://www.reddit.com/r/pythonnews/comments/nywnx9/new_release_of_fpdf2_markdown_styling_jpeg/
* [x] https://dev.to/lucasc/new-release-for-fpdf2-40pi
* [x] video comment: https://www.youtube.com/watch?v=euNvxWaRQMY
* [x] video comment: https://www.youtube.com/watch?v=JhQVD7Y1bsA
-->

<style>
article img { max-height: 12rem; }
article img.big { max-height: 20rem; }
article h2 { padding-top: 2rem; }
@media screen and (min-width: 40rem) {
  article img { margin: 0 1rem; }
  img.left  { float: left; }
  img.right { float: right; }
  article h2 { clear: both; }
}
.uk-article-content > p:nth-child(3) { /* Link to GitHub repo */
  display: block;
  text-align: center;
  border: 1px solid black;
  border-radius: 10rem;
  padding: 1rem;
  margin: 2rem 10vw;
}
.uk-article-content > p:nth-child(3) img { margin: auto; }
</style>
