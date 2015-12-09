#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'khalid'
SITENAME = u'Khalid Alnuaim blog'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Asia/Riyadh'
DEFAULT_LANG = u'ar'
STATIC_PATHS = ['uploads']
DEFAULT_CATEGORY = 'misc'
THEME = '/Users/khalidAlnuaim/workspace/theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('linktesting', '#'),)


# Social widget
SOCIAL = (('twiiter', '#'),
          ('linkedin', '#'),)


DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Theme settings
TAGLINE = 'Software engineer devoted to Automation. Work @Red Hat.'

# if 'rtl' if will import rtl.css to the site.
SITE_DIRECTION = 'rtl'
FS_SIDE_TITLE_PAGES = 'Pages'
FS_SIDE_TITLE_MENUITEM = 'Menu Items'
FS_SIDE_TITLE_LINKS = 'Links'
FS_SIDE_TITLE_SOCIAL = 'Social'
