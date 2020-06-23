# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from googletrans import Translator
from translator.translator import translator


class Covid19Pipeline:
    def __init__(self):
        self.translator = translator(translator_name="microsoft", to_language="de")
        self.china_data_file = codecs.open("../../Covid19_china_data.json", "ab", encoding="utf-8")
        self.china_news_file = codecs.open("../../Covid19_china_news.json", "ab", encoding="utf-8")

    def process_item(self, item, spider):
        if spider.name == "China":
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.china_data_file.write(line)
            return item
        elif spider.name == "ChineseNews":

            item['title'] = self.translator.translate_text(text=item['title'])
            item['content'] = self.translator.translate_text(text=item['content'])

            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.china_news_file.write(line)
            return item
