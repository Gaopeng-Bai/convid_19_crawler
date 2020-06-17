---
title: Convid-19 data crawler force on regionals and cites in china
---

# Introductions

This script wrote by scrapy to crawl Covid-19 data on individuals cities. Right now only support Chinese cities covid-19 case numbers and news.

[Data Resources](https://ncov.dxy.cn/ncovh5/view/pneumonia)

# Usage

All running conditions of scrapy has been integrated in script. Simply run like normal python script.

* Covid-19 case distributed

    ```
    python China.py
    ```
    Then a .json file will be generated with the data.

* Covid-19 Chinese news

    ```
    python chinese_news.py
    ```