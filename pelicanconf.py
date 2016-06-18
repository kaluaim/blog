#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

AUTHOR = u'خالد'
SITENAME = u'مدونّة كاليم'
SITEURL = 'http://kalua.im/blog'
PATH = 'content'
TIMEZONE = 'Asia/Riyadh'
DEFAULT_LANG = u'ar'
STATIC_PATHS = ['uploads',
                'extra/robots.txt',
                'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
DEFAULT_CATEGORY = 'misc'
THEME = '/Users/khalidAlnuaim/workspace/sardine/theme'
LOCALE = ('ar')
DEFAULT_DATE_FORMAT = '%d / %m / %Y'
DEFAULT_PAGINATION = 5
PAGE_ORDER_BY = 'order'

PLUGINS = [
    'pelican_youtube',
]

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/atom.xml'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('تويتر', 'https://twitter.com/kaluaim/', 'fa fa-twitter', '_blank'),
          ('لينكدان', 'https://www.linkedin.com/in/khalidalnuaim/', 'fa fa-linkedin', '_blank'),
          ('قيت هب', 'https://github.com/kaluaim/', 'fa fa-github', '_blank'),
          ('انستقرام', 'https://instagram.com/kaluaim/', 'fa fa-instagram', '_blank'),
          ('المزيد...', 'http://kalua.im/blog/pages/social.html', 'fa fa-angle-double-left', '_self'),)


#   _____               _ _
#  / ____|             | (_)
# | (___   __ _ _ __ __| |_ _ __   ___
#  \___ \ / _` | '__/ _` | | '_ \ / _ \
#  ____) | (_| | | | (_| | | | | |  __/
# |_____/ \__,_|_|  \__,_|_|_| |_|\___| Configurations

# If any of the fields are empty it will not be rendared.
# if 'rtl' then will import rtl.css to the site.
SRDN_SITE_DIRECTION = 'rtl'
SRDN_SITE_LOGO = 'kaluaim.png'
SRDN_TAGLINE = 'تقنيـــة وعوامـــل أخـــرى'
SRDN_SIDE_TITLE_PAGES = 'صفحات'
SRDN_SIDE_TITLE_MENUITEM = ''
SRDN_SIDE_TITLE_LINKS = ''
SRDN_SIDE_TITLE_SOCIAL = 'روابط'
SRDN_SIDE_MSG = ''
SRDN_GOOGLE_ANALYTICS = 'UA-43312127-5'

# RSS Feed. for example use feedburnr
SRDN_RSS_TITLE = 'الإشتراك عبر الخلاصات'
SRDN_RSS_URL = 'http://feeds.feedburner.com/kaluaim'

# Email Feed
SRDN_EMAIL_TITLE = 'الإشتراك عبر البريد الإلكتروني'
SRDN_EMAIL_URL = 'https://feedburner.google.com/fb/a/mailverify?uri=kaluaim&amp;loc=en_US'

SRDN_CATEGORY_TEXT = 'تصنيف:'
SRDN_TAG_TEXT = 'وسوم:'
SRDN_DISQUS_SITENAME = 'kaluaim'

# HTML footer lines, after each line <br/> will be added.
SRDN_FOOTER_LINES = (('<span>جميع الحقوق <a href="http://www.gnu.org/licenses/copyleft.ar.html" target="_blank">متروكة</a></span>'),
                     ('<span>بحب استخدم <a href="http://blog.getpelican.com/" target="_blank">بيليكن</a> و <a href="https://github.com/kaluaim/sardine" target="_blank">سردين</a></span>'),
                     ('<span>مستضاف على <a href="https://pages.github.com/" target="_blank">صفحات قيت هب</a></span>'),)
