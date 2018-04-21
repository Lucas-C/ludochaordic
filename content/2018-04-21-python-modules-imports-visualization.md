Title: Python module imports visualization
Date: 2018-04-21 18:00
Tags: lang:en, python, javascript, documentation, graph, open-source, charts, visualization, prog
Slug: python-modules-imports-visualization
Status: draft
---
<script src="images/2018/04/d3.v4.min.js"></script>
<script src="images/2018/04/d3.dependencyWheel.js"></script>

```python
gen_modules_graph.py flask > modules-flask.json
```
<div id="modules-flask" style="text-align: center; padding-bottom: 4rem"></div>

```python
gen_modules_graph.py httpie.core > modules-httpie.json
```
<div id="modules-httpie" style="text-align: center; padding-bottom: 4rem"></div>

I'm using a [slightly patched](https://github.com/fzaninotto/DependencyWheel/pull/15) version of [fzaninotto/DependencyWheel](https://github.com/fzaninotto/DependencyWheel)

<script>
    function buildPkgTree(pkgPaths) {
        var tree = {};
        pkgPaths.forEach(pkgPath => {
            pkgPath.split('.').reduce((parent, pkg) => (parent[pkg] = parent[pkg] || {}), tree);
        });
        return tree;
    }
    function pkgPath2Degrees(pkgPath, maxArrLength, pkgTree) {
        var parentPkgNode = pkgTree, result = 0, baseRadix = Math.pow(360, 1 / maxArrLength);
        for (var i = 0; i < maxArrLength && pkgPath[i]; i++) {
            var parentpkgChildren = Object.keys(parentPkgNode);
            parentpkgChildren.sort();
            var pkgRatioInParent = parentpkgChildren.indexOf(pkgPath[i]) / parentpkgChildren.length;
            var weight = Math.pow(baseRadix, maxArrLength - 1 - i);
            result += weight * (pkgRatioInParent * (baseRadix - 1));
            parentPkgNode = parentPkgNode[pkgPath[i]];
        }
        return result;
    }
    function renderDependencyWheel(dependencyGraphJsonUrl, htmlElementSelector) {
        d3.json(dependencyGraphJsonUrl, function(data) {
            // Custom chords & path colors:
            var maxPkgDepth = Math.max(...data.packageNames.map(p => p.split('.').length));
            var pkgTree = buildPkgTree(data.packageNames);
            var chart = d3.chart.dependencyWheel({fill: function (d) {
                var pkgPath = data.packageNames[d.index].split('.');
                var hue = pkgPath2Degrees(pkgPath, maxPkgDepth, pkgTree);
                return 'hsl(' + hue + ', 90%, 70%)';
            }});
            d3.select(htmlElementSelector).datum(data).call(chart).call(function(selection) {
                d3.select('svg').style('overflow', 'visible');
                // Insert <a> links on module names:
                d3.selectAll('text').each(function() {
                    var oldParent = this.parentNode;
                    var newParentAnchor = document.createElementNS('http://www.w3.org/2000/svg', 'a');
                    newParentAnchor.setAttributeNS(null, 'href', 'http://gitlab.socrate.vsct.fr/dtaas/api-system/blob/master/flaskapp/' + this.textContent.replace('.', '/') + '.py');
                    newParentAnchor.setAttributeNS(null, 'target', '_blank');
                    oldParent.replaceChild(newParentAnchor, this);
                    newParentAnchor.appendChild(this);
                });
            });
        });
    }
    renderDependencyWheel('images/2018/04/modules-flask.json', '#modules-flask')
    renderDependencyWheel('images/2018/04/modules-httpie.json', '#modules-httpie')
</script>