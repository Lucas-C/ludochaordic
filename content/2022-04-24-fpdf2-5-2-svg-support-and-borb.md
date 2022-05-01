Title: fpdf2.5.2 : SVG support and borb
Date: 2022-04-24 13:00
Tags: lang:en, libre-software, open-source, python, library, release, source-code, pdf, benchmark, documentation, xml, security, django, flask, streamlit, aws, lambda, matplotlib, fpdf2, borb, prog
Slug: fpdf2-5-2-svg-support-and-borb
Image: images/2022/04/Ghostscript_Tiger.png
---

<!-- Com' réalisée :
* [x] https://news.ycombinator.com/item?id=31143783
* [x] https://www.reddit.com/r/programming/comments/ubg1mu/borb_vs_fpdf2_comparing_2_pdf_generation_libs/
* [x] https://www.reddit.com/r/Python/comments/uasf5r/borb_vs_fpdf2_comparing_2_pdf_generation_libs/
* [x] https://dev.to/lucasc/fpdf252-svg-support-and-comparison-with-borb-2fip
* [x] email @jorisschellekens & @gmischler + comment on @torque PR
-->

`fpdf2` is a simple & fast PDF creation library for Python that I have been maintaining since mid-2020.

In this article, I'm going to present some of the new features that landed since [my last post on the subject](hacktoberfest-on-fpdf2.html).
Hence, this will cover versions **2.5.0**, **2.5.1** & **2.5.2** of `fpdf2`.I will also perform a quick comparison with the [borb](https://borbpdf.com/) library.

<https://github.com/pyfpdf/fpdf2/> [![Pypi latest version](https://img.shields.io/pypi/v/fpdf2.svg)](https://pypi.python.org/pypi/fpdf2)
Doc: <https://pyfpdf.github.io/fpdf2/>

## Support for SVG (Scalable Vector Graphics)

Thanks to [@torque](https://github.com/torque) who worked on this over several months
and produced very high quality code, **`fpdf2` now supports embedding SVG files**!

He actually started by implementing a very large part of the **PDF drawing API**,
allowing to compose arbitrary sequences of paths, lines and curves:
[fpdf2 Drawing API documentation](https://pyfpdf.github.io/fpdf2/Drawing.html).

As a direct consequence, it became possible to build a direct SVG-to-PDF converter, which he did!

SVG files can now be directly added to a PDF file using the [image()](fpdf/fpdf.html#fpdf.fpdf.FPDF.image) method:
[fpdf2 SVG documentation](https://pyfpdf.github.io/fpdf2/SVG.html).

For security reasons, with the addition of this feature we added a new dependency to `fpdf2`:
[defusedxml](https://pypi.org/project/defusedxml/), used to check that embedding a SVG file does not trigger a denial of service,
for example a [_Billion laughs_ attack](https://github.com/PyFPDF/fpdf2/blob/master/test/image/test_vector_image.py#L77).

While the SVG converter has [some limitations](https://pyfpdf.github.io/fpdf2/SVG.html#currently-unsupported-notable-svg-features),
it is able, for example, to perfectly render the famous SVG example [Ghostscript_Tiger.svg](https://commons.wikimedia.org/wiki/File:Ghostscript_Tiger.svg)
to PDF: [Ghostscript_Tiger.pdf](images/2022/04/Ghostscript_Tiger.pdf).

[![Ghostscript Tiger PDF preview](images/2022/04/Ghostscript_Tiger.png)](images/2022/04/Ghostscript_Tiger.pdf)

## Other features

Two other useful features were added by [Georg Mischler](https://github.com/gmischler):

* support for soft-hyphen (`\u00ad`) break in `write()`, `cell()` & `multi_cell()`,
  _cf._ [documentation on line breaks](https://pyfpdf.github.io/fpdf2/LineBreaks.html)
* new parameters `new_x` and `new_y` were introduced for `cell()` and `multi_cell()` methods,
  in order to make cursor position after cell-rendering a lot more intuitive & user-friendly,
  _cf._ [related documentation](https://pyfpdf.github.io/fpdf2/Text.html#change-in-current-position)

[Georg Mischler](https://github.com/gmischler) also took some time to revise the whole structure of the documentation,
making it a lot more user-friendly. Thanks! 🙏

I also contributed a few extra functionalities:

* a new `add_highlight()` method to insert <mark>highlight annotations</mark>: [documentation](https://pyfpdf.github.io/fpdf2/Annotations.html#highlights)
* support for new PDF properties: `.text_mode` ([documentation](https://pyfpdf.github.io/fpdf2/TextStyling.html#text_mode)) & `.blend_mode` ([documentation](https://pyfpdf.github.io/fpdf2/Images.html#blending-images))
* new `round_clip()` & `elliptic_clip()` image clipping methods: [documentation](https://pyfpdf.github.io/fpdf2/Images.html#image-clipping)
  _(not released yet, planned for `v2.5.3`)_

## Usage examples with other libs

A few additions were made to the documentation to provide usage examples of `fpdf2` with other libraries:

* with [Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com), [streamlit](https://streamlit.io/), AWS lambdas: _cf._ [documentation](https://pyfpdf.github.io/fpdf2/UsageInWebAPI.html)
* with [Matplotlib](https://matplotlib.org/) to embed **charts & equations**: _cf._ [documentation](https://pyfpdf.github.io/fpdf2/Maths.html)
* with [SQLAlchemy](https://www.sqlalchemy.org/) to **store PDFs in a database**: _cf._ [documentation](https://pyfpdf.github.io/fpdf2/DatabaseStorage.html)
* with [pdfrw](https://github.com/pmaupin/pdfrw) to modify **existing PDFs**: _cf._ [documentation](https://pyfpdf.github.io/fpdf2/ExistingPDFs.html)

Would you like other examples being provided?
If so, drop a comment at the bottom of the page, or open a [discussion](https://github.com/PyFPDF/fpdf2/discussions/) / [issue](https://github.com/PyFPDF/fpdf2/issues),
explaining with which library you would like to combine `fpdf2` with 😊

## Deprecation notice

First, `DeprecationWarning` messages are not displayed by Python by default.

Hence, every time you use a newer version of `fpdf2`, we strongly encourage you to execute your scripts
with the `-Wd` option (_cf._ [documentation](https://docs.python.org/3/using/cmdline.html#cmdoption-W))
in order to get warned about deprecated features used in your code.
This can also be enabled programmatically with `warnings.simplefilter('default', DeprecationWarning)`.

Now, there are the notable recent API changes in `fpdf2`:

* the font caching mechanism, that used the `pickle` module, has been removed, for security reasons,
  and because it provided little performance gain (_cf._ [issue #345](https://github.com/PyFPDF/fpdf2/issues/345)).
  That means that the `font_cache_dir` optional parameter of `fpdf.FPDF` constructor
  and the `uni` optional argument of `add_font()` are deprecated:
  **`uni=True` can now be removed from all calls to `add_font()`**.

* the parameter `ln` to `cell()` and `multi_cell()` is now deprecated: **use `new_x` and `new_y` instead**.


## borb

[![](https://raw.githubusercontent.com/jorisschellekens/borb/master/logo/borb_64.png)](https://borbpdf.com/)

In November of 2020, Joris Schellekens released another excellent pure-Python library dedicated to reading & write PDF: [borb](https://github.com/jorisschellekens/borb/).
He even wrote a very detailed e-book about it, available publicly there: [borb-examples](https://github.com/jorisschellekens/borb-examples/).

In many ways, `borb` excels in areas where `fpdf2` has gaps:
it has a very clean and well-structure code API, with well-defined PDF primitive data-types and type hints (checked with `mypy`),
it offers several options for [pages layout](https://github.com/jorisschellekens/borb-examples/#223-setting-a-pagelayout),
it can [parse PDF files](https://github.com/jorisschellekens/borb-examples/#5-working-with-existing-pdfs) and even [extract tables](https://github.com/jorisschellekens/borb-examples/#71-extracting-tables-from-a-pdf),
it even allows you to insert [forms](https://github.com/jorisschellekens/borb-examples/#4-forms) or [Javascript code](https://github.com/jorisschellekens/borb-examples/#439-adding-a-javascriptpushbutton-to-a-pdf).

If ever you want to combine usage of `borb` **and** `fpdf`,
we provide some guidance in doing so: [documentation](https://pyfpdf.github.io/fpdf2/borb.html).

## borb vs fpdf2

I have 2 intents in drawing this comparison:

* help Python coders chose the library that best fit their need
* figure if `fpdf2` is indeed the fastest of the 2 libraries, as I suspect 😁

<u>First</u>, there are a couple of features that only `fpdf2` offers: SVG support (`borb` [rasters](https://en.wikipedia.org/wiki/Rasterisation) `.svg` files to pixelated images)
and some useful methods to generate a [table of contents](https://pyfpdf.github.io/fpdf2/DocumentOutlineAndTableOfContents.html).
On the other hand, `borb` offers **many** other features not provided by `fpdf2`...
So **from the point of functionality, borb is much more complete**.

<u>Second</u>, I think `fpdf2` CD/CI pipeline is a bit more powerful ([YAML source](https://github.com/PyFPDF/fpdf2/blob/master/.github/workflows/continuous-integration-workflow.yml) / [GitHub Actions pipeline execution](https://github.com/PyFPDF/fpdf2/actions/runs/2212594208)):
we run hundreds of unit tests based on PDF reference files, with 3 validators checking the PDF files generated,
and we test all this with the 4 latest version of Python 3. We also use [Pylint](https://pylint.pycqa.org/en/latest/) & [bandit](https://github.com/PyCQA/bandit).
`borb` [current CD/CI pipeline](https://github.com/jorisschellekens/borb/blob/master/.github/workflows/python-publish.yml) currently does none of this,
while the number of unit tests of the two libraries is comparable (346 for `borb`, 390 for `fpdf2`).
Added with the fact that `fpdf2` has been in use for a longer time (since 2006),
I'd say that **`fpdf2` is slightly more robust than `borb`**.

<u>Third and finally</u>, **let's benchmark**! 💥💨

I wrote the following script to compare `borb` & `fpdf2` performances on a specific usage scenario:
[benchmark_borb_vs_fpdf2.py](https://github.com/PyFPDF/fpdf2/blob/master/scripts/benchmark_borb_vs_fpdf2.py).

There is its execution result on my computer:

```
Speed benchmark: how much time each lib takes to generate a 10 thousands pages PDF with ~180 distinct images?
  (disclaimer: the author of this benchmark is fpdf2 current maintainer)
Versions tested: borb version 2.0.24 VS fpdf2 v2.5.2

Benchmarking fpdf2...
Memory usage peak (resource.ru_maxrss): 47MB
Generated PDF file size: 2.68MB
Duration: 1.87s

Benchmarking borb...
Memory usage peak (resource.ru_maxrss): 646MB
Generated PDF file size: 0.36MB
Duration: 71.35s
```

There are the resulting PDF files:

* [borb-10000-pages.pdf](images/2022/04/borb-10000-pages.pdf)
* [fpdf2-10000-pages.pdf](images/2022/04/fpdf2-10000-pages.pdf)

Now, what can we conclude <u>in this usage scenario</u>?

* **`fpdf2` is faster than `borb`** (by a factor ~40)
* **`fpdf2` use less memory than `borb`** (by a factor ~15)
* **`borb` produces smaller PDFs than `fpdf2`** (by a factor ~10), but **at a cost**:
  if you check the files produced, the images in the PDF made with `borb` contain **visible [artifacts](https://en.wikipedia.org/wiki/Artifact_(error))** due to compression

Finally, while crafting this benchmark script, I triggered several crashes of `borb`.
There are documented as comments in the script (it did not like some PNG files, and opening many images caused an `OSError: [Errno 24] Too many open files`)
and I think this supports my previous analysis regarding `fpdf2` robustness compared to `borb`.

I hope that this comparison will be useful to pythonistas around here.
I'd like to stress that I really admire & respect Joris Schellekens work on `borb`,
and that this analysis may be biased by the fact that I'm `fpdf2` current maintainer.
I encourage every reader to make their own list of criteria that matter, depending on their own project.

---

That's it for today regarding `fpdf2`!
You can also check the detailed [CHANGELOG](https://github.com/PyFPDF/fpdf2/blob/master/CHANGELOG.md)
for an exhaustive list of all changes: bug fixes, other minor improvements and deprecation notices.

I'd like to give a shout-out to all `fpdf2` contributors,
and especially [@torque](https://github.com/torque) & [Georg Mischler](https://github.com/gmischler),
for continually improving this library through code contributions, bug reports, improved documentation, [translations](https://github.com/PyFPDF/fpdf2/issues/267), etc.

![Thank you!](images/2022/04/chibird-thank-you.png)

I'd like to end this article with an announcement: after making [Undying Dusk](https://lucas-c.itch.io/undying-dusk) last year,
I am now working on a new PDF game! It will be made using `fpdf2` again, but this time I'm working with French illustrator [Elliot Jolivet aka Tenseï](https://chezsoi.org/lucas/blog/elliot-jolivet-aka-tensei.html)
who will provide all the game visuals. More about this soon!

Now, I wish you all to have a lot of fun building PDFs with `fpdf2` & `borb`!


<style>
article img { max-height: 12rem; }
article h2 { padding-top: 2rem; }
article hr { margin: 3rem; }
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
