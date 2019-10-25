Title: GitHub project statistics and Python interactive coding
Date: 2019-10-14 8:00
Tags: lang:en, git, github, python, statistics, javascript, oui.sncf, open-source, charts, pelican, hesperides, tutorial, practical-exercise, visualization, prog
Slug: github-project-statistics-and-python-interactive-coding
Image: images/2019/10/GitHub_issues_over_time.png
---

<div style="text-align:center;">
  <iframe src="https://chezsoi.org/lucas/blog/images/2019/10/github-stats.html">
  <p>Iframes not supported. Click on the link below to access the graphs.</p>
</iframe></div>

The `iframe` above displays some graphs I've built last week,
in order to get some insight on some GitHub projects _issues_ & _pull requests_ evolution.
They are directly inspired by [nf-core project activity statistics](https://nf-co.re/stats#github_prs).

<p class="centered-content">
   <a target="_blank" href="https://chezsoi.org/lucas/blog/images/2019/10/github-stats.html">
   Click here to open those graphs in another tab</a>
</p>

In this post, I will explain step by step how I wrote a Python script that can generate those graphs
for any GitHub project. This script is available [as a gist](https://gist.github.com/Lucas-C/5c9730756e7b3f795c6d121d38a9ce88), but the last part of this article is structured as a practical exercise, to guide you to write it yourself.

- [Goal & methodology](github-project-statistics-and-python-interactive-coding.html#goal--methodology)
- [Minimal starting code](github-project-statistics-and-python-interactive-coding.html#minimal-starting-code)
- [Libraries](github-project-statistics-and-python-interactive-coding.html#libraries)
    * [Python Libraries](github-project-statistics-and-python-interactive-coding.html#python-libraries)
    * [Javascript Libraries](github-project-statistics-and-python-interactive-coding.html#javascript-libraries)
- [Code structure](github-project-statistics-and-python-interactive-coding.html#code-structure)
    * [main](github-project-statistics-and-python-interactive-coding.html#main)
    * [parse_args](github-project-statistics-and-python-interactive-coding.html#parse-args)
    * [build_page](github-project-statistics-and-python-interactive-coding.html#build-page)
    * [watch_and_serve](github-project-statistics-and-python-interactive-coding.html#watch-and-serve)
    * [reload_script](github-project-statistics-and-python-interactive-coding.html#reload-script)
- [Adding features step by step](github-project-statistics-and-python-interactive-coding.html#adding-features-step-by-step)
    * [Step 1](github-project-statistics-and-python-interactive-coding.html#step-1)
    * [Step 2](github-project-statistics-and-python-interactive-coding.html#step-2)
    * [Step 3](github-project-statistics-and-python-interactive-coding.html#step-3)
    * [Step 4](github-project-statistics-and-python-interactive-coding.html#step-4)

---

## Goal & methodology

Initially, I was struggling to find a tool that would produce graphs of a GitHub project _issues_ & _pull requests_ growth.

Some useful tools exist to analyze a project activity, like [gitstats](http://gitstats.sourceforge.net), that can generate a very complete graphical report of a `git` repository history, but does not provide any statistics on _issues_ & _PRs_.

That is when I discovered the [nf-core website page dedicated to measuring their project activity « in numbers »](https://nf-co.re/stats#github_prs), made by [Phil Ewens](https://github.com/ewels).
After [asking permission to reuse them](https://github.com/nf-core/nf-co.re/issues/190),
I decided to write a Python script that would generate those graphs.

It happens that in the last few months I have written several Python scripts with a similar purpose: **querying an HTTP API** and **generating an HTML page from this data**.

Sounds simple, isn't it ? 😉
It doesn't require complicated code, but there a few tips & tricks I used that I think are worth sharing,
including how to **program iteratively with code auto-reloading**.

In the next sections I will describe in details the nuts and bolts of this approach.
I'll start by describing some Python come that make a good starting point for this kind of script.
Then I'll guide you through the steps needed to generated GitHub activity graphs.

---

## Libraries

Before detailing what this script does, let's present its foundations:
the libraries it uses.

### Python libraries

In Python, it is standard to bundle code dependencies as packages,
hosted on [Pypi](https://pypi.org).

You can easily install the packages needed for this script by using [`pip`](https://pip.pypa.io/en/stable/installing/):

    pip install jinja2 livereload requests xreload

Now let's explain briefly what are those libraries useful for:

- [**jinja2**](https://jinja.palletsprojects.com) allow to combine _template files_
with _code variables_ using a specific syntax made of _mustaches_ like `{{ }}` or `{% %}`.
In our case, we will generate a `page.html` file based on a `template.html` file.

- [**livereload**](https://github.com/lepture/python-livereload/) provides two services:
it can `.serve()` files as an HTTP server, so that you will be able to navigate with your web browser to <http://localhost:5500/page.html>, and it can `.watch()` for changes on some target files,
in our case in order to trigger a new generation of `page.html` **and** to instruct your browser to reload this page.
This is made possible because `livereload` actually injects some Javascript code in the HTML
of the pages it serves.

- [**requests**](https://2.python-requests.org) is maybe the most handy Pypi package ever,
as it will allow you to perform HTTP requests easily.
We do not use it in our initial minimal code, but we will need it in later steps to get data from GitHub.

- [**xreload**](https://github.com/Lucas-C/xreload) is initially a script written by Guido van Rossum and named [xreload.py](http://svn.python.org/projects/sandbox/trunk/xreload/), but made Python3-compatible and uploaded on Pypi to make things easier. Its purpose is to _hot reload_ a Python module. In our case that means, when we run `./build_page.py --watch-and-serve`, to update all the objects in the running Python interpreter, each time we save new changes made on the file `build_page.py`.

Because Python comes with batteries included, it has many useful _built-in_ modules.
We rely on two of them here:

- [**argparse**](https://docs.python.org/3/library/argparse.html) is a powerful parser for command line arguments (things like `--help` or `-n 1` passed to a program).

- [**webbrowser**](https://docs.python.org/3/library/webbrowser.html) will ask your default web browser to open a given URL.

### Javascript libraries

Later on in this tutorial, I will introduce some Javascript code.
So let's also mention JS libraries :

- I used the same one to draw graphs as my model [nf-core statistics page](https://nf-co.re/stats#github_prs) :
the [ChartJS](https://www.chartjs.org) library.

- on other projects I often used [DataTables JS](https://datatables.net),
which adds very handy features to HTML `<table>` elements.
Here is a starting code if you want to use it, in this case with `jQuery`:
```
<script>
const queryParams = new URLSearchParams(location.search);
$(document).ready(() => {
    $('#id-of-your-table').DataTable({
        pageLength: 100,
        order: [[ 0, 'asc' ]],
        search: { search: queryParams.get('search') || '', },
        createdRow: (row, data) => {
            console.log('data:', data);
            if (data[1].toLowerCase() === 'warning') {
                $(row).addClass('warning');
            }
        }
    });
});
</script>
```

---

## Minimal starting code
I usually start with those 2 files:

- [`template.html`](https://github.com/Lucas-C/ludochaordic/blob/master/content/github-project-statistics-and-python-interactive-coding/step0/template.html): nothing really fancy here, apart from the [jinja2](https://jinja.palletsprojects.com)
`{{mustaches}}`, which will render the value of the variable `name` or display `World` if it is undefined or empty
```html
{! github-project-statistics-and-python-interactive-coding/step0/template.html !}
```

- [`build_page.py`](https://github.com/Lucas-C/ludochaordic/blob/master/content/github-project-statistics-and-python-interactive-coding/step0/build_page.py): I will go through this script in details below
```python
{! github-project-statistics-and-python-interactive-coding/step0/build_page.py !}

```

Go and try it !
Create those files on your computer and call `python3 build_page.py --watch-and-serve`.
A web page should open in your web browser.
Now, without shutting down the script:

- try to change the `Hello` word in `template.html`
- try to change the value of the `name` variable on line 27 of `build_page.py`

---

## Code structure
To start with, notice that the first line of the script is `#!/usr/bin/env python3`.
This is called a [_shebang_](https://en.wikipedia.org/wiki/Shebang_(Unix)).
If you make the Python file executable (_e.g._ by calling `chmod u+x build_page.py`),
and invoke this script as a command (_i.e._ `./build_page.py`),
your shell will read this line and know it needs to use the Python 3 interpreter to execute the script coming after in the file.
Moreover, by using `env` instead of specifying the exact path to the `python3` command,
we ensure that the correct interpreter will be used if using a [`virtualenv`](https://virtualenv.pypa.io).

Now, if we focus on the functions only, and the order in which they are called in this script,
we could summarize it like that:
```
main()
  parse_args()
  build_page()
  watch_and_serve()
    reload_script()
```

Those functions are defined _top-down_ : starting from the program entry point to the most specific subroutines.

Let's go through them in details.

### main

This is the program entry point.
It is called when the script is loaded and both those conditional expressions are true:

- `__name__ == '__main__'`: this _guard_ is very common in Python scripts,
to avoid executing the `main` entrypoint if one just import functions from the module,
_e.g._ with `from build_page import parse_args`.

- `'RELOADING' not in __annotations__`: this ensure the `main` function is not called when using `xreload`.
The [reload_script](github-project-statistics-and-python-interactive-coding.html#reload_script) section will explain this further.

### parse_args

This function define all the command line arguments that the script accept,
perform their _parsing_ and return and object `args` containing the corresponding _flags_.

Our script will have two main operating modes: either it will simply generate the HTML page and stop,
or it will run indefinitely, serving the generated web page as an HTTP server and hot-reloading changes made to files.

To enable this later mode, we define a single boolean option.
`args.watch_and_serve` will be `True` if `--watch-and-serve` is provided,
and else its value will be `False`.

### build_page
This function will contain our main logic.
For now it only uses `jinja2` to construct the resulting HTML page.
Note that we pass the variables to use in the template to the `.render` method.

By using the `PARENT_DIR` constant, we ensure that the file paths used are all relative
to the `build_page.py` script parent directory.
This way, if we are in the directory `/tmp` in a console shell,
and we call `/var/scripts/build_page.py`, the generated `page.html` will be created in `/var/scripts`.

### watch_and_serve

This function basically configures `livereload`.
It tells it to serve files in the `PARENT_DIR` directory on `localhost:5500`;
to watch for changes made in the `template.html` file and then to rebuild `page.html`;
to watch for changes made in the `build_page.py` (which is the value of `__file__`)
and then to reload the script and rebuild `page.html`;
and finally it opens `http://localhost:5500/page.html` in the default web browser.

### reload_script

This function reload the current module (retrieved with `sys.modules[__name__]`)
from the file `build_page.py`.
In doing so, it adds an annotation `RELOADING` to the module,
so that the `main()` function is not re-executed.

---

## Adding features step by step

Now that we have our code skeleton,
let's iterate while `python3 build_page.py --watch-and-serve` is running !
For each step below, let's add code to `template.html` & `build_page.py` to implement new features.

The goal here is to generate 2 graphs of GitHub _issues_
and _pull request_ over time for a given repository,
taking inspiration from [the nf-co.re website](https://nf-co.re/stats#github_prs).

As this can make a good coding exercise, I'm going to explain for each step what I want to achieve,
so that you can try it yourself. I'll provide the source code I ended up with myself after each step.

### Step 1

First, let's focus on the HTML + Javascript part.

Having got approval from [Phil Ewes & the nf-core project](https://github.com/nf-core/nf-co.re/issues/190)
to reuse their layout, my first goal was to strip down the <https://nf-co.re/stats> page to the
very minimal code that would display those graphs.

After copy-pasting the web page source code into the `template.html` file,
you will realize that the rendered page is broken, because it has many dependencies to other JS & CSS files served on relative paths.

To fix this, for every `<script>` or `<link>` tag, either get rid of it
(`googletagmanager`, `leaflet`, `hammer.min.js`, `canvas2svg.js`, `FileSaver.js`, `jquery.tablesorter.min.js`, `popper.min.js`, JS & CSS for code highlighting...) or replace it by a CDN-hosted version.
I usually prefer to have all my dependencies _on-disk_ and to serve them with `livereload`,
but in the context of this exercise I prefer to keep things really simple and stick with only two source files.

Two special cases remain: `nf-core.js`, which on further inspection reveals to be useless
in the context of those 2 graphs, and `nf-core.css`,
which you can shorten up and incorporate as an _inline_ `<style>` tag.
Finally, get rid of all the unnecessary HTML & JS code, including the "Download as SVG" button.

The `chartData[].data.datasets[].data` array in the main inline `<script>`
contains the data points to display in the graphs. You can also make it shorter.
For now, just define a bunch of _hardcoded_ dummy data points.

The resulting code at the end of this step: [step1/](https://github.com/Lucas-C/ludochaordic/tree/master/content/github-project-statistics-and-python-interactive-coding/step1/).

### Step 2

Now, let's prepare the data retrieval
by setting up a local file cache and adding command line options.

Why using a cache ? Two reasons: to avoid hitting [GitHub rate limit of 60 requests per hour if unauthenticated](https://developer.github.com/v3/#rate-limiting), and to speed things up by avoiding to repeat HTTP calls that have already been made.

The idea is to systematically write all the JSON responses to a `dump.json` file,
and to use this file instead of making HTTP requests if the `--use-dump` option is passed to the script.

As you add this option to the `argparse` parser, use this occasion to introduce a required argument specifying which
GitHub repository to target. Because the command line arguments are not parsed again on every "reload",
you will have to **restart the script** when you edit the `parse_args` function, otherwise you'll get an

    AttributeError: 'Namespace' object has no attribute ...

In terms of code structure, we're going to add two new functions, `read_dump` & `write_dump`.
You can also factor-out the code dedicated to generate the HTML file into a `generate_html` function.
Finally, initiate a `get_github_stats` function returning some dummy data:
a dict with 2 fields: `org_repo` (a string) and `issues` (an array).

This is an opportunity to remove our _hardcoded_ data from `template.html`,
and inject it from the Python code by using `jinja`.
Use this syntax to insert the charts data points: `{% for x, y in issues %} ... {% endfor %}`.

And to build the page title, use the `org_repo` variable like this:

    <a href="https://github.com/{{org_repo}}">{{org_repo}}</a> in numbers

The resulting code at the end of this step: [step2/](https://github.com/Lucas-C/ludochaordic/tree/master/content/github-project-statistics-and-python-interactive-coding/step2/).

### Step 3

Next step: perform the data retrieval from GitHub API.

The data we need for our use case is relatively simple to obtain:
all _issues_ & _pull requests_ information is accessible through [the `issues` resource](https://developer.github.com/v3/issues/) as a JSON document: `https://api.github.com/repos/$org/$repo/issues`.

We need to be careful about two things though:

- by default closed _issues_ are not returned, so we need to provide a `state=all` query parameter.

- the data returned is [paginated](https://developer.github.com/v3/guides/traversing-with-pagination/).
To get all the data, we need to request this resource with an incrementing `page` query parameter
as long as it does not return an empty response.
**Code tip:** you can get a forever incrementing integer variable by using [`itertools.count`](https://docs.python.org/3/library/itertools.html#itertools.count):

```python
for page in count(1):
    ...
```

As a bonus, for users with a GitHub account and willing to use this script authenticated,
if a `GITHUB_OAUTH_TOKEN` environment variable is defined,
you can pass it to the API as [an HTTP header `Authorization` token](https://developer.github.com/v3/#oauth2-token-sent-in-a-header).

Because the resulting `github_stats['issues']` data is not correctly formatted for our template,
we will stick with dummy data for now and implement a valid `pre_process` function in next step.

The resulting code at the end of this step: [step3/](https://github.com/Lucas-C/ludochaordic/tree/master/content/github-project-statistics-and-python-interactive-coding/step3/).

### Step 4

Finally, let's transform the data to fit our template needs.

The goal here is to use our `github_stats['issues']` data to build the 4 arrays needed by our graphs:

- `open_issues_count_over_time`
- `closed_issues_count_over_time`
- `open_prs_count_over_time`
- `closed_prs_count_over_time`

Start by generating a `dict` named `issues_per_creation_day` that associate to a given day all the issues created on that date. [`collections.defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict) may be useful here. You retrieve the creation date base on the `created_at` field in GitHub data, but you will have to shorten it because our date must have a format like `2019-05-10`.

Once you have this `issues_per_creation_day dict`, you should be able to be build the other 4 arrays,
by filtering issues depending on their `state` (`closed` or not),
and if they have a `pull_request` field, indicating they are actually _pull requests_ and not simple _issues_.

Finally, if you want the same result as the [nf-core project activity statistics](https://nf-co.re/stats#github_prs),
take care to build cumulative statistics.

The resulting code at the end of this step: [step4/](https://github.com/Lucas-C/ludochaordic/tree/master/content/github-project-statistics-and-python-interactive-coding/step4/).

---

## Conclusion

This method can be applied in many other situations,
whether an HTML page is involved or not.
It is very useful and frequent to use this approach when coding video games for example,
and I think that Markus @notch Persson used some code auto-reloading when he wrote his [Ludum Dare entry _Prelude of the Chambered_](http://ludumdare.com/compo/ludum-dare-21/?action=preview&uid=398).

If you want to streamline your code once you are satisfied with it,
the whole `watch-and-serve` logic can be easily removed in the end.

I hope this Python code will be useful to you !
If you use this approach yourself,
or if you're willing to give me some feedback on this article,
please add a comment below 😉
I'll try to answer you questions if you have any !

**[EDIT 2019/10/16]:** I stumbled upon this which seems promising as an alternative to `xreload`:
<https://github.com/CFSworks/limeade>

**[EDIT 2019/10/24]:** there is also this: <https://github.com/julvo/reloading>

<style>
article iframe {
  width: 100%;
  height: 75vh;
}
article hr {
  margin: 4rem !important;
}
.centered-content {
  text-align: center;
}
</style>

<script>
['h3', 'h3'].forEach(function (selector) {
    document.querySelectorAll(selector).forEach(function (header) {
        if (!header.classList.length) {
            header.id = header.textContent
                              .toLowerCase()
                              .replace(/[()?:,'&]/g, '')
                              .replace(/[à]/g, 'a')
                              .replace(/[ç]/g, 'c')
                              .replace(/[éêè]/g, 'e')
                              .replace(/[ï]/g, 'i')
                              .replace(/ /g, '-');
        }
    });
});
</script>

