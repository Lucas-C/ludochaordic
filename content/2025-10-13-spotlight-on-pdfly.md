Title: Spotlight on pdfly, the Swiss Army knife for PDF files
Slug: spotlight-on-pdfly
Date: 2025-10-13 10:30
Lang: en
Tags: lang:en, libre-software, open-source, python, library, release, pdf, pdfly, hacktoberfest, pypi, prog
---
![pdfly logo](images/2025/10/pdfly-logo.png)

Project documentation: [pdfly.readthedocs.io](https://pdfly.readthedocs.io/en/latest/)

`pdfly` is the youngest project of the [`py-pdf`](https://py-pdf.github.io/) organization.
It has been created by [Martin Thoma](https://github.com/martinthoma) in 2022.

It's simply **a CLI tool to manipulate PDF files**, written in Python and based on the [fpdf2](https://py-pdf.github.io/fpdf2/) & [pypdf](https://pypdf.readthedocs.io/en/stable/) libraries.

I'm a maintainer of the project 🙂

## What can it do?
It has meany features, including:

* **display PDF metadata** using [`pdfly meta`](https://pdfly.readthedocs.io/en/latest/user/subcommand-meta.html) and [`pdfly pagemeta`](https://pdfly.readthedocs.io/en/latest/user/subcommand-pagemeta.html) commands.
Example:
```
$ pdfly meta minimal-document.pdf
                      Operating System Data
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃         Attribute ┃ Value                     ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│         File Name │ /tmp/minimal-document.pdf │
│  File Permissions │ -rw-r--r--                │
│         File Size │ 16,978 bytes              │
│     Creation Time │ 2025-10-13 09:44:32       │
│ Modification Time │ 2025-10-13 09:44:32       │
│       Access Time │ 2025-10-13 09:44:46       │
└───────────────────┴───────────────────────────┘
                       PDF Data
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          Attribute ┃ Value                                                    ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│       CreationDate │ 2022-04-03 18:05:42+02:00                                │
│            Creator │ TeX                                                      │
│           Producer │ pdfTeX-1.40.23                                           │
│              Pages │ 1                                                        │
│          Encrypted │ None                                                     │
│   PDF File Version │ %PDF-1.5                                                 │
│        Page Layout │                                                          │
│          Page Mode │                                                          │
│             PDF ID │ ID1=b'q\x96\xc3\xe3U\xc1|\x9fS\xba\x9a\r\xcap\xcd\xd0'   │
│                    │ ID2=b'q\x96\xc3\xe3U\xc1|\x9fS\xba\x9a\r\xcap\xcd\xd0'   │
│ Fonts (embedded) │                                                          │
│   Fonts (embedded) │ /KNEUFH+CMR10                                            │
│        Attachments │ []                                                       │
│             Images │ 0 images (0 bytes)                                       │
└────────────────────┴──────────────────────────────────────────────────────────┘
```

* `pdfly` can also combine files into new PDF documents: it can **extract specific pages & merge documents** ([`pdfly cat`](https://pdfly.readthedocs.io/en/latest/user/subcommand-cat.html)); selectively **remove pages** ([`pdfly rm`](https://pdfly.readthedocs.io/en/latest/user/subcommand-rm.html)); **convert images to PDF documents** ([`pdfly x2pdf`](https://pdfly.readthedocs.io/en/latest/user/subcommand-x2pdf.html)); and even **compress documents** ([`pdfly compress`](https://pdfly.readthedocs.io/en/latest/user/subcommand-compress.html)) or **build booklets** ([`pdfly 2-up`](https://pdfly.readthedocs.io/en/latest/user/subcommand-2-up.html) & [`pdfly booklet`](https://pdfly.readthedocs.io/en/latest/user/subcommand-booklet.html)).

* `pdfly` includes some commands to **pull out specific content from PDF files**: [`pdfly extract-images`](https://pdfly.readthedocs.io/en/latest/user/subcommand-extract-images.html) & [`pdfly extract-annotated-text`](https://pdfly.readthedocs.io/en/latest/user/subcommand-extract-text.html).

* sometimes you want to edit a PDF file manually, in a text editor.
But when you do so, you break its `xref` table, that is an index of byte offsets in the document. [`pdfly update-offsets`](https://pdfly.readthedocs.io/en/latest/user/subcommand-update-offsets.html) is there to save the day, **fixing manually-edited PDF documents**, so that they can be opened in a PDF viewer again!


## Release 0.5.0 & new features
Today we released a new version: [`pdfly release 0.5.0`](https://github.com/py-pdf/pdfly/releases/tag/0.5.0).

Thanks to several contributors, including developers taking part in [Hacktoberfest](https://hacktoberfest.com/), new exciting features have been added:

* [`pdfly sign`](https://pdfly.readthedocs.io/en/latest/user/subcommand-sign.html) allows you to **easily sign PDF documents**, while [`pdfly check-sign`](https://pdfly.readthedocs.io/en/latest/user/subcommand-sign.html) makes it easy to check a PDF document signature. Thanks to [@moormaster](https://github.com/moormaster) for implementing this in PRs [#165](https://github.com/py-pdf/pdfly/pull/165) & [#166](https://github.com/py-pdf/pdfly/pull/166) 👍🙏.
* [`pdfly extract-annotated-pages`](https://pdfly.readthedocs.io/en/latest/user/subcommand-extract-annotated-pages.html) **extract only annotated pages** from a PDF, hence helping to review or rework pages from a large document iteratively. Thanks to [Hal Wine (@hwine)](https://github.com/hwine) for implementing this in PR [#128](https://github.com/py-pdf/pdfly/pull/128) 👍🙏.
* [`pdfly rotate`](https://pdfly.readthedocs.io/en/latest/user/subcommand-rotate.html) **rotate specific pages** of a document. Thanks to [Subhajit Sahu (@wolfram77)](https://github.com/wolfram77) for implementing this in PR [#98](https://github.com/py-pdf/pdfly/pull/98) 👍🙏.

## What's next?
We have a bunch of feature ideas: [`up-for-grabs` issues](https://github.com/py-pdf/pdfly/issues?q=is%3Aissue%20state%3Aopen%20label%3Aup-for-grabs), including some [`good first issues`](https://github.com/py-pdf/pdfly/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22) aimed specially at **new contributors**, that are willing to help but new to open-source.

Personally, I think the `pdfly sign` & `check-sign` could become handy to many end-users, and I think we should continue to extend those commands usage options, as described in [issue #71](https://github.com/py-pdf/pdfly/issues/71).

We would also be happy to get your feedbacks, bug reports & feature suggestions! 🙂

<!--
Com':
* [ ] https://dev.to/lucasc/
* [ ] https://news.ycombinator.com/
* [ ] https://www.reddit.com/r/hacktoberfest/
-->
