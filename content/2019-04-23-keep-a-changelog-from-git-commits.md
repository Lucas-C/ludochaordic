Title: Keep a changelog from git commits
Date: 2019-04-23 12:00
Tags: lang:en, changelog, git, markdown, python, hesperides, open-source, oui.sncf, prog
Slug: keep-a-changelog-from-git-commits
---

Over the past years, on software programming projects where my end users where developers (other than myself or my team),
I have tried to follow the advice of this website : [keepachangelog(.com)](https://keepachangelog.com)

A changelog is [defined by Wikipedia](https://en.wikipedia.org/wiki/Changelog) as :
> a log or record of all notable changes made to a project.
> [It] usually includes records of changes such as bug fixes, new features, etc.

It is very simple to add one to a project, and brings a lot of value to its users.
You can even consume them as Atom/RSS feeds, with tools like [allmychanges.com](https://allmychanges.com).

Honestly I haven't tried other standards than [keepachangelog.com](https://keepachangelog.com),
but what I like about it is that it's **aimed at users**.

As a software library or API user, when your are faced with a bug
or when you are considering an upgrade to a more recent version,
you want to be able to rapidly scroll through a changelog and detect useful bug / security fixes,
non backward compatible changes or new useful features.

This simple format standard provides exactly that,
with a very simple Markdown structure.

<figure>
  <img src="images/2019/04/AyaMulder_FourSeasonsTree.png">
  <figcaption>I could not find an image I liked illustrating <code>changelogs</code> under a CC license,
  so I picked this one which represents a tree but reminds me of git branches
  - Four Seasons Tree by Aya Mulder <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0</a></figcaption>
</figure>

The [keepachangelog.com](https://keepachangelog.com) website clearly states as its top heading:

> Don’t let your friends dump git logs into changelogs.

Which is more or less what I am going to advice you do 😏

I think that by making the changelog contribution part of the necessary steps to make code changes,
instead of having to edit a Markdown file separately,
you won't risk to forget about it.

I recently used [gitchangelog](https://github.com/vaab/gitchangelog)
which can be configured very easily to follow [keepachangelog.com](https://keepachangelog.com) format:

- [.gitchangelog.rc](https://github.com/voyages-sncf-technologies/hesperides/blob/develop/.gitchangelog.rc):

```python
section_regexps = [
    ('Added', [r'^[aA]dded\s*:.*$']),
    ('Changed', [r'^[cC]hanged\s*:.*$']),
    ('Deprecated', [r'^[dD]eprecated\s*:.*$']),
    ('Removed', [r'^[rR]emoved\s*:.*$']),
    ('Fixed', [r'^[fF]ix(ed)?\s*:.*$']),
    ('Security', [r'^[sS]ecu(rity)?\s*:.*$']),
]

output_engine = mustache(".gitchangelog-keepachangelog.tpl")

publish = FileRegexSubst(
    "CHANGELOG.md",
    r'(?s)(<!-- gitchangelog START -->\n).*(<!-- gitchangelog END -->\n)',
    r"\1\o\2"
)
```

- `.gitchangelog-keepachangelog.tpl` mustache template simple example: <https://github.com/voyages-sncf-technologies/hesperides/blob/develop/.gitchangelog-keepachangelog.tpl>

- starting [CHANGELOG.md](https://github.com/voyages-sncf-technologies/hesperides/blob/develop/CHANGELOG.md):
```
# CHANGELOG
All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com).

It is generated from the `git` commits whose message starts with
`added:` / `changed:` / `deprecated:` / `removed:` / `fixed:` / `security:`
thanks to [gitchangelog](https://github.com/vaab/gitchangelog) :
`pip install gitchangelog pystache`
`gitchangelog`

You can still use [conventional commit messages](https://www.conventionalcommits.org), starting for example with
`chore:` / `docs:` / `refactor:` / `style:` / `test:`, they just won't be included in this changelog.

<!-- gitchangelog START -->
<!-- gitchangelog END -->
```

Then you simply execute the `gitchangelog` command in a pre-commit hook or in your release CI pipeline and _voilà_ !

Now, I am far from an expert on this subject. There are many other standards for changelogs,
and other tools to use `git` commits or pull requests to extract such history.

But I see the following advantages to using `gitchangelog`:

- it is easy to introduce to an existing code base, while preserving an existing changelog or ignoring old commits
- it lets you configure the naming convention you want to use in your commit messages
- it lets you choose whether or not to ignore commits without the required prefixes.
- it is written in Python 😉
