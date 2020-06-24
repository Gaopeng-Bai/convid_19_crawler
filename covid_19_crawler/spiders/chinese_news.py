#!/usr/bin/python3
# -*-coding:utf-8 -*-

# Reference:**********************************************
# @Time    : 6/15/2020 10:43 PM
# @Author  : Gaopeng.Bai
# @File    : chinese_news.py
# @User    : gaope
# @Software: PyCharm
# @Description: 
# Reference:**********************************************
import scrapy

from selenium import webdriver

from covid_19_crawler.items import Covid19Item


def parse_template(response):
    
    for box in response.xpath('//div[@class="item-box"]'):
        for inner in box.xpath('.//li[@class="inner-item article-mod clearfix"]'):
            a = inner.xpath('.//a[@class="pics"]/@href').extract_first()
            yield scrapy.Request(a, callback=parse_newsPage)


def parse_newsPage(response):
    item = newsItem()

    years = response.xpath('//div[@class="year through"]/span/text()').extract_first()
    mouth_day = ''.join(map(str, response.xpath('//div[@class="md"]/text()').extract()))
    times = ''.join(map(str, response.xpath('//div[@class="time"]/text()').extract()))

    item["date"] = years + " " + mouth_day + " " + times

    item["title"] = response.xpath('//div[@class="LEFT"]/h1/text()').extract_first()

    content = ''
    for items in response.xpath('//p[@class="one-p"]'):
        try:
            text = items.xpath('./text()').extract_first()
        except Exception as e:
            pass
        else:
            if text is not None:
                temp = text.strip().replace('\n', '').replace('\r', '')
                if temp != "":
                    content = content + temp.replace('“', "").replace('”', "") + '\n '

    item["content"] = content[:-3]
    return item


class MySpider(scrapy.Spider):
    name = "ChineseNews"
    allowed_domains = ['qq.com']
    start_urls = [
        "https://new.qq.com/ch/antip/"]

    def __init__(self):
        # create driver when init Alibaba object
        super(MySpider, self).__init__(name='ChineseNews')
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver.exe", chrome_options=option)

    def parse(self, response):

        for box in response.xpath('//li[contains(@class,"item") and contains(@class, "cf")]'):

            a = box.xpath('.//a[@class="picture"]/@href').extract_first()
            if a is not None:
                if "template" in a:
                    yield scrapy.Request(a, callback=parse_template,
                                         errback=self.error_back_http)
                else:
                    yield scrapy.Request(a, callback=parse_newsPage,
                                         errback=self.error_back_http)

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

    cmdline.execute("scrapy crawl ChineseNews".split())
