# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from settings import SPIDER_NAME


class TiktokSpider(RedisSpider):
    name = SPIDER_NAME
    allowed_domains = ['tiktokv.com']

    def parse(self, response):

        print(response.url)


