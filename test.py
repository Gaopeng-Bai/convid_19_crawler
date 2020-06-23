#!/usr/bin/python3
# -*-coding:utf-8 -*-

# Reference:**********************************************
# @Time    : 6/23/2020 7:20 PM
# @Author  : Gaopeng.Bai
# @File    : test.py
# @User    : gaope
# @Software: PyCharm
# @Description: 
# Reference:**********************************************
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument("--no-sandbox")
option.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=option)