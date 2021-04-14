Title: A review of HTML linters
Date: 2021-04-23 14:00
Tags: lang:en, html, linter, python, source-code, vnu, w3c, continuous-integration, gitlab-ci, github-actions, travis-ci, prog
Slug: a-review-of-html-linters
Status: draft
---

... and how to use them in CI pipelines.

[Why is HTML linting not a common practice?](https://dev.to/dandevri/why-is-html-linting-not-a-common-practice-4gme)

- Tidy HTML:
  * ` -modify` autoformat
  * latest version allow to mute some warnings, but [the exit code will still be non-zero](https://github.com/htacg/tidy-html5/issues/933),
    making its usage in CI pipelines difficult
  * [latest binaries are from 4 years ago](https://github.com/htacg/tidy-html5/issues/939)

Usage in [GitHub Actions](https://github.com/features/actions) / [Gitlab CI](https://docs.gitlab.com/ee/ci/) / [Travis CI](https://www.travis-ci.com):

```yaml
- apt-get update && apt-get install -y tidy
- tidy -version
- tidy -quiet -lang en -config htmltidy.conf index.html
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
# Display message ID's with error reports, useful to filter them out using "mute":
mute-id: yes
# The following config entry requires tidy v5.6+:
warn-proprietary-attributes: no
```

- [v.Nu, the Nu HTML Checker](https://validator.github.io/validator/) from the W3C
  * [html5validator](https://pypi.org/project/html5validator/) Python wrapper
  * also npm & Docker usages

- [htmlhint](https://htmlhint.com)

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

- [html-validate](https://gitlab.com/html-validate/html-validate)


Also mentions:
* https://github.com/twbs/bootlint
* https://github.com/motet-a/jinjalint
* usages as pre-commit hooks
