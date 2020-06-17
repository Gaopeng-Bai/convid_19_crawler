---
title: Convid-19 data crawler in china
---

# Introductions

This script wrote by Scrapy to crawl Covid-19 data. Right now support Chinese cities Covid-19 case numbers and relevent Covid-19 news in china.

[Data Resources (Case numbers)](https://ncov.dxy.cn/ncovh5/view/pneumonia)

[Data Resources (Covid-19 news)](https://new.qq.com/ch/antip/)

# Usage

All running conditions of Scrapy has been integrated in script. Simply run like normal python script.

* Covid-19 case distributed

    ```
    python China.py
    ```
    Then a .json file will be generated with the data.

* Covid-19 Chinese news

    ```
    python chinese_news.py
    ```