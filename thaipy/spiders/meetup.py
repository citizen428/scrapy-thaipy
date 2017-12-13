# -*- coding: utf-8 -*-
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from thaipy.items import MeetupItem


class MeetupSpider(CrawlSpider):
    name = 'meetup'
    allowed_domains = ['meetup.com']
    start_urls = [
        'https://www.meetup.com/ThaiPy-Bangkok-Python-Meetup/events/past']

    rules = [
        Rule(LinkExtractor(allow=('events/\w+/')), callback='parse_meetup')
    ]

    def parse_meetup(self, response):
        loader = ItemLoader(item=MeetupItem(), response=response)
        loader.add_css('title', 'h1.pageHead-headline::text')
        loader.add_css('date', '.eventTimeDisplay-startDate > span::text')
        loader.add_css('date', '.eventTimeDisplay-startDate-time > span::text')
        yield loader.load_item()
