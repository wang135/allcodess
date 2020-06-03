
import tushare as ts
import threading
import time
import multiprocessing
from multiprocessing import Process,Pool
import requests
from bs4 import BeautifulSoup
import  scrapy

from allcodess.items import SmppItem
#from dayhq.items import MysqlTwistedPipline
import tushare as ts
import json
import re
import datetime
from scrapy.spiders import CrawlSpider, Rule
import redis
import copy

class DmozSpider(scrapy.Spider):
    name = "riday"
    allowed_domains = ["pdfm.eastmoney.com"]
    redis_key = 'ridayss:start_urls'
    print('111111111111111111111111')
    start_urls = []
    codess = list(ts.get_stock_basics().index)[0:10]
    for code in codess:
        if code[0] == '6':
            print(code)
            start_urls.append(
                           'http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&token=4f1862fc3b5e77c150a2b985b12db0fd&cb='  \
                                     'jQuery1830877243188420505_1555667605057&id='+code+'1&type=k&authorityType=&_=1555667607552')
        else:
            start_urls.append(
                   'http://pdfm.eastmoney.com/EM_UBG_PDTI_Fast/api/js?rtntype=5&token=4f1862fc3b5e77c150a2b985b12db0fd&cb='  \
                                     'jQuery1830877243188420505_1555667605057&id='+code+'2&type=k&authorityType=&_=1555667607552')


    def parse(self, response):
        print('222222222222222')
        infos = copy.copy(response.text)
        # print(infos)

        p1 = re.compile(r'[(](.*?)[)]', re.S)
        list_all = re.findall(p1, infos)
        # info = eval(list_all[0])
        info = json.loads(list_all[0])
        names = info['name']
        print(names)
        codes = info['code']
        dates = info['data']
        # item = DmozItem()
        list_times = []
        for date in dates:
            item = SmppItem()
            dts = date.split(',')
            times = dts[0]
            timess = datetime.datetime.strptime(times, '%Y-%m-%d')
            item['time'] = timess
            list_times.append(times)
            item['opens'] = dts[1]

            item['closes'] = dts[2]

            item['high'] = dts[3]

            item['low'] = dts[4]

            item['volume'] = dts[5]

            item['volumemoney'] = dts[6]

            item['huanshou'] = dts[7]
            item['names'] = names
            item['codes'] = codes
            print('wwwwwwwwwwwwwwwwwww', item['codes'], item['names'])

            yield item