# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IccItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    h1 = scrapy.Field()
    bio = scrapy.Field()
    image = scrapy.Field()
    og_locale = scrapy.Field()
    og_type = scrapy.Field()
    og_title = scrapy.Field()
    og_description = scrapy.Field()
    og_url = scrapy.Field()
    og_site_name = scrapy.Field()
    og_image = scrapy.Field()
    twitter_card = scrapy.Field()
    twitter_description = scrapy.Field()
    twitter_title = scrapy.Field()
    twitter_site = scrapy.Field()
    twitter_domain = scrapy.Field()
    twitter_image  = scrapy.Field()
    twitter_creator = scrapy.Field()