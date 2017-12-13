# -*- coding: utf-8 -*-
import scrapy
from thaipy.items import MeetupItem


class MeetupSpider(scrapy.Spider):
    name = 'meetup'
    allowed_domains = ['meetup.com']
    start_urls = [
        'https://www.meetup.com/ThaiPy-Bangkok-Python-Meetup/events/past']

    def parse(self, response):
        for event in response.css('li.list-item'):
            yield MeetupItem(
                title=event.css(
                    'h2.eventCardHead--title::text').extract_first(),
                date=event.css(
                    '.eventTimeDisplay-startDate > span::text').extract()
            )
