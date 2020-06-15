# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Covid19Item(scrapy.Item):
    # define the fields for your item here like:
    province = scrapy.Field()
    city = scrapy.Field()

    current_case = scrapy.Field()
    accumulated_case = scrapy.Field()

    death = scrapy.Field()
    cured = scrapy.Field()


class newsItem(scrapy.Item):
    date = scrapy.Field()
    title = scrapy.Field()

    content = scrapy.Field()
