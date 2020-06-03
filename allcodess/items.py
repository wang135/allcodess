# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SmppItem(scrapy.Item):

    # define the fields for your item here like:
    #categories = scrapy.Field()

    time = scrapy.Field()
    opens =  scrapy.Field()

    closes =  scrapy.Field()

    high =  scrapy.Field()

    low = scrapy.Field()

    volume=  scrapy.Field()

    volumemoney =scrapy.Field()

    huanshou = scrapy.Field()
    names = scrapy.Field()
    codes = scrapy.Field()

    # def get_insert_sql(self):
    #     insert_sql = """
    #         insert into codeday4(times, opens, closes, high, low, volume, volumemoney, huanshou, codes, namess)
    #         VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s)
    #     """
    #     params = (self.times, str(self.opens), str(self.closes), str(self.high), str(self.low), str(self.volume), str(self.volumemoney), str(self.huanshou), str(self.codes), str(self.names))

     #   return insert_sql, params
