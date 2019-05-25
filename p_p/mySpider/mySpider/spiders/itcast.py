# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        with open('teacher.html','w') as f:
            f.write(response.text)


