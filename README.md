---
Title: Convid-19 data crawler in china
---

# Introductions

This script written by Scrapy to crawl Covid-19 data, running on azure cloud virtual machine and also upload data into azure storage table. Right now support Chinese cities Covid-19 case numbers and relevant Covid-19 news in china. 

[Data Resources (Case numbers)](https://ncov.dxy.cn/ncovh5/view/pneumonia)

[Data Resources (Covid-19 news)](https://new.qq.com/ch/antip/)

# Usage

All running conditions of Scrapy has been integrated in script. Simply run like normal python script.


This section only can run on linux vm. Change the code block make this to run on local windows OS.
Hint: On local machine must consist chromedriver in correct path or custom path.

```
# self.driver = webdriver.Chrome(executable_path="D:\chromedriver.exe", options=option)
self.driver = webdriver.Chrome(options=option)

```
* Covid-19 case distributed

    ```
    python China.py
    ```
 
* Covid-19 Chinese news

    ```
    python chinese_news.py
    ```
* run this on linux:

    ```
    scrapy crawl <spider name>
    ```