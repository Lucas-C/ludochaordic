Title: How to install CodeCity source code visualization tool on Ubuntu
Date: 2015-03-09 14:03
Tags: lang:en, _preview
Slug: en-how-to-install-codecity-source-code-visualization-tool
---
Inspired by some recent thoughts I had and an article on InfoQ named ["Your Code as a Crime Scene"](http://www.infoq.com/news/2015/03/code-as-a-crime-scene), I wanted to install and try Richard Wettel's [CodeCity](http://www.inf.usi.ch/phd/wettel/codecity.html).

TBD

<!--
The first step was to install VisualWorks/Cincom Smalltalk 7.6. The task can be quickly summarized as "Yay ! Let's try the venerable SmallTalk !" ...and then...
<img src="/lucas/wwcb/photos/star_trek_unbelievable.gif" alt="Star Trek Head Hurts">

There's how I managed to do it:

- register a "Personal-Use" license for Cincom Smalltalk [on their website](http://www.cincomsmalltalk.com/main/developer-community/trying-cincom-smalltalk/try-cincom-smalltalk/)
- download the ISO using the link your received by email
- extract the ISO content in a directory using the Archive Manager
- open a console in that directory and `chmod u+x installUnix vw8.0pul/bin/linux86/visual`.
- launch the installer with `./installUnix`. If you want to specify a custom installation path, select "Custom Install".
- once you've been through all the graphical installer steps, you'll get a pop-up asking you to set an environment variable named `VISUALWORKS` pointing to the installation path. Proceed by defining it in your `.bashrc`.

Then stuck on:
```
$ /opt/vw8.0pul/bin/linux86/visual /opt/codecity-image/codecity.im 
VisualWorks(R) 7.5 Non-Commercial Mar 3, 2008
VisualWorks(R) 7.5 Non-Commercial Mar 3, 2008
src/stack/send.c:317
Fatal error: unexpected translation failure (selector 'value'), code = 3

Space could not be allocated.
```
-->