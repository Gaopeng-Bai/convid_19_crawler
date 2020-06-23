#!/usr/bin/python3
# -*-coding:utf-8 -*-

# Reference:**********************************************
# @Time    : 6/18/2020 3:25 PM
# @Author  : Gaopeng.Bai
# @File    : translator.py
# @User    : gaope
# @Software: PyCharm
# @Description: 
# Reference:**********************************************
import translators as ts

from termcolor import colored
from bs4 import BeautifulSoup

import requests


class translator:
    def __init__(self, translator_name="google", to_language="en"):
        self.translator = translator_name
        if translator_name == "microsoft":
            # Specify the subscription Key

            subscriptionKey = "3bad207c87df4b1984b932905cb80f31"

            # Specify URLs for Cognitive Services - Translator Text API

            self.translateUrl = 'https://api.microsofttranslator.com/v2/http.svc/Translate'

            cognitiveServiceUrl = 'https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issueToken'
            requestHeader = {'Ocp-Apim-Subscription-Key': subscriptionKey}

            responseResult = requests.post(cognitiveServiceUrl, headers=requestHeader)

            self.token = responseResult.text

            # self.microsoft = Translator("8305750734ea4ea8b89d02ac542a1b48")

        self.to_language = to_language

    def translate_text(self, text):
        if self.translator == "google":
            return ts.google(text, to_language=self.to_language)
        elif self.translator == "bing":
            return ts.bing(text, to_language=self.to_language)
        elif self.translator == "microsoft":
            params = {'appid': 'Bearer ' + self.token, 'text': text, 'to': self.to_language}

            requestHeader = {'Accept': 'application/xml'}

            responseResult = requests.get(self.translateUrl, params=params, headers=requestHeader)

            soup = BeautifulSoup(responseResult.text, "lxml")

            return colored(soup.get_text())

        elif self.translator == "sogou":
            return ts.sogou(text, to_language=self.to_language)
        elif self.translator == "baidu":
            return ts.baidu(text, to_language=self.to_language)
        elif self.translator == "alibaba":
            return ts.alibaba(text, to_language=self.to_language)
        elif self.translator == "tencent":
            return ts.tencent(text, to_language=self.to_language)
        elif self.translator == "youdao":
            return ts.youdao(text, to_language=self.to_language)
        elif self.translator == "deepl":
            return ts.deepl(text, to_language=self.to_language)


if __name__ == '__main__':
    t = translator(translator_name="microsoft")

    print("result: "+t.translate_text(text="我是谁"))