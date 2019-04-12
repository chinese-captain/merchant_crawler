# -*- coding: utf-8 -*-
import scrapy
import logging

class FullOrder(scrapy.Spider):
    name = "fullOrder"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://www.baidu.com/"]

    def parse(self, response):
        pass