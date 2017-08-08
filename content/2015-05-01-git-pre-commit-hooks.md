Title: Git pre-commit hooks
Date: 2015-05-01 13:05
Tags: lang:en, python, git, hooks, yaml, pre-commit, sha, contribution, pip
Slug: en-git-pre-commit-hooks
---
I'd like to introduce you to an **awesome git companion** : [`pre-commit` hooks by Yelp](http://pre-commit.com).

<img src="http://pre-commit.com/pre-commit-darwin.png"/>

Git hooks are scripts that `git` executes before or after events such as: commit, push, and receive.

Git hooks are a built-in feature, but `git` does not offer much support for them: if there is a `.git/hooks/pre-commit` file, it just executes it. It's up to you to do all the wiring with existing checkers, run them consecutively and do some pretty console reporting.

[Many projects exist to do this](http://githooks.com), but in my humble opinion the Yelp one is simply awesome :

- it's really simple to install & use
- it's written in Python
- it already has [a huge list of supported checks](http://pre-commit.com/hooks.html)
- the project is mature, has a nice & supporting community, and is open to improvements

To install it on your machine, you just need [`pip`](https://docs.python.org/3/installing/), Python package manager : `pip install --user git+git://github.com/pre-commit/pre-commit.git@b68261c#egg=pre-commit`

Then you can install Yelp `pre-commit` hooks into your repository: `cd path/to/my/git/repo && pre-commit install`. This will simply create `.git/hooks/pre-commit` so that it invokes the `pre-commit` commands.

Now all your hooks configuration fits in one file: `.pre-commit-config.yaml`. For example:

```
- repo: git://github.com/pre-commit/pre-commit-hooks
  sha: cedcea550c495d536247ca23115035b17074cac7
  hooks:
  - id: trailing-whitespace
  - id: check-json
```

This config tells `pre-commit` to use 2 predefined hooks, that check for trailing whitespaces and malformed `.json` files.

The checks will automagically be executed whenever you do a commit, preventing you to commit files that don't pass the checks.
Here is an exemple of the resulting terminal output in case of a hook failure:

![](/lucas/blog/content/images/2015/08/pre-commit.png)

You can also invoke the hooks manually:

```
pre-commit run $hook_id # run one specific hook on all files ready to be commited
pre-commit run --files $file1 $file2 # run all hooks on some specific files
pre-commit run --all-files # run all hooks on all the files in the repo
```

The checks defined above live in git repositories. [Many are already available](http://pre-commit.com/hooks.html) for you tu use.
They are associated with a sha signature, used to determine which version of the hook to use. It looks a bit verbose, but as [this post](https://github.com/pre-commit/pre-commit/issues/158) explains in details, it's mandatory and you can update all your hooks to the latest version with `pre-commit autoupdate`.

And finally, after a [small contribution](https://github.com/pre-commit/pre-commit/pull/226) from your servitor, simple hooks defined directly in the config file are now supported !

Example:
```
- repo: local
  hooks:
  - id: make check
    name: Run the Makefile checks
    language: system
    entry: make check
    files: ''
  - id: pyflakes
    name: Run Pyflakes
    language: system
    entry: pyflakes
    files: .py$
  - id: vnu-html-checker
    name: Download & execute VNU HTML checker
    language: script
    entry: bin/vnu_html_checker.py
    files: .html$
```

<a href="http://www.commitstrip.com/fr/2012/03/06/pre-commit-hook-irl/">![](/lucas/blog/content/images/2015/05/Strip-SVN-800-final.jpg)</a>