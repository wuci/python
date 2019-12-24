# -*- coding: utf-8 -*-

import requests
import scrapy
import datetime

from EraytSpider.items.CalendarItem import EraytspiderItem


class JinSpider(scrapy.Spider):
    name = 'JinSpider'
    allowed_domains = ['jin10.com']
    start_urls = ['http://jin10.com/']

    def parse(self, response):
        # 设置抓取日期(当日)
        timelist = [0]
        for timelist1 in timelist:
            date = (datetime.datetime.now() + datetime.timedelta(days=timelist1)).strftime("%Y%m%d")
            year = str(date)[0:4]
            time = str(date)[4:8]

            # url = "https://rili.jin10.com/datas/" + year + "/" + time + "/economics.json"
            # response = requests.get(url)
            # jsoninfo = response.json()

            item = EraytspiderItem()
            url2 = "https://cdn-rili.jin10.com/data/" + year + "/" + time + "/economics.json"
            req = requests.get(url2)
            jsonResult = req.json()
            # day = 0 是周日,无数据,不爬取
            for result1 in jsonResult:
                resultTime = result1.get('pub_time')
                realTime = datetime.datetime.strptime(str(resultTime).replace("T", " ")[0:16], "%Y-%m-%d %H:%M") \
                           + datetime.timedelta(hours=8)
                item['_id'] = result1.get("id")
                time_split = str(realTime).split(" ")
                item['date'] = time_split[0].replace("-", "")
                item['time'] = time_split[1].split(":")[0] + ":" + time_split[1].split(":")[1]
                item['state'] = result1.get("country")
                if result1.get("unit") is not "%" and result1.get("unit") is not None and result1.get("unit") is not "":
                    item['title'] = result1.get("country") + result1.get("time_period") + \
                                    result1.get("name") + "(" + result1.get("unit") + ")"
                else:
                    item['title'] = result1.get("country") + result1.get("time_period") + result1.get(
                        "name")
                item['importance'] = result1.get("star")
                item['timeNode'] = result1.get("time_period")
                item['details'] = result1.get("name")

                # if result1.get("actual") is not None and result1.get("actual") is not "None":
                #     item['influence'] = "利多"
                # else:
                #     item['influence'] = "未公布"

                #判断影响的标志位
                affect = result1.get("affect")
                # 前值
                before = result1.get("previous")
                # 预测值
                forecast = result1.get("consensus")
                # 公布值
                reality = result1.get("actual")

                if before is not None and before is not "%" and before is not "":
                    if result1.get("unit") is "%":
                        item['before'] = before + "%"
                    else:
                        item['before'] = before
                else:
                    item['before'] = None

                if forecast is not None and forecast is not "":
                    if result1.get("unit") is "%":
                        item['forecast'] = forecast + "%"
                    else:
                        item['forecast'] = forecast
                else:
                    item['forecast'] = None

                if reality is not None and reality is not "":
                    if result1.get("unit") is "%":
                        item['reality'] = reality + "%"
                    else:
                        item['reality'] = reality
                else:
                    item['reality'] = "未公布"



                if forecast is None or forecast is "":
                    forecast = before

                if affect is 0:
                    if reality is not None and reality is not "":
                        if float(reality) > float(forecast) :
                            item['influence'] = "利多"
                        elif reality == forecast:
                            item['influence'] = "影响较小"
                        else:
                            item['influence'] = "利空"

                    else:
                        item['influence'] = "未公布"

                else:
                    if reality is not None and reality is not "":
                        if float(reality) > float(forecast):
                            item['influence'] = "利空"
                        elif reality == forecast:
                            item['influence'] = "影响较小"
                        else:
                            item['influence'] = "利多"

                    else:
                        item['influence'] = "未公布"
                yield item
