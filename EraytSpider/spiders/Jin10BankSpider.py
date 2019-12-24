# -*- coding: utf-8 -*-

import scrapy
import requests
import json
import datetime
from EraytSpider.items.BankItem import BankspiderItem

# Author :  Li Yipin
# Date   :  2019/06/17
# Description : 金十投行订单数据抓取模块

class Jin10BankSpider(scrapy.Spider):
    name = 'Jin10BankSpider'
    allowed_domains = ['jin10.com']
    start_urls = ['http://jin10.com/']

    def parse(self, response):
        date = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime("%Y%m%d")
        item = BankspiderItem()
        url = 'https://datacenter.jin10.com/get_dc_second_data?type=dc_efx_news&jsonpCallback=jQuery111105106126254799792_1559535093655&_=1559535093656'
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        r = r.text
        r = r.replace('/**/jQuery111105106126254799792_1559535093655(', '').replace(');', '')
        data = str(json.loads(r)['data']).replace("[", "").replace("{", "").replace("'", "").replace("]", "").replace("}", "")
        dataList = data.split("]},")

        dict = {}
        if len(dataList) and '' is not dataList[0]:
            for dataStr in dataList:
                data1 = dataStr.replace(" ", "").split(",rationale")[0]
                dict1 = {}
                list = data1.split(",")
                for res in list:
                    result = res.split(":")
                    key = result[0]
                    val = result[1]
                    dict1[key] = val
                dict[dict1.get("bank_name") + dict1.get("currency")] = dict1

            for key, val in dict.items():
                item['_id'] = dict.get(key).get("bank_name") + "_" + dict.get(key).get("currency")
                item['bank_name'] = dict.get(key).get("bank_name")
                item['currency'] = dict.get(key).get("currency")
                item['currency_code'] = dict.get(key).get("currency_code")[0:3] + "/" \
                                        + dict.get(key).get("currency_code")[3:6]
                item['order_type'] = dict.get(key).get("order_type")
                item['order_data'] = dict.get(key).get("order_data")
                item['target_data'] = dict.get(key).get("target_data")
                item['stop'] = dict.get(key).get("stop")
                item['type'] = dict.get(key).get("types")
                item['order_term'] = dict.get(key).get("order_term")
                item['date'] = date
                yield item
