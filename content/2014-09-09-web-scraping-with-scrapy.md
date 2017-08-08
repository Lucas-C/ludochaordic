Title: [EN] Web scraping with Scrapy
Date: 2014-09-09 11:09
Tags: lang:en, script, grep, scrapy, python, web-scraping, rpg, image, goblin, dict, wget
Slug: web-scraping-with-scrapy
---
As a tabletop RPG game master, whenever I need to imagine a universe background for a scenario, I need illustrations to picture myself the atmosphere, and get some inspiration.
I usually simply surf the web from blog to blog, or spend some time on inspirational websites like [DeviantArt](//www.deviantart.com), [Tumblr](//www.tumblr.com), [Unurth](http://unurth.com) or [DarkRoastedBlend](http://www.darkroastedblend.com/).

But last week, I stumbled upon [Sylvain Robert great illustration gallery]( http://crpp0001.uqtr.ca/w4/campagne/images).
It has thousands of fantasy images, from D&D to comics.

But... I was only looking for goblin illustrations.

Hence, I decided to scrape all the file names from the Apache directory index pages.

My first attemps involved [`wget`](http://linux.die.net/man/1/wget) and [`httrack`](http://www.httrack.com), but I found no way to use their _spider_ mode to only list the file names **AND** ignore urls containing the string _"fichiers/"_.

Hence, my fallback solution was [Scrapy](http://scrapy.org), which leverage all the flexibility and simplicty of Python for web crawling.

In a matter of minutes, I was able to write a very basic but functional scraper.
There is a refined version:

```
from collections import Counter, OrderedDict
import json
import os
import scrapy
import urlparse

class FileUrl(scrapy.Item):
    url = scrapy.Field()

class HtmlDirectoryCrawler(scrapy.Spider):
    name = os.path.basename(__file__)
    def __init__(self, url=''):
        self.start_urls = [url]
        self.ext_counter = Counter()
    def parse(self, response):
        for href in response.xpath('//a/@href')[5:]:
        # Skipping the 5 first hrefs: Name, Last modified, Size, Description, Parent Folder
            child_url = urlparse.urljoin(response.url, href.extract())
            is_garbage = child_url.endswith('_fichiers/')
            if is_garbage:
                continue
            is_folder = (child_url[-1] == '/')
            if is_folder:
                yield scrapy.Request(child_url, self.parse)
            else:
                ext = child_url.split('.')[-1]
                self.ext_counter[ext] += 1
                yield FileUrl(url=child_url)
    def closed(self, reason):
        ordered_ext_counter = OrderedDict(sorted(
        		self.ext_counter.iteritems(),
    			key=lambda (k,v): (v,k)))
        self.log("Stats on extensions found:\n{}".format(
        		json.dumps(ordered_ext_counter, indent=4)),
                level=scrapy.log.INFO)
```

At the end of the scraping, I wanted to know the count of files per extension. To do so, I incremented a `collections.Counter` for every file processed. Then, at the end, I used a `collections.OrderedDict` and `json.dumps` to pretty-print the dictionnary of extensions frequencies.

The following command runs the scraper and dumps its output in a file named _crpp0001.uqtr.ca.json_ :

```
# time scrapy runspider --pdb -L INFO html_dir_crawler.py -a url=http://crpp0001.uqtr.ca/w4/campagne/images -o crpp0001.uqtr.ca.json
...
2014-09-09 13:47:48+0200 [html_dir_crawler.pyc] INFO: Spider opened
2014-09-09 13:47:48+0200 [html_dir_crawler.pyc] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2014-09-09 13:48:48+0200 [html_dir_crawler.pyc] INFO: Crawled 284 pages (at 284 pages/min), scraped 11343 items (at 11343 items/min)
2014-09-09 13:49:48+0200 [html_dir_crawler.pyc] INFO: Crawled 957 pages (at 673 pages/min), scraped 29275 items (at 17932 items/min)
2014-09-09 13:50:43+0200 [html_dir_crawler.pyc] INFO: Closing spider (finished)
2014-09-09 13:50:43+0200 [html_dir_crawler.pyc] INFO: Stats on extensions found:
...
            "PNG": 60, 
            "URL": 69, 
            "jpe": 70, 
            "pdf": 134, 
            "html": 162, 
            "FCW": 194, 
            "zip": 216, 
            "BMP": 235, 
            "htm": 419, 
            "psd": 608, 
            "bmp": 657, 
            "jpeg": 854, 
            "fcw": 892, 
            "db": 1051, 
            "JPG": 1192, 
            "gif": 1872, 
            "png": 2989, 
            "jpg": 27162
        }
2014-09-09 13:50:43+0200 [html_dir_crawler.pyc] INFO: Stored json feed (39340 items) in: crpp0001.uqtr.ca.json
...
real    0m45.489s
user    0m27.370s
sys     0m0.553s
```

And now I can search all those JPEG file names with a simple `grep` !


```
# grep -ic goblin crpp0001.uqtr.ca.json
35
# grep -i space crpp0001.uqtr.ca.json | grep -iv espace | wc -l
56
```
<br>

---

<br>
**EDIT**[8/10/2014]: as an exercise, you could try to scrape all the tags from [Justin Mason Weblog](http://taint.org/) and then use [tagcrowd.com](http://tagcrowd.com) (or the fantastic Javascript library [d3-cloud](http://www.jasondavies.com/wordcloud)) to generate the following tags cloud:

<img src="/lucas/blog/content/images/2014/Oct/jmason_weblog_tagscloud.png" alt="Justin Mason Weblog PNG Tags Cloud"/>