import os, sys
for f in os.listdir(sys.argv[1]):
    print('<div class="lazyload" data-noscript=""><noscript><img src="images/{}"></noscript></div>\n'.format(f))
