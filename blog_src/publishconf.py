#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://inventwithpython.com/blog'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = '%s.atom.xml'

FEED_ALL_RSS = 'rss.xml'
CATEGORY_FEED_RSS = '%s.rss.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = 'inventwithpython'
#GOOGLE_ANALYTICS = 'UA-5459430-3'
