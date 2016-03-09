#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'خالد'
SITENAME = u'مدونة كاليّم'
SITEURL = 'http://kalua.im/blog/'
PATH = 'content'
TIMEZONE = 'Asia/Riyadh'
DEFAULT_LANG = u'ar'
STATIC_PATHS = ['uploads']
DEFAULT_CATEGORY = 'misc'
THEME = '/Users/khalidAlnuaim/workspace/sardine/theme'
LOCALE = ('ar')
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
RELATIVE_URLS = True




# Sardine configurations
# if 'rtl' if will import rtl.css to the site.
SRDN_SITE_DIRECTION = 'rtl'
SRDN_TAGLINE = 'تقنيـــة وعوامـــل أخـــرى'
SRDN_SIDE_TITLE_PAGES = ''
SRDN_SIDE_TITLE_MENUITEM = ''
SRDN_SIDE_TITLE_LINKS = ''
SRDN_SIDE_TITLE_SOCIAL = ''
SRDN_SIDE_MSG = ''
SRDN_FOOTER_CR_YEAR = '2016'
