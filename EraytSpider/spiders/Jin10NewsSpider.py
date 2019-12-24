# -*- coding: utf-8 -*-

import scrapy
import requests
import json
from EraytSpider.items.NewsItem import NewsspiderItem

# Author :  Li Yipin
# Date   :  2019/06/17
# Description : 金十资讯数据抓取模块 (抓取当日数据)

class Jin10NewsSpider(scrapy.Spider):
    name = 'Jin10NewsSpider'
    allowed_domains = ['jin10.com']
    start_urls = ['http://jin10.com/']

    def parse(self, response):

        item = NewsspiderItem()
        reqData = requests.get("https://www.jin10.com/flash_newest.js")
        requestData = reqData.content.decode().split("= ", 1)[1].strip(";")
        dataList = json.loads(requestData)
        if len(dataList):
            for eachData in dataList:
                if 'content' in eachData['data']:
                    item['title'] = eachData['data']['content']
                    item['_id'] = eachData['id']
                    item['date'] = eachData['time'][0:10]
                    item['time'] = eachData['time'][11:19]
                    yield item


























