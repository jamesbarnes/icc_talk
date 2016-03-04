# -*- coding: utf-8 -*-

# Scrapy settings for icc project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'icc'

SPIDER_MODULES = ['icc.spiders']
NEWSPIDER_MODULE = 'icc.spiders'

#save output to csv 
FEED_FORMAT="csv"
FEED_URI="file:output.csv"