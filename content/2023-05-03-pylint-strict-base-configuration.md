Title: Pylint strict base configuration
Date: 2023-05-03 13:15
Tags: lang:en, python, pylint, configuration, linter, static-code-analysis, fpdf2, github-actions, prog
---
![Pylint logo](images/2023/05/pylint-strict.webp)

[Pylint](https://pylint.pycqa.org) is a great static code analyser for Python code.
I have been using it for several years, in various projects, and it's simple to use yet very powerful.

I even contributed to Pylint by submitting a new rule a few years ago : [implicit-str-concat](https://github.com/pylint-dev/pylint/pull/1655).

For an introduction to Pylint, you can check those tutorials:

* official documentation: [Tutorial](https://pylint.readthedocs.io/en/latest/tutorial.html) & [Usage](https://pylint.readthedocs.io/en/latest/user_guide/usage/run.html)
* [How To Get Started With Pylint by Oliyadk @medium.com](https://medium.com/@oliyadkebede32/how-to-get-started-with-pylint-79bf950f61a8)

Pylint default configuration is very reasonable, but one thing that I find missing is a simple way to switch to a "strict" mode, that would enable all optional rules. ESLint has [eslint-config-strict-mode](https://www.npmjs.com/package/eslint-config-strict-mode) for example.

Such "strict" mode can be useful:

* when bootstrapping a new project, you may want to enable all rules by default,
  and progressively disable the ones you find non necessary for your project

* on an existing project using Pylint, when you want to test what extra checks
  can be performed by this tool, and see if it can spot bugs you missed so far

The following `.pylintrc` configuration file is my attempt to setup a "strict" mode:

```toml
[MESSAGES CONTROL]
# Enable some checkers that are not activated by default:
enable = bad-inline-option, deprecated-pragma, file-ignored, use-symbolic-message-instead, useless-suppression

# Include some helpful details on errors messages for naming rules:
include-naming-hint = yes

[MASTER]
# Informational messages ("I") should make Pylint execution fail (non-0 program return code):
fail-on = I
# Enable many optional extensions:
load-plugins = pylint.extensions.bad_builtin,
               pylint.extensions.code_style,
               pylint.extensions.comparison_placement,
               pylint.extensions.consider_refactoring_into_while_condition,
               pylint.extensions.docparams,
               pylint.extensions.dunder,
               pylint.extensions.eq_without_hash,
               pylint.extensions.for_any_all,
               pylint.extensions.magic_value,
               pylint.extensions.mccabe,
               pylint.extensions.no_self_use,
               pylint.extensions.overlapping_exceptions,
               pylint.extensions.private_import,
               pylint.extensions.redefined_loop_name,
               pylint.extensions.redefined_variable_type,
               pylint.extensions.set_membership,
               pylint.extensions.typing,
               pylint.extensions.while_used,

[STRING_CONSTANT]
# Doc: https://pylint.pycqa.org/en/latest/user_guide/messages/warning/implicit-str-concat.html
check-quote-consistency = yes

[VARIABLES]
allow-global-unused-variables = no
```

I recently used this approach on `fpdf2`: [PR #780 Hardening Pylint config](https://github.com/PyFPDF/fpdf2/pull/780)

Related configuration files in `fpdf2`:

* [.pylintrc](https://github.com/PyFPDF/fpdf2/blob/master/.pylintrc)
* [call in GitHub Actions pipeline definition](https://github.com/PyFPDF/fpdf2/blob/master/.github/workflows/continuous-integration-workflow.yml#L36)

I hope this `.pylintrc` could be useful to others!

You can drop a comment if this article was helpful to you 😊
