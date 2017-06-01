#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jimmy Jiang'
SITENAME = "Jimmy Jiang's Blog"
SITEURL = 'http://localhost:8000'
SITESUBTITLE = 'Software Engineer'
# SITELOGO = '//s.gravatar.com/avatar/9544bbb3a7e40cbcade687ded264c5ea?s=80'
SITELOGO = '/extra/sitelogo.ico'
ITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
PYGMENTS_STYLE = 'monokai'

FAVICON = '/extra/favicon.ico'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = ()

# Social widget
SOCIAL = ( ('github', 'https://github.com/jglwiz'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

# THEME
THEME = 'Flex'
LOAD_CONTENT_CACHE = False

# comment 
DISQUS_SITENAME = 'jglwiz-blog'

# static paths
STATIC_PATHS = ['images', 'extra']
