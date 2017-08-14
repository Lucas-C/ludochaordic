Title: Setting-up Etherpad in a server subdirectory -aka- Apache config hell
Date: 2014-10-09 22:10
Tags: lang:en, etherpad, journal, diary, logbook, apache, config, sed, xargs, relative, url, proxy, html, prog
Slug: setting-up-etherpad-in-a-server-subdirectory-aka-apache-config-hell
---
![](images/2014/Oct/Cloudberry-Kingdom-difficulty_reduced_x3.gif)

I truly think [Etherpad](//github.com/ether/etherpad-lite) is an amazing piece of software. Not so much for its code base quality than for its extraordinary range of usages.

Now, while I'm still unsure if todo-lists are useful [or a complete waste of energy](//blog.codinghorror.com/todont/), I'm convinced that keeping a developer logbook / diary / journal has [many](http://coliveira.net/software/day-3-keep-a-programming-diary/) [benefits](//programmers.stackexchange.com/a/3499) (even [The Pragmatic Programmer](http://en.wikipedia.org/wiki/The_Pragmatic_Programmer) and [Redis creator](http://antirez.com/news/51) recommend it).

Then, don't get me wrong: paper notebooks are [GREAT](https://gist.github.com/sent-hil/3444793). I love them, and always carry one with me. But for the sake of durability, safety and hypertextuality, I often end up transfering most of my hand-written notes on my computer. And Etherpad is just the perfect tool for this. Why ?

- its interface is slick, easy to grasp quickly, almost simplistic at first but with a bit of [progressive disclosure](//en.wikipedia.org/wiki/Progressive_disclosure)
- it provides the flexibility to add, remove or rearrange ideas way more easily than on paper
- it allows quick copy & paste of URLs, code snippets, quotes, input text for a temporary backup copy... like some kind of cross-applications scratchpad/buffer
- it has various font sizes, styles and colors : it is well-known in [mind-mapping](en.wikipedia.org/wiki/Mind_map) that this will help make your notes more stimulating, engaging & easy to remember
- it allows simultaneous multi-users access
- it has plenty of plugins : [images preview](//github.com/JohnMcLear/ep_previewimages), [list of pads](//github.com/spruce/ep_small_list), [syntax highlighting](//github.com/etinquis/etherpad-plugins/tree/master/ep_syntaxhighlighting)...
- and above all: **it provides a persistent history of changes**

Hence my will to install a local instance on my server.

It all started off on the right foot: installing Etherpad on my Ubuntu laptop revealed to be [easy as a pie](//github.com/ether/etherpad-lite/blob/master/README.md#gnulinux-and-other-unix-like-systems).

But things became nasty when I had to serve it through Apache. The [wiki guidelines](//github.com/ether/etherpad-lite/wiki/How-to-put-Etherpad-Lite-behind-a-reverse-Proxy) did not work for me.

After hours of googling (more precisely [duckduckgoing](//duckduckgo.com)) and a stupid attempt to add an additional helpful entry to the Etherpad config (I was about to send a pull request on github when I realized how useless it was), I found the [wisdom of the ancients](//xkcd.com/979/) on good old [StackOverflow](//stackoverflow.com/a/13385407).

First, assuming you have an Etherpad node.js process ready & listening on port 9001, you'll have to configure Apache to use mod\_proxy\_html:

    sudo apt-get install libapache2-mod-proxy-html libxml2-dev
    sudo a2enmod proxy_html xml2enc

Then, there is the magic config:

    <Location /pad>
      ProxyPass http://localhost:9001 retry=0
      # retry=0 => avoid 503's when restarting etherpad-lite
      ProxyPassReverse http://localhost:9001
      SetOutputFilter proxy-html
      ProxyHTMLURLMap http://localhost:9001
    </Location>
    RewriteRule ^/pad$ /pad/ [R]

Now simply restart Apache, and Bob's your uncle !

    sudo service apache2 restart
    sudo tail -F /var/log/apache2/*.log # watch that everything is OK

![](images/2014/Oct/PowerRanger_stunt_GotYou.gif)

<br/><br/><br/><br/><br/><br/><br/>

Still here ? Ok, there is a last tip, in case you use either ep\_small_list or ep\_syntaxhighlighting plugins, to convert their bogus absolute URLs into relative ones:

    grep -FIlR '"/static/' path/to/etherpad-lite/node_modules/ep_{small_list,syntaxhighlighting} | xargs sed -i 's~"/static/~"../static/~'
