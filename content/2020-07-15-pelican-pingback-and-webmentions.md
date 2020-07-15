Title: Pelican, pingback and webmentions
Date: 2020-07-15 14:00
Tags: lang:en, libre-software, open-source, pelican, python, blog, plugin, http, html, library, release, source-code, decentralized-web, web-standards, semantic-web, linkbacks, low-tech, static-site-generator, wordpress, security, code-quality, prog, @Matt
Slug: pelican-pingback-and-webmentions
---
[Linkback protocols](https://en.wikipedia.org/wiki/Linkback) are an old breed.
They were born in a time where MySpace, Wikipedia & WordPress had just been born,
and Friendster was more popular than this new website called Facebook.

<figure>
  <img alt="Diagram showing how linkback protocols work" src="images/2020/07/linkback.gif">
  <figcaption>Diagram source: <a href="https://www.pprune.org/misc.php?do=linkbacks">PPRuNe article on linkbacks</a></figcaption>
</figure>

The latest linkback protocol, [Webmention](https://indieweb.org/Webmention), is relatively recent though,
as it became a W3C recommendation in 2017.

What are they ?

A web mechanism to **notify** `website-B.com`
when `website-A.com` publishes content that includes [a link](https://en.wikipedia.org/wiki/Hyperlink) to `website-B.com`.

Basically, `website-A.com` says “Hello `website-B.com` ! I have just written something about you, maybe you'd like to know !”

I find linkback protocols very valuable, for several reasons:

- they have strong technical features: conceptually simple, flexible, lightweight, easy to implement...
As they exist since almost 20 years, their robustness has been tried-and-tested.
- they are a web standard
- they foster a decentralized web

As such, they form a practical alternative to commenting systems of tech Giants centralized platforms.

Many publishing tools (blog engines, website frameworks...) already support linkbacks.
As an example, IndieWeb has [a long list of software that support Webmention](https://indieweb.org/Webmention#Publishing_Software).

<img class="pelican-logo" alt="Pelican logo" src="images/open-source/pelican-logo.png">

Myself, to generate this website, I am using [Pelican](https://getpelican.com),
a static blog engine written in Python.

So-called "static" websites are great: they are conceptually simple,
they are [_low tech_](https://homebrewserver.club/low-tech-website-howto.html#software),
and because they are generated only from [versionable text documents](https://en.wikipedia.org/wiki/Version_control), they are very resilient.

Sadly, static websites cannot **receive** linkbacks, as this requires some custom server-side code.
However they can perfectly well **send** linkbacks !

Hence, I have written a Pelican plugin to send linkbacks,
with support for both Pingbacks & Webmentions,
which I am now proud to introduce here:

<https://github.com/pelican-plugins/linkbacks/> [![Pypi latest version](https://img.shields.io/pypi/v/pelican-plugin-linkbacks.svg)](https://pypi.python.org/pypi/pelican-plugin-linkbacks)

There are already libraries on Pypi dedicated to publishing linkbacks, for various protocols.
However I did not find any which I was satisfied with the code quality, hence I wrote my own implementation.

![The only valid measurement of code quality: WTFs/minute](https://chezsoi.org/lucas/wwcb/photos/Best_Code_Quality_Indicator%20-WTFs_per_minute.png)

The `send_pingback` & `send_webmention` functions in `linkbacks.py` are pretty straightforward.
They are well tested, and are easily usable in another Python project:

```python
from linkbacks import *

logging.basicConfig(level=logging.DEBUG)
LOGGER.setLevel(logging.DEBUG)

send_pingback('https://chezsoi.org/lucas/blog/',
              'https://chezsoi.org/lucas/blog/pages/jeux-de-role.html')
send_webmention('https://chezsoi.org/lucas/blog/',
                'https://chezsoi.org/lucas/blog/pages/jeux-de-role.html')
```

As proof of this library correctly sending notifications, there are two websites that acknowledged reception of Pingback from this blog:

- <https://oujevipo.fr/general/4406-til-cows-tear-us-apart-web/>
- <http://lookrobot.co.uk/games/>

Many thanks to Matthieu for providing me a temporary Wordpress blog, under a different domain, for my tests !

By the way, I learned that most Wordpress websites systematically answer to Pingback requests with a very unhelpful silent `faultCode 0`, due to the default value of the `xmlrpc_pingback_error` filter ([source](https://github.com/WordPress/WordPress/blob/5.4.2/wp-includes/comment.php#L3016)). 😞
This was done to prevent [Pingback exploits](https://en.wikipedia.org/wiki/Pingback#Exploits) like the infamous [CVE-2013-0235](https://nvd.nist.gov/vuln/detail/CVE-2013-0235) ([commit source](https://github.com/WordPress/WordPress/commit/82e9c40)),
but I don't think this kind of [security through obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity) is needed.
In fact I fear that the impact of hiding the Pingback submission status was mostly to slow down the adoption of this protocol...

Another side note: maybe in the future I'll write a web-app to receive & store linkback requests,
and "plug" it to this blog.
In the meantime, I have found <https://webmention.io> service very nice & simple to use to add support for Webmention on this blog.
As it is centralized, it is not perfect, but it is a good start to support the adoption of this great linkback protocol !

That's it for today.
Of course, I'd be more than happy to get feedback from you if you use this Pelican plugin 😉
And may the _God of Clean Web Protocols & Semantics_ be with you !

![Ooops! you found a Dead Link](https://chezsoi.org/lucas/wwcb/photos/404-Dead_Link.jpg)


<style>
.uk-article-content > p:nth-child(16) { /* Link to GitHub repo */
  display: block;
  text-align: center;
  border: 1px solid black;
  border-radius: 10rem;
  padding: 1rem;
  margin: 2rem 10vw;
}
.pelican-logo { float: left; max-height: 6rem; margin: 0 1rem; }
</style>
