#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://chezsoi.org/lucas/blog'
RELATIVE_URLS = False

# Reverting speed optimization settings
TAG_SAVE_AS = 'tag/{slug}.html'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

# This plugin is called manually:
PLUGINS = tuple(p for p in PLUGINS if p != 'image_preview_thumbnailer')
PLUGINS += ('linkbacks', 'pelican.plugins.sitemap', 'tag_cloud')  # 'shaarli_poster' - Disabled for now

DEADLINK_VALIDATION = False
