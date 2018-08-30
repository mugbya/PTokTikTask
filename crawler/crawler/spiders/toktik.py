# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from crawler.settings import SPIDER_NAME,  LOGGER_NAME
from crawler.common import redis_client, download
import logging

logger = logging.getLogger(LOGGER_NAME)

# sys.argv = ['you-get',
#             'https://api.tiktokv.com/aweme/v1/playwm/?video_id=v090446c0000bdl7jffsmmqslle94s9g&amp;line=0']


class TiktokSpider(RedisSpider):
    name = SPIDER_NAME
    allowed_domains = ['tiktokv.com']

    def parse(self, response):
        # 爬虫接接收到的地址
        redirect_url = response.request.meta['redirect_urls'][0]
        logger.info('爬虫接接收到的地址: ' + redirect_url)

        #  response.url 是被重定向后的地
        mp4_sign = response.url.split('/')[-2]
        logger.info('爬虫解析视频的标识:  ' + mp4_sign)
        download(response.url)

        redis_client.hset('mint', redirect_url, mp4_sign)






