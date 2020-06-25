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
import datetime
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
        option.add_argument('--headless')
        # option.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver.exe", options=option)

    def parse(self, response):

        item = Covid19Item()
        province = ''
        for box in response.xpath('//div[contains(@class,"areaBlock1___3qjL7") or contains(@class, "areaBlock2___2gER7")]'):
            # # debug in scrapy shell
            # from scrapy.shell import inspect_response
            # inspect_response(response, self)
            a = box.xpath('./@class').extract_first()
            item['RowKey'] = str(datetime.date.today())
            if "areaBlock1___3qjL7" == a:
                province = box.xpath('./p[@class="subBlock1___3cWXy"]/text()').extract_first()
                if province.find('(') != -1:
                    break
                else:
                    item["PartitionKey"] = province
                    # item["province"] = province

                # item["city"] = ''
                item["current_case"] = box.xpath('./p[@class="subBlock2___2BONl"]/text()').extract_first().replace("-", "0")
                item["accumulated_case"] = box.xpath('./p[@class="subBlock3___3dTLM"]/text()').extract_first().replace("-", "0")
                item["death"] = box.xpath('./p[@class="subBlock4___3SAto"]/text()').extract_first().replace("-", "0")
                item["cured"] = box.xpath('./p[@class="subBlock5___33XVW"]/text()').extract_first().replace("-", "0")
            elif "areaBlock2___2gER7" == a:
                # item["province"] = province
                city = box.xpath('./p[@class="subBlock1___3cWXy"]/span/text()').extract_first()
                if city is None:
                    continue
                else:
                    # item["city"] = city
                    item["PartitionKey"] = city
                item["current_case"] = box.xpath('./p[@class="subBlock2___2BONl"]/text()').extract_first().replace("-", "0")
                item["accumulated_case"] = box.xpath('./p[@class="subBlock3___3dTLM"]/text()').extract_first().replace("-", "0")
                item["death"] = box.xpath('./p[@class="subBlock4___3SAto"]/text()').extract_first().replace("-", "0")
                item["cured"] = box.xpath('./p[@class="subBlock5___33XVW"]/text()').extract_first().replace("-", "0")

            yield item


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute("scrapy crawl China".split())
