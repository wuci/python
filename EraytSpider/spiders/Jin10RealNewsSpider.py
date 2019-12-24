import datetime
import scrapy
import requests
import json

from EraytSpider.items.RealNewsItem import RealNewsItem


class Jin10RealNewsSpider(scrapy.Spider):
    name = 'Jin10RealNewsSpider'
    allowed_domains = ['jin10.com']
    start_urls = ['http://jin10.com/']

    def parse(self, response):
        item = RealNewsItem()
        reqData = requests.get("https://www.jin10.com/flash_newest.js")
        requestData = reqData.content.decode().split("= ", 1)[1].strip(";")
        dataList = json.loads(requestData)
        if len(dataList):
            for eachData in dataList:
                if "content" in eachData['data']:
                    if "金十" not in eachData['data']['content'] and ("jin10" not in eachData['data']['content']):
                        item['title'] = eachData['data']['content']
                        item['_id'] = eachData['id']
                        utcTime = datetime.datetime.strptime(eachData['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
                        localtime = utcTime + datetime.timedelta(hours=8)
                        item['date'] = str(localtime)[0:10]
                        item['time'] = str(localtime)[11:]
                        item['important'] = eachData['important']
                    yield item
