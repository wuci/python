# -*- coding: utf-8 -*-

import requests
import scrapy
import pymongo
import datetime

from EraytSpider import settings
from EraytSpider.items.CalendarDetailsItem import CalendarDetailsItem


# Author :  Li Yipin
# Date   :  2019/06/17
# Description : 金十财经日历详情数据抓取  timelist 设置爬取的日期 0 代表当日 (生产可设计成每周日爬取下两周的数据)

class Jin10CalendarDetailsSpider(scrapy.Spider):
    name = 'Jin10CalendarDetailsSpider'
    allowed_domains = ['jin10.com']
    start_urls = ['http://jin10.com/']

    def parse(self, response):
        # myclient = pymongo.MongoClient('mongodb://192.168.193.108:27017/')
        myclient = pymongo.MongoClient(host=settings.MONGODB_HOST, port=settings.MONGODB_PORT)
        mydb = myclient["Finance"]
        mycol = mydb["FinanceCalendar"]
        item = CalendarDetailsItem()
        for dayNum in list(range(0, 30)):
            date = (datetime.datetime.now() + datetime.timedelta(days=dayNum)).strftime("%Y%m%d")
            myquery = {"date": date}
            mydoc = mycol.find(myquery)
            list_id = []
            for x in mydoc:
                list_id.append(x.get("_id"))

            for a in list_id:
                url = "https://cdn-rili.jin10.com/data/jiedu/" + str(a) + ".json"
                resultData = requests.get(url)
                if len(resultData.text):
                    if "<Error>" in resultData.text:
                        continue
                    else:
                        result = resultData.json()
                        item['_id'] = a
                        item['relationId'] = a
                        item['nextTime'] = result.get("public_time")
                        item['reportFrequency'] = result.get("frequency")
                        item['statisticalMethod'] = result.get("method")
                        item['dataInfluence'] = result.get("impact")
                        item['dataInterpretation'] = result.get("paraphrase")
                        item['interestRead'] = result.get("concern")
                        item['publishAgencies'] = result.get("institutions")
                        yield item

