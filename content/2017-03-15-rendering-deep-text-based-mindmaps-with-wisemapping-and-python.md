Title: Rendering deep text-based mindmaps with WiseMapping and Python
Date: 2017-03-15 20:03
Tags: lang:en, python, mindmap, javascript, bundle, framasoft, markdown, prog
Slug: rendering-deep-text-based-mindmaps-with-wisemapping-and-python
---
In this blog post, I'm going to demonstrate how to reuse [WiseMapping](http://wisemapping.com) HTML+JS rendering engine to easily visualize...
<pre>text-based mindmaps
    like this one
    have many benefits
        they are readable as-it-is
        they don't require any tool to be edited
        [they follow the UNIX tenets](http://www.ru.j-npcs.org/usoft/WWW/LJ/Articles/unixtenets.html)
</pre>

For the impatient ones, [here](/lucas/mindmap/mindmap-viewer/?text_based_mindmaps) is the result (click & drag to center the mindmap):
<iframe src="/lucas/mindmap/mindmap-viewer/?text_based_mindmaps" height="200" width="800"></iframe>

And you'll find [here](https://github.com/Lucas-C/linux_configuration/tree/master/languages/python/mindmaps) all that is required to launch this viewer yourself:
```
./build_viewer.sh
./wisemapping_txt2xml.py text_based_mindmaps.txt > wise-editor/src/main/webapp/samples/text_based_mindmaps.xml
python3 -m http.server
```
You only need: `git`, `python3`, `rsync` and `sed`.

**EDIT [2017/08/02]**: in the end I put the viewer in a separate repo: https://github.com/Lucas-C/wisemapping-simple-viewer

### Genesis of the project

Perfect time to slip in [one of their songs](https://www.youtube.com/watch?v=ZujuYiweht8).

The reason behind this experiment (and [this previous one with graphviz](/lucas/blog/2017/02/22/en-solarized-mindmaps-with-python-and-graphviz/)) is that I wanted to leave the excellent [Freeplane](http://www.freeplane.org) mindmapping software for a text file based solution, in order to store my mindmaps in Gitlab.

Using graphviz has some severe limitations : big mindmaps are hard to read and navigate due to the absence of a folding mechanism, links are not clickable, etc.

Then I realized an Open-Source mindmap software, [WiseMapping](http://wisemapping.com), was in fact a web interface built on top of a Java REST API. So I planned to write a mock API in Python in order to answer the required HTTP calls to display a mindmap based on a text file.

### Poking around

To begin with, I followed the project README instructions:
```
cd wise-webapp
mvn jetty:run-war -Dmaven.test.skip=true
cd -
mvn assembly:assembly -Dmaven.test.skip=true
python3 -m http.server
```

The tests systematically failed, hence I passed `-Dmaven.test.skip=true` to all the Maven commands.
I'more Python than Ruby, so I replaced the command they used to serve the static files by a Python one.

Quickly, I realized that it would be even easier than I thought: most of the code logic was in Javascript, the API only serving as a mindmap save/restore mechanism. Zero call to the Java process is made when loading the default `welcome.xml` mindmap in [`viewmode.html`](https://bitbucket.org/wisemapping/wisemapping-open-source/src/v4.0.3/wise-editor/src/main/webapp/html/viewmode.html) !

### Extracting the HTML+JS mindmap renderer from WiseMapping

If you look at [`build_viewer.sh`](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/mindmaps/build_viewer.sh#L6) you'll see that I use `rsync` to extract from the repo only [a few files](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/mindmaps/rsync.include) required to run the viewer. They are mostly JS & image files, and not even all of them are needed !

Looking at my browser Network tab, I figured out that the `mapId = 'welcome'` in [`viewmode.html`](https://bitbucket.org/wisemapping/wisemapping-open-source/src/v4.0.3/wise-editor/src/main/webapp/html/viewmode.html#viewmode.html-25) was the name of an XML file in the [samples/] (https://bitbucket.org/wisemapping/wisemapping-open-source/src/v4.0.3/wise-editor/src/main/webapp/samples/) directory that was loaded and parsed by the app.

Instead of this default value, I just changed the code to load the XML file corresponding to the query string:

    mapId = location.search.substr(1) || 'welcome'

### WTF is JSPomLoader ???

Strangely, loading a mindmap was really slow. Here is what Firefox Network tab showed when loading the viewser in a new private window:

![](images/2017/03/Firefox_WiseMapping_RequestCount1.png)

I realized that for some crazy reason, when the JS editor component was loading, it retrieved the Maven `pom.xml` file from disk, parsed it and then loaded those files one per one ! And with jQuery adding a `?_=${timestamp}` query parameter each time, to avoid browser caches !! `JSPomLoader` is the class responsible for this absurdity this in [mindplot-min.js](https://bitbucket.org/wisemapping/wisemapping-open-source/src/v4.0.3/wise-editor/src/main/webapp/js/mindplot-min.js).

I decided to build a JS bundle instead. After some experiments with `xmlstartlet` and `browserify`, I realized it was doable in [just 3 simple commands](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/mindmaps/build_viewer.sh#L15):
```
cd mindplot/src/main/javascript
sed -n '/<includes>/,/<\/includes>/{/<includes>/d;/<\/includes>/d;p}' ../../../../wisemapping-open-source/mindplot/pom.xml | sed -e 's~${basedir}~../../..~' -e 's~\s*<include>~~' -e 's~</include>$~~' > js_sources
cat js_sources > ../../../../wise-editor/src/main/webapp/js/mindplot-bundle.js
cd -
sed -i '$d' wise-editor/src/main/webapp/js/editor.js
cat wise-editor/src/main/webapp/js/mindplot-bundle.js >> wise-editor/src/main/webapp/js/editor.js
```

The second command makes `editor.js` use our new `mindplot-bundle.js` instead of `mindplot-min.js` by replacing its last JS line.

The result:

![](images/2017/03/Firefox_WiseMapping_RequestCount2.png)

### Avoiding unwanted LocalStorage cache

At this stage, I could add XML mindmaps in `wise-editor/src/main/webapp/samples/` and visualize them with `viewmode.html?file_base_name`.

However, when modifying an XML file after rendering it once, changes to the mindmap were not taken into consideration when refreshing the page.

This happened because the WiseMapping editor agressively caches mindmaps in your browser LocalStorage and does not expect changes on those XML files outside its saving mechanism. Hence I had to add this line to disable the cache:

    persistence.discardChanges(mapId);

### Converting text mindmaps to XML

Last but not least, remained to convert textual mindmaps into WiseMapping XML format.

In order to do so I wrote a [Python script](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/mindmaps/wisemapping_txt2xml.py) that uses a `pyparsing` to parse the pseudo-markdown syntax:

- Markdown:

<pre>Markdown styles
    Font styles
        **bold**
        __italic__
        __**bold italic**__
    Hyperlinks
        [My blog](https://chezsoi.org/lucas/blog)
        ![](https://chezsoi.org/lucas/blog/content/images/2014/Jul/bw-2.jpg)
</pre>

```
./wisemapping_txt2xml.py --images-size 100,100 --no-shrink markdown_example.txt > wise-editor/src/main/webapp/samples/markdown_example.xml
```
The result:
<iframe src="/lucas/mindmap/mindmap-viewer/?markdown_example" height="300" width="800"></iframe>

- WiseMaping icons (they are all in `wise-editor/src/main/webapp/icons/`)

<pre>Blah blah blah   !icon=${icon_name}</pre>

```
./wisemapping_txt2xml.py icons_example.txt > wise-editor/src/main/webapp/samples/icons_example.xml
```
The result:
<iframe src="/lucas/mindmap/mindmap-viewer/?icons_example" height="450" width="800"></iframe>

- and with inline attributes like `<!--fontStyle=";;#dfcfe6;;;" bgColor="#0a0a08"-->`, full support for all the features in the default [`welcome.xml`](/lucas/mindmap/mindmap-viewer/samples/welcome.xml) defined in an [`welcome.txt`](https://github.com/Lucas-C/linux_configuration/blob/master/languages/python/mindmaps/welcome.txt):

<iframe src="/lucas/mindmap/mindmap-viewer/?welcomeFromText" height="600" width="800"></iframe>

### Final touches

In the end, I noticed the links preview, when you hover over a node with an anchor, was broken: it uses [pagepeeker.com](http://pagepeeker.com) to create website screenshots, but oviously that doesn't work on localhost.
Comparing with [Framindmap](https://framindmap.org) fork of WiseMapping, I realized they also fixed in their own way the JS loader hell.
And in their version, they replaced the pagepeeker screenshot by a simple button, which I preferred:
```
git clone https://framagit.org/framasoft/framindmap.git
cp framindmap/webapps/wisemapping/js/mindplot-min.js wise-editor/src/main/webapp/js/mindplot-bundle.js
# puis regénérer wise-editor/src/main/webapp/js/editor.js
```
