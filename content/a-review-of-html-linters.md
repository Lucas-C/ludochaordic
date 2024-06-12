Title: A review of HTML linters
Date: 2021-08-27 14:00
Tags: lang:en, html, linter, python, source-code, vnu, w3c, continuous-integration, gitlab-ci, github-actions, travis-ci, prog
Slug: a-review-of-html-linters
Status: draft
---

... and how to use them in CI pipelines.

[Why is HTML linting not a common practice?](https://dev.to/dandevri/why-is-html-linting-not-a-common-practice-4gme)

Criterias : activity (commits / year, overview of last issues...), features (auto-fix, #number of rules...), usability (user-friendliness, ease of installation & configuration...) testing 3-4 example pages (Boostrap 4.1 Starter template, Foundation, Pure CSS, Semantic UI, UI kit, https://www.w3schools.com/html/html_examples.asp, HTML5UP)

## W3C v.Nu HTML linter
[v.Nu, the Nu HTML Checker](https://validator.github.io/validator/) from the W3C

* https://chezsoi.org/shaarli/shaare/AIzoYw
* [html5validator (Python package)](https://pypi.org/project/html5validator/)
* [vnu-jar (npm package)](https://www.npmjs.com/package/vnu-jar)
* [validator/validator (Docker image)[https://hub.docker.com/r/validator/validator/]

## Tidy HTML
* ` -modify` autoformat
* latest version allow to mute some warnings, but [the exit code will still be non-zero](https://github.com/htacg/tidy-html5/issues/933),
  making its usage in CI pipelines difficult
* [latest binaries are from 4 years ago](https://github.com/htacg/tidy-html5/issues/939)

Usage in [GitHub Actions](https://github.com/features/actions) / [Gitlab CI](https://docs.gitlab.com/ee/ci/) / [Travis CI](https://www.travis-ci.com):

```yaml
- wget -O tidy-html5.deb https://github.com/htacg/tidy-html5/releases/download/5.8.0/tidy-5.8.0-Linux-64bit.deb
- dpkg -i tidy-html5.deb
- tidy -version
- tidy -quiet -lang en -modify -config htmltidy.conf index.html
```

Example of `htmltidy.conf`:

```
// cf. https://api.html-tidy.org/tidy/quickref_next.html
char-encoding: utf8
newline: lf
indent: auto
indent-spaces: 4
wrap: no
drop-empty-elements: false
warn-proprietary-attributes: no
# Display message ID's with error reports, useful to filter them out using "mute":
mute-id: yes
```
<!-- /opt/tidy-html5/build/cmake/tidy --version # 5.7.45 -->

Note: on Lucas-C/jdr I ended up switching to the Nu HTML checker instead, because of the annoying `fix-style-tags` rule, using the latest release, and the general lack of maintenance / answers on issues / new releases on the project

## htmlhint
[htmlhint](https://htmlhint.com)

Usage in [GitHub Actions](https://github.com/features/actions) / [Gitlab CI](https://docs.gitlab.com/ee/ci/) / [Travis CI](https://www.travis-ci.com):

```yaml
- npm install -g htmlhint
```

Example of `.htmlhintrc`:

```json
{
    "tagname-lowercase": true,
    "attr-lowercase": true,
    "attr-value-double-quotes": true,
    "doctype-first": true,
    "tag-pair": true,
    "spec-char-escape": true,
    "id-unique": true,
    "src-not-empty": true,
    "attr-no-duplication": true,
    "title-require": true
}
```

- [htmllint](https://github.com/htmllint/htmllint)

Usage in [GitHub Actions](https://github.com/features/actions) / [Gitlab CI](https://docs.gitlab.com/ee/ci/) / [Travis CI](https://www.travis-ci.com):

```yaml
- npm install -g htmllint
```

Example of `.htmllintrc`:

```json
{
    "indent-width": 2,
    "id-class-style": "bem",
    "attr-name-style": "dash",
    "tag-bans": ["b", "i"], // allowing "style"
    "attr-bans": ["align", "background", "bgcolor", "border", "frameborder", "longdesc", "marginwidth", "marginheight", "scrolling", "width"], // allowing "style"
    "spec-char-escape": false
}
```

## html-validate

- [html-validate](https://gitlab.com/html-validate/html-validate)

Usage in [GitHub Actions](https://github.com/features/actions) / [Gitlab CI](https://docs.gitlab.com/ee/ci/) / [Travis CI](https://www.travis-ci.com):

```yaml
- npm install -g html-validate
```

Also mentions:
* https://github.com/twbs/bootlint
* https://github.com/motet-a/jinjalint
* usages as pre-commit hooks
