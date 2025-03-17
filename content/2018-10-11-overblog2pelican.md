Title: From overblog to a pelican static website
Date: 2018-10-11 18:00
Lang: en
Tags: lang:en, blog, migration, pelican, python, overblog, static-site-generator, prog
Slug: overblog2pelican
---
Some time ago, I used the [overblog](https://over-blog.com) platform in order to create a blog for a long trip in Ireland.

Despite being sometimes very slow, it was overall a good platform, very easy to grasp for beginners.
The blog is now old and unused, but before destroying it I wanted to export a copy as a memory.
I also wanted to get my data back, from overblog servers onto my computer.

Because I love Python, I made a script [overblog2pelican.py](https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/overblog2pelican.py)
that performs an export of all texts and images to flat files,
so that it can be powered by [Pelican](https://blog.getpelican.com/).

![Old Pelican logo](images/2018/10/pelican-old.png)

I'm just sharing this code in case it can help someone else.
The process to run this script is the following:

1. Ensure you have Python 3 and the libs listed in the script installed
2. Create a new project using [`pelican-quickstart`](http://docs.getpelican.com/en/stable/quickstart.html#create-a-project)
3. Generate an `overblog-posts-with-dates.yaml` file from the Overblog admin page,
following the instructions at the top of my script
4. Run `python overblog2pelican.py` in the directory of your new pelican project

Feel free to leave a comment if you need any support.
