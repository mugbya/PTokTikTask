# -*- coding: utf-8 -*-
from scrapy import cmdline
# from product_crawler.settings import SPIDER_NAME

name = 'toktik'
cmd = 'scrapy crawl {0}'.format(name)
# cmd = 'scrapy crawl {0} -o {1}.json'.format(name, name)
cmdline.execute(cmd.split())

