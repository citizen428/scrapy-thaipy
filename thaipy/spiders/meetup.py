# -*- coding: utf-8 -*-
import scrapy


class MeetupSpider(scrapy.Spider):
    name = 'meetup'
    allowed_domains = ['meetup.com']
    start_urls = ['http://meetup.com/']

    def parse(self, response):
        pass
