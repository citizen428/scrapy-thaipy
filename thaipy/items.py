# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, Join


class MeetupItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=Join(" @ "))
    parsed_at = scrapy.Field()
