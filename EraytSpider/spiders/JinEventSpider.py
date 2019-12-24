# -*- coding: utf-8 -*-

import requests
import scrapy
import datetime
from EraytSpider.items.EventItem import EventspiderItem


# Author :  Li Yipin
# Date   :  2019/06/17
# Description : 金十事件数据抓取模块  timelist 设置爬取的日期 0 代表当日

class JinEventSpider(scrapy.Spider):
    name = 'JinEventSpider'
    allowed_domains = ['jin10.com']
    start_urls = ['http://jin10.com/']

    def parse(self, response):

        # 事件抓取日期设置 (当日)
        timelist = [0]
        item = EventspiderItem()
        for timelist1 in timelist:
            date = (datetime.datetime.now() + datetime.timedelta(days=timelist1)).strftime("%Y%m%d")
            year = str(date)[0:4]
            time = str(date)[4:8]
            #day = str(datetime.datetime(int(year), int(str(date)[5:6]), int(str(date)[6:8])).strftime("%w"))
            url = "https://cdn-rili.jin10.com/data/" + year + "/" + time + "/event.json"
            response = requests.get(url)
            jsoninfo = response.json()
            #if day is not "0" and len(str(jsoninfo)) > 10:
            for result in jsoninfo:
                # 拿到 event_time 字段的值并解析出真正时间(UTC)
                resultTime = result.get('event_time')
                realTime = datetime.datetime.strptime(str(resultTime).replace("T", " ")[0:16], "%Y-%m-%d %H:%M") \
                           + datetime.timedelta(hours=8)
                time_split = str(realTime).split(" ")
                item['_id'] = result.get("id")
                item['date'] = time_split[0].replace("-", "")
                realTime = str(time_split[1].split(":")[0] + ":" + time_split[1].split(":")[1])
                if realTime == "00:00":
                    item['time'] = "待定"
                else:
                    item['time'] = time_split[1].split(":")[0] + ":" + time_split[1].split(":")[1]
                item['state'] = result.get("country")
                item['city'] = result.get("region")
                item['star'] = result.get("star")
                item['title'] = result.get("event_content")

                yield item