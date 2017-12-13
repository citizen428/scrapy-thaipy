# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from thaipy.items import MeetupItem


class MeetupSpider(scrapy.Spider):
    name = 'meetup'
    allowed_domains = ['meetup.com']
    start_urls = [
        'https://www.meetup.com/ThaiPy-Bangkok-Python-Meetup/events/past']

    def parse(self, response):
        for event in response.css('li.list-item'):
            loader = ItemLoader(item=MeetupItem(), selector=event)
            loader.add_css('title', 'h2.eventCardHead--title::text')
            loader.add_css('date', '.eventTimeDisplay-startDate > span::text')
            yield loader.load_item()
