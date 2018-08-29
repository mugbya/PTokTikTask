# -*- coding: utf-8 -*-
from scrapy import cmdline
from crawler.settings import SPIDER_NAME

name = SPIDER_NAME
cmd = 'scrapy crawl {0}'.format(name)
# cmd = 'scrapy crawl {0} -o {1}.json'.format(name, name)
cmdline.execute(cmd.split())

