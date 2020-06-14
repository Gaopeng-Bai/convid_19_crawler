#!/usr/bin/python3
# -*-coding:utf-8 -*-

# Reference:**********************************************
# @Time    : 6/14/2020 5:09 PM
# @Author  : Gaopeng.Bai
# @File    : China.py
# @User    : gaope
# @Software: PyCharm
# @Description: 
# Reference:**********************************************
import scrapy
from scrapy.selector import Selector

from selenium import webdriver

from covid_19_crawler.items import Covid19Item


class MySpider(scrapy.Spider):
    name = "China"
    allowed_domains = ['dxy.cn']
    start_urls = [
        "https://ncov.dxy.cn/ncovh5/view/pneumonia"]

    def __init__(self):
        # create driver when init Alibaba object
        super(MySpider, self).__init__(name='China')
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver.exe", chrome_options=option)

    def parse(self, response):

        item = Covid19Item()
        for box in response.xpath('//div[contains(@class,"areaBlock1___3qjL7") or contains(@class, "areaBlock2___2gER7")]'):
            # # debug in scrapy shell
            # from scrapy.shell import inspect_response
            # inspect_response(response, self)
            a = box.xpath('./@class').extract_first()
            if "areaBlock1___3qjL7" == a:
                item["province"] = box.xpath('./p[@class="subBlock1___3cWXy"]/text()').extract_first()
                item["city"] = ''
                item["current_case"] = box.xpath('./p[@class="subBlock2___2BONl"]/text()').extract_first()
                item["accumulated_case"] = box.xpath('./p[@class="subBlock3___3dTLM"]/text()').extract_first()
                item["death"] = box.xpath('./p[@class="subBlock4___3SAto"]/text()').extract_first()
                item["cured"] = box.xpath('./p[@class="subBlock5___33XVW"]/text()').extract_first()
            elif "areaBlock2___2gER7" == a:
                item["province"] = ''
                item["city"] = box.xpath('./p[@class="subBlock1___3cWXy"]/span/text()').extract_first()
                item["current_case"] = box.xpath('./p[@class="subBlock2___2BONl"]/text()').extract_first()
                item["accumulated_case"] = box.xpath('./p[@class="subBlock3___3dTLM"]/text()').extract_first()
                item["death"] = box.xpath('./p[@class="subBlock4___3SAto"]/text()').extract_first()
                item["cured"] = box.xpath('./p[@class="subBlock5___33XVW"]/text()').extract_first()

            yield item

    def error_back_http(self, failure):
        # log all failures
        self.logger.info(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.info('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.info('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.info('TimeoutError on %s', request.url)


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute("scrapy crawl China".split())
