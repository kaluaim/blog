#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

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
DEFAULT_PAGINATION = 5

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('تويتر', '#', 'fa fa-twitter'),
          ('لينكدان', '#', 'fa fa-linkedin'),)


#   _____               _ _
#  / ____|             | (_)
# | (___   __ _ _ __ __| |_ _ __   ___
#  \___ \ / _` | '__/ _` | | '_ \ / _ \
#  ____) | (_| | | | (_| | | | | |  __/
# |_____/ \__,_|_|  \__,_|_|_| |_|\___| configurations

# Sardine configurations
# if 'rtl' if will import rtl.css to the site.
SRDN_SITE_DIRECTION = 'rtl'
SRDN_SITE_LOGO = 'kaluaim.png'
SRDN_TAGLINE = 'تقنيـــة وعوامـــل أخـــرى'
SRDN_SIDE_TITLE_PAGES = ''
SRDN_SIDE_TITLE_MENUITEM = ''
SRDN_SIDE_TITLE_LINKS = ''
SRDN_SIDE_TITLE_SOCIAL = ''
SRDN_SIDE_MSG = ''
SRDN_RSS_TITLE = 'الإشتراك عبر الخلاصات'
SRDN_EMAIL_TITLE = 'الإشتراك عبر البريد الإلكتروني'
SRDN_CATEGORY_TEXT = 'تصنيف:'
SRDN_DISQUS_SITENAME = 'kaluaim'

# HTML footer lines, after each line <br/> will be added.
SRDN_FOOTER_LINES = (('<span>جميع الحقوق <a href="http://www.gnu.org/licenses/copyleft.ar.html" target="_blank">متروكة</a></span>'),
                     ('<span>بحب استخدم <a href="http://blog.getpelican.com/">بيلكن</a> و <a href="https://github.com/kaluaim/sardine">سردين</a></span>'),)
