Title: Python module imports visualization
Date: 2018-04-24 18:30
Tags: lang:en, python, javascript, d3-js, documentation, literate-programming, graph, open-source, charts, tree, visualization, technical-debt, git, gitlab, maths, color, oui.sncf, prog
Slug: python-modules-imports-visualization
Image: images/2018/04/flask-modules--visualization.png
---
### flask
<div id="modules-flask" style="text-align: center; padding-bottom: 4rem"></div>
### httpie
<div id="modules-httpie" style="text-align: center; padding-bottom: 4rem"></div>
### requests
<div id="modules-requests" style="text-align: center; padding-bottom: 4rem"></div>
### simplejson
<div id="modules-simplejson" style="text-align: center; padding-bottom: 4rem"></div>
### botocore
<div id="modules-botocore" style="text-align: center; padding-bottom: 4rem"></div>
### scrapy
<div id="modules-scrapy" style="text-align: center; padding-bottom: 4rem"></div>
### docker-compose
<div id="modules-docker-compose" style="text-align: center; padding-bottom: 4rem"></div>
### ansible
<div id="modules-ansible" style="text-align: center; padding-bottom: 4rem"></div>

## What are those diagrams ?

They show dependencies between the internal modules of various well-known Python libraries.

They goal is to provide a global overview of a Python project architecture, as a map of **modules & packages**, the top-level code abstractions.

Note that all module names in those diagrams are HTML links to the actual source code on GitHub.


## Why ?

At work, we did a short **technical-debt review** of one of our Python services,
and a coworker reported a lack of documentation to provide a clear overview of the code structure,
for first-time contributors to easily jump in.

Hence, last week I searched for some helpful code visualization recipes to provide such insight to our code base,
hoping to find an easy-to-setup Python module that would do the job.

I did not find any off-the-shelf package for my need (althought I'd love your suggestions if you know some !),
but discovered Francois Zaninotto's [DependencyWheel](https://github.com/fzaninotto/DependencyWheel) vizualiation of dependencies,
and decided to use it to build a nice diagram and add it to our documentation.

I thought it could be useful to others, hence this blog post to share the recipe online.


## How ?

Following the spirit of ["Modern Technical Writing"](http://idratherbewriting.com/2016/07/26/modern-technical-writing-review/)
/ ["Literate programming"](https://en.wikipedia.org/wiki/Literate_programming) / ["Living Documentation"](https://leanpub.com/livingdocumentation),
our documentation for this project at work is written in Markdown and compiled with [mkdocs](http://www.mkdocs.org) to provide a static website.
Moreover, the project is built & hosted by [GitLab Pages](https://about.gitlab.com/features/pages/).

This way, the diagram is always up-to-date with the project code.
It also made the addition of this diagram quite easy:

1. I added some code to the GitLab Pages build script to fetch the corresponding git repo and exract the modules dependencies as JSON.
2. I added some Javascript code to a Markdown page in our documentation to render the depency wheel based on this JSON

The script to extract the modules dependencies is on GitHub: [gen_modules_graph.py](https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/gen_modules_graph.py).
It is less than 100 lines and use the [modulegraph](https://pypi.org/project/modulegraph/) package to parse modules dependencies, taking care to:

- ignore modules outside of the target project
- ignore constants, functions and modules with the zero incoming & outgoing dependencies (like Python packages with an empty `__init__.py`)

Usage example:
```python
gen_modules_graph.py ansible.inventory.manager ansible.playbook ansible.executor.task_queue_manager > modules-ansible.json
```

For the rendering, I used [fzaninotto/DependencyWheel](http://www.redotheweb.com/DependencyWheel/),
originally written to display the **external** dependencies of a project (e.g. links between PHP composer packages).
I made 2 small patches / PRs to latest version of this project:

- [a single-line code change to allow for colors customization](https://github.com/fzaninotto/DependencyWheel/pull/15)
- [another minor change to make the chart adaptive to the parent DOM element width](https://github.com/fzaninotto/DependencyWheel/pull/16)

I also used some additionnal JS code to:

- ensure the dependencies matrix is square (to get prettier graphs)
- customize the colors
- add HTML anchor links

The code is available in this page source. Like the Python script, you are free to reuse it at will.

It is relatively straightforward, with a single notable trick:
the conversion from a Python module path to a [hue](https://en.wikipedia.org/wiki/Hue) color value on a 360 degrees scale.

## A little bit of maths

In order for modules with a shared ancestor to have close colors (like `http.response.html` and `http.response.text` in the `scrapy` wheel above),
I used a simple mathematical concept: decomposing the hue value with a [bijective numeration](https://en.wikipedia.org/wiki/Bijective_numeration)
into a fixed-size string of digits.

This idea is similar to the binary numeral system, notably with the same concept of most / least significant digits,
except that the range covered is `[0, 360]` and we want as many digits as the module tree depth.

Once this numeral system [base radix](https://en.wikipedia.org/wiki/Radix) is computed from those 2 constraints,
computing the hue value is simply a matter of a basic [exponentiation](https://en.wikipedia.org/wiki/Positional_notation#Exponentiation) :

<figure>
  <img alt="Python module tree" src="images/2018/04/PythonModuleTree.png">
  <figcaption>Python module tree, with module names positions for module path <code>output.formatters.headers</code> of <code>httpie</code>
          <br>(made with <a href="https://www.draw.io">draw.io</a> - <a href="images/2018/04/PythonModuleTree.xml">source xml</a>)</figcaption>
</figure>

<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=AM_HTMLorMML"></script>

<p class="formula">
  `"Let's consider a module tree of depth " D "."`

  `"Then the base radix to use in our decomposition is " R = 360^(1 / D)`

  `"Now, let " m " be a module path, constituded of " d " modules names " m_i ", with " d <= D "."`

  `"We can define " pos(m_i) " to be the position of the module name " m_i " in the sorted list of its parent module children."`

  `"We can now compute the digits of " m " in our decomposition: " d_(m_i) = (pos(m_i)) / D * (R - 1)`

  `"And then " hue(m) = sum_(i=1)^D d_(m_i)*R^i`
</p>

<script src="images/2018/04/d3.v4.min.js"></script>
<script src="images/2018/04/d3.dependencyWheel.js"></script>
<script>
    function buildModuleTree(modulePaths) {
        var tree = {};
        modulePaths.forEach(modulePath => {
            modulePath.split('.').reduce((parent, moduleName) => (parent[moduleName] = parent[moduleName] || {}), tree);
        });
        return tree;
    }
    function modulePath2Degrees(modulePath, moduleTree, moduleTreeDepth) {
        var parentModule = moduleTree, result = 0, baseRadix = Math.pow(360, 1 / moduleTreeDepth);
        for (var i = 0; i < moduleTreeDepth && modulePath[i]; i++) {
            var parentModuleChildren = Object.keys(parentModule);
            parentModuleChildren.sort();
            var moduleRatioInParent = parentModuleChildren.indexOf(modulePath[i]) / parentModuleChildren.length;
            var weight = Math.pow(baseRadix, moduleTreeDepth - 1 - i);
            result += weight * (moduleRatioInParent * (baseRadix - 1));
            parentModule = parentModule[modulePath[i]];
        }
        return result;
    }
    function renderDependencyWheel(dependencyGraphJsonUrl, htmlElementSelector, moduleUrlTemplate) {
        d3.json(dependencyGraphJsonUrl, function(data) {
            // Ensuring matrix is symmetrical to make chords more regular, thick
            var originalMatrix = JSON.parse(JSON.stringify(data.matrix));
            data.matrix.forEach((row, i) => {
                row.forEach((value, j) => {
                    if (value && !data.matrix[j][i]) {
                        data.matrix[j][i] = value;
                    }
                });
            });
            // Custom chords & path colors:
            var moduleTree = buildModuleTree(data.packageNames);
            var moduleTreeDepth = Math.max(...data.packageNames.map(p => p.split('.').length));
            var chart = d3.chart.dependencyWheel({fill: function (d) {
                var modulePath = data.packageNames[d.index].split('.');
                if (d.subindex && !originalMatrix[d.index][d.subindex]) {
                    modulePath = data.packageNames[d.subindex].split('.');
                }
                var hue = modulePath2Degrees(modulePath, moduleTree, moduleTreeDepth);
                return 'hsl(' + hue + ', 90%, 70%)';
            }});
            d3.select(htmlElementSelector).datum(data).call(chart).call(function(selection) {
                // Insert <a> links on module names:
                d3.selectAll(htmlElementSelector + ' text').each(function() {
                    var oldParent = this.parentNode;
                    var newParentAnchor = document.createElementNS('http://www.w3.org/2000/svg', 'a');
                    newParentAnchor.setAttributeNS(null, 'href', moduleUrlTemplate(this.textContent.replace('.', '/') + '.py'));
                    newParentAnchor.setAttributeNS(null, 'target', '_blank');
                    oldParent.replaceChild(newParentAnchor, this);
                    newParentAnchor.appendChild(this);
                });
            });
        });
    }
    renderDependencyWheel('images/2018/04/modules-flask.json',          '#modules-flask',          (modPath) => `https://github.com/pallets/flask/blob/master/flask/${modPath}`)
    renderDependencyWheel('images/2018/04/modules-httpie.json',         '#modules-httpie',         (modPath) => `https://github.com/jakubroztocil/httpie/blob/master/httpie/${modPath}`)
    renderDependencyWheel('images/2018/04/modules-requests.json',       '#modules-requests',       (modPath) => `https://github.com/requests/requests/blob/master/requests/${modPath}`)
    renderDependencyWheel('images/2018/04/modules-simplejson.json',     '#modules-simplejson',     (modPath) => `https://github.com/simplejson/simplejson/blob/master/simplejson/${modPath}`)
    renderDependencyWheel('images/2018/04/modules-botocore.json',       '#modules-botocore',       (modPath) => `https://github.com/boto/botocore/blob/master/botocore/${modPath}`)
    renderDependencyWheel('images/2018/04/modules-scrapy.json',         '#modules-scrapy',         (modPath) => `https://github.com/scrapy/scrapy/blob/master/scrapy/${modPath}`)
    renderDependencyWheel('images/2018/04/modules-docker-compose.json', '#modules-docker-compose', (modPath) => `https://github.com/docker/compose/blob/master/compose/${modPath}`)
    renderDependencyWheel('images/2018/04/modules-ansible.json',        '#modules-ansible',        (modPath) => `https://github.com/ansible/ansible/blob/master/lib/ansible/${modPath}`)
</script>

<style>
    h3 {
      text-align: center;
    }
    article img {
        display: block;
        margin: 0 auto;
        max-height: 30rem;
    }
    article figcaption {
        text-align: center;
    }
    .formula {
      font-size: larger;
      text-align: center;
    }
    .MathJax {
      line-height: 3rem;
    }
</style>
