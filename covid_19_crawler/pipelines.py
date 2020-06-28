# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import time
from translator.translator import translator
from azure_table_storage.table_client import azure_table


class Covid19Pipeline:
    def __init__(self):
        self.translator = translator(translator_name="google_separate", to_language="de")
        self.azure_table = azure_table()
        # self.china_data_file = codecs.open("Covid19_china_data.json", "ab")
        # self.china_news_file = codecs.open("Covid19_china_news.json", "ab", encoding="utf-8")

    def process_item(self, item, spider):
        if spider.name == "China":
            temp = {}
            # item['province'] = self.translator.translate_text(text=item['province'])
            # item['city'] = self.translator.translate_text(text=item['city'])
            item['PartitionKey'] = self.translator.translate_text(text=item['PartitionKey'])
            item['RowKey'] = self.translator.translate_text(text=item['RowKey'])
            time.sleep(1)

            temp['PartitionKey'] = item['PartitionKey']
            temp['RowKey'] = item['RowKey']

            try:
                a = self.azure_table.get_entity(item['PartitionKey'], item['RowKey'])
                temp['new_case'] = str(int(item['accumulated_case'].replace(',', ''))-int(a['accumulated_case'].replace(',', '')))
            except Exception as e:
                temp['new_case'] = 'none'
                print(e)

            temp['current_case'] = item['current_case']
            temp['accumulated_case'] = item['accumulated_case']
            temp['death'] = item['death']
            temp['cured'] = item['cured']
            self.azure_table.insert_entity(temp)
            # with codecs.open("Covid19_china_data.json", "ab", encoding="utf-8") as f:
            #     line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            #     f.write(line)
            return item
        elif spider.name == "ChineseNews":

            item['title'] = self.translator.translate_text(text=item['title'])
            item['content'] = self.translator.translate_text(text=item['content'])

            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            self.china_news_file.write(line)
            return item
