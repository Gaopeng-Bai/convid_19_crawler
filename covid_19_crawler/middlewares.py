# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time
import random

from scrapy import signals
from scrapy.http import HtmlResponse, Response
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

from covid_19_crawler.settings import user_agent_list
from covid_19_crawler.settings import IPPOOL


class Convid19SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Convid19DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SeleniumCorona19DownloaderMiddleware(object):

    # create driver in the initial method of middleware, worked in one spider.
    # create driver object in each spider when working in multi-spiders.

    def process_request(self, request, spider):
        spider.driver.get(request.url)

        spider.driver.find_element_by_class_name(
            "expandRow___1Y0WD").click()

        origin_code = spider.driver.page_source
        # 将源代码构造成为一个Response对象，并返回。
        res = HtmlResponse(
            url=request.url,
            encoding='utf8',
            body=origin_code,
            request=request)
        # res = Response(url=request.url, body=bytes(origin_code),
        # request=request)
        return res

    def process_response(self, request, response, spider):
        # print(response.url, response.status)
        return response


class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=''):
        super().__init__(user_agent)
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(user_agent_list)
        if ua:
            # print("current user agent:" + ua)
            request.headers.setdefault('User-Agent', ua)


class IPpools(HttpProxyMiddleware):
    def __init__(self, ip=''):
        super().__init__()
        self.ip = ip

    def process_request(self, request, spider):
        this_ip = random.choice(IPpools)
        request.meta["proxy"] = "http://" + this_ip