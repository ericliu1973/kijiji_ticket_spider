# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KjjspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    description= scrapy.Field()
    postdate= scrapy.Field()
    ticket_avail = scrapy.Field()
    ticket_info = scrapy.Field()
    url = scrapy.Field()

