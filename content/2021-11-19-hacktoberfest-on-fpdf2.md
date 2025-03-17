Title: Hacktoberfest on fpdf2 & v2.4.6
Date: 2021-11-19 14:00
Lang: en
Tags: lang:en, libre-software, open-source, fpdf2, hacktoberfest, python, pdf, traduction, compte-rendu, pypi, github, prog, @kleph, @minitux
Slug: hacktoberfest-on-fpdf2
---

Last month, I realized late that October was [hacktoberfest](https://hacktoberfest.digitalocean.com) month!

[<img alt="Hacktoberfest 2021 logo" src="images/2021/11/hacktoberfest.jpg" style="max-height: 16rem">](https://hacktoberfest.digitalocean.com)

This online event is a month-long celebration (October 1-31) of open source software run in partnership with different software companies, with a focus on encouraging contributions to open source projects.

While I participated in the 2019 edition as a contributor, with [@kleph](https://github.com/kleph) & [@minitux](https://github.com/minitux),
this year I wanted to involve myself as a maintainer around the [fpdf2](https://pyfpdf.github.io/fpdf2/) Python project,
a minimalist PDF creation library.

[<img alt="fpdf2 logo" src="https://pyfpdf.github.io/fpdf2/fpdf2-logo.png" style="max-height: 12rem">](https://pyfpdf.github.io/fpdf2/)

In this blog post I simply want to share my personal experience with this event.


## Set up
The first tier of October had already passed when I realized hacktoberfest had started,
so I quickly took a few actions to ensure the `fpdf2` project was ready to receive contributions from newcomers:

* I skimmed through the event rules, and ensured the repo had the `hacktoberfest` tag
* I enabled [discussions](https://github.com/PyFPDF/fpdf2/discussions) on the GitHub project,
  in hope it would allow for more casual chats with contributors (not a massive success)
* I tagged some `fpdf2` [GitHub issues](https://github.com/PyFPDF/fpdf2/issues) with the `hacktoberfest` label,
  to make it easy for curious developers to spot issues they could contribute to.
  I also tried to redact those issues in a way that would make them accessible and interesting to work on.
* I created 3 extra `good first issues`, aimed at new contributors: [#256](https://github.com/PyFPDF/fpdf2/issues/256),
  [#257](https://github.com/PyFPDF/fpdf2/issues/257) & [#258](https://github.com/PyFPDF/fpdf2/issues/258).
  In the end I implemented one myself because it was fun 😁
* **post-hacktoberfest**, I also took sometime to write some issue / PR templates,
  so that when newcomers attempt to submit a bug report, a feature request, a PR or just ask a question,
  they are welcome with some nice explanatory text


## A tutorial available in 8 languages!
Among the `fpdf2` [GitHub issues](https://github.com/PyFPDF/fpdf2/issues) tagged `hacktoberfest`,
one received an outstanding number of contributions:
an issue suggesting to [**translate the one-page tutorial** (#267)](https://github.com/PyFPDF/fpdf2/issues/267).

What happened is that, mid-October, a contributor [suggested to translate the tutorial in Portugese](https://github.com/PyFPDF/fpdf2/issues/259). I though the idea was great and totally fitted with the context of the hacktoberfest, so I opened issue #267 to encourage other translations.

This was well received as this idea motivated **6 people** to contribute a translation,
making the tutorial available in 8 languages total! [Link to Tutorial](https://pyfpdf.github.io/fpdf2/Tutorial.html).


## Results & personal feedback

* **more than 50 issues & PRs** have been created since October 1st, on the `fpdf2` GitHub repo
* **v2.4.6** of `fpdf2` has been released, and it is the biggest release since I joined the project: [v2.4.6 ChangeLog](https://github.com/PyFPDF/fpdf2/blob/master/CHANGELOG.md#246---2021-11-16)
* `fpdf2` reached **300 stars ⭐** on GitHub! ✨ 🥳 🎉 🎈 🥂
* it seems like the **peak downloads per day almost doubled** since September: [Pepy stats](https://pepy.tech/project/fpdf2?versions=2.3.5&versions=2.4.2&versions=2.4.3&versions=2.4.5), [PypiStats](https://pypistats.org/packages/fpdf2)

![fpdf2 download statistics](images/2021/11/fpdf2-download-stats.png)

A huge _THANKS!_ to all the people who made contributions to `fpdf2` since October 1st:

* [Georg Mischler](https://github.com/gmischler) who made several major refactoring,
  like introducing a [FlexTemplate](https://pyfpdf.github.io/fpdf2/fpdf/template.html#fpdf.template.FlexTemplate) class, and [FPDF.local_context()](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.local_context)
* [@portfedh](https://github.com/portfedh) who added section 5 & 6 to the tutorial,
  just in time before the big wave of hacktoberfest translations!
* [@tabarnhack](https://github.com/tabarnhack) who implemented the new [arc()](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.arc) and [solid_arc()](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.solid_arc) methods
* [Mridul Birla](https://github.com/Mridulbirla13) who contributed the Hindi translation of the tutorial
* [@digidigital](https://github.com/digidigital) who contributed the German translation of the tutorial
* [@Xit](https://github.com/xit4) who contributed the Italian translation of the tutorial
* [Alexander Burchenko](https://github.com/AABur) who contributed the Russian translation of the tutorial
* [André Assunção](https://github.com/fuscati) who contributed the Portuguese translation of the tutorial
* [Quentin Brault](https://github.com/Tititesouris) who contributed the French translation of the tutorial
* [@bettman-latin](https://github.com/bettman-latin) who implemented the new [regular_polygon()](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.regular_polygon) method
* [Paula Campigotto](https://github.com/paulacampigotto) who reported a tricky bug with automated page breaks for two-columns documents, and also submitted [a PR](https://github.com/PyFPDF/fpdf2/pull/281) to fix it

It was really an amazing experience for me,
and I had this great feeling of being part of some wave of positive human energy!


## Notable new features in fpdf2 v2.4.6

**Temporary changes to graphics state variables** are now possible using `with pdf.local_context():` ... [Docstring](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.local_context).

A mechanism to **detect & downscale oversized images**:
[dedicated documentation](https://pyfpdf.github.io/fpdf2/Images.html#oversized-images-detection-downscaling).
[Feedbacks](https://github.com/PyFPDF/fpdf2/discussions) on this new feature are very welcome! Has it been useful to you? Do you see behaviour / usage improvements?

New drawing methods have also been introduced:

- [`FPDF.arc`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.arc) & [`FPDF.solid_arc`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.solid_arc) to draw arcs. A solid arc combines an arc and a triangle to form a pie slice: ...
- [`FPDF.regular_polygon`](https://pyfpdf.github.io/fpdf2/fpdf/fpdf.html#fpdf.fpdf.FPDF.regular_polygon)

**Documentation improvements**:

- new documentation on how to display equations, using Google Charts or `matplotlib`: [Maths](https://pyfpdf.github.io/fpdf2/Maths.html)
- new sections have been added to [the tutorial](https://pyfpdf.github.io/fpdf2/Tutorial.html):

    + [Creating Tables](https://pyfpdf.github.io/fpdf2/Tutorial.html#tuto-5-creating-tables)
    + [Creating links and mixing text styles](https://pyfpdf.github.io/fpdf2/Tutorial.html#tuto-6-creating-links-and-mixing-text-styles)

- the whole documentation can now be downloaded as a PDF: [fpdf2-manual.pdf](https://pyfpdf.github.io/fpdf2/fpdf2-manual.pdf)

[<img alt="fpdf2 PDF manual screenshot" src="images/2021/11/fpdf2-pdf-manual-preview.jpg" style="max-height: 16rem">](https://pyfpdf.github.io/fpdf2/fpdf2-manual.pdf)


## Final words

While I had a great time during this Hacktoberfest,
I think that for the next open source / libre software contribution event,
I'll try to pick one where I can be **physically present**.

I simply would have loved chat with the contributors at the end of the event!
To get to know a little who they are and what are their reasons for contributing.

Happy coding to you all!

<!-- Com'
* [x] notified contributors on their PRs
* [x] https://linuxfr.org/users/lucas-c/liens/retour-d-experience-du-hacktoberfest-comme-mainteneur-du-projet-fpdf2
* [x] https://www.journalduhacker.net/s/udvgeu/hacktoberfest_on_fpdf2_v2_4_6
* [x] https://www.reddit.com/r/hacktoberfest/comments/qxguse/hacktoberfest_on_fpdf2_v246/
-->
