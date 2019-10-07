# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodreadquotesItem(scrapy.Item):
    # define the fields for your item here like:
    source = scrapy.Field()
    title = scrapy.Field()
    length = scrapy.Field()
    author = scrapy.Field()
    likes = scrapy.Field()
    tags = scrapy.Field()
    
