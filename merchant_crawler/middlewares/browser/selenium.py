
# -*- coding: utf-8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.keys import Keys
import logging
import time


class SeleniumMiddleware():
    def __init__(self):
        self.logger = logging.getLogger()
        self.driver = webdriver.Chrome()

    def process_request(self, request, spider):
        #两种log打印方式
        spider.logger.info('Spider opened321312312312: %s' % spider.name)
        self.logger.warning("This is a warning 321")
        #打开浏览器
        self.driver.get(request.url)
        #选择对应元素
        element = self.driver.find_element_by_xpath("//*[@id='kw']")
        #输入查询目标
        element.send_keys("12309")
        time.sleep(2)
        #模拟回车
        element.send_keys(Keys.RETURN)
        time.sleep(3)
        #返回response对象
        return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8', status=200)

    def process_response(self, request, response, spider):
        #打印当前页面源码
        with open('response', 'w') as f:
            f.write(f'{self.driver.page_source}')
        #关闭浏览器
        self.driver.close()
        return response

    def process_exception(self, request, exception, spider):
        return request
