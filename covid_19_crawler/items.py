# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Covid19Item(scrapy.Item):
    # define the fields for your item here like:
    # province = scrapy.Field()
    # city = scrapy.Field()
    PartitionKey = scrapy.Field()
    RowKey = scrapy.Field()

    current_case = scrapy.Field()
    new_addition_case = scrapy.Field()
    accumulated_case = scrapy.Field()
    cured = scrapy.Field()

    death = scrapy.Field()


class newsItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()

    content = scrapy.Field()
