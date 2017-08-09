Title: Python gevent terrible failure mode under Windows
Date: 2017-05-18 14:05
Tags: lang:en, python, gevent, greenlet, windows, failure-mode, terrible
Slug: python-gevent-terrible-failure-mode
---
What do you think of the following innocuous Python code ?
```python
from gevent import monkey
monkey.patch_all(thread=False, select=False)
import requests

requests.get('http://i-do-not-exist.com')
print('THIS WILL NEVER BE PRINTED !!!')
```

Guess what ? The string message will never get printed :(

![](/lucas/blog/content/images/2017/05/96cb6a3bd576058ccc3ca0442099c9f7_silent-memes-image-memes-at-relatablycom-silent-meme_400-400.jpeg)

Simply remove the `monkey.patch_all` line and you'll get a pretty `socket.gaierror: [Errno 8] Name or service not known`.

I tested this with `gevent==1.2.1` and Windows 10, with the `gevent` & `greenlet` packages built from source by `pip install`.