#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'خالد'
SITENAME = u'مدونة كاليّم'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Asia/Riyadh'
DEFAULT_LANG = u'ar'
STATIC_PATHS = ['uploads']
DEFAULT_CATEGORY = 'misc'
THEME = '/Users/khalidAlnuaim/workspace/theme'
LOCALE = ('en')
DEFAULT_DATE_FORMAT = '%d / %m / %Y'

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


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Theme settings
P_TAGLINE = 'تقنيـــة وعوامـــل أخـــرى'

# if 'rtl' if will import rtl.css to the site.
SITE_DIRECTION = 'rtl'
P_SIDE_TITLE_PAGES = ''
P_SIDE_TITLE_MENUITEM = 'Menu Items'
P_SIDE_TITLE_LINKS = 'روابط'
P_SIDE_TITLE_SOCIAL = ''
P_SIDE_TEXT_RSS = 'خلاصات'
P_SIDE_MSG = ''
P_DISQUS_SITENAME = 'kaluaim'
