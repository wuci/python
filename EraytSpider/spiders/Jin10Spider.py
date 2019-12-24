# -*- coding: utf-8 -*-
import pymongo
import pymongo
import requests
import scrapy
import datetime

from EraytSpider import settings
from EraytSpider.items.CalendarItem import EraytspiderItem

# Author :  Li Yipin
# Date   :  2019/06/17
# Description : 金十财经日历数据抓取模块  timelist 设置爬取的日期 0 代表当日 (生产可设计成每周日爬取下两周的数据)


class Jin10spiderSpider(scrapy.Spider):
    name = 'Jin10Spider'
    allowed_domains = ['jin10.com']
    start_urls = ['http://jin10.com/']

    def parse(self, response):
        # mongodb相关配置
        mongo_client = pymongo.MongoClient(host=settings.MONGODB_HOST,port=settings.MONGODB_PORT)
        mongo_db = mongo_client["Finance"]
        mongo_doc = mongo_db["FinanceCalendar"]
        # 定义一个临时字典，用于判断每天只清空第一次执行的数据库数据
        refer_dict = dict.fromkeys(['tempDate', 'counts'], "0")
        # 设置抓取日期
        for dayNum in list(range(0, 11)):
            current_date = datetime.datetime.now().strftime("%Y%m%d")
            req_date = (datetime.datetime.now() + datetime.timedelta(days=dayNum)).strftime("%Y%m%d")
            if not (not (refer_dict['tempDate'] in "0") and not (refer_dict['tempDate'] not in current_date)) or (refer_dict['tempDate'] in current_date and refer_dict['counts'] in "0") :
                # 执行删除操作后，次数加"1"
                mydoc = mongo_doc.delete_many({"date": current_date})
                print("Today{%s} delete the current text record:{%s}bar." % (current_date, mydoc.deleted_count))
                # 次数赋值，当天第二次循环，不执行删除操作
                refer_dict['counts'] = "1"
                refer_dict['tempDate'] = current_date

            item = EraytspiderItem()

            # 爬取网页数据，进行解析页面
            # url = "https://rili.jin10.com/datas/" + str(req_date)[0:4] + "/" + str(req_date)[4:8] + "/economics.json"
            url = "https://cdn-rili.jin10.com/data/" + str(req_date)[0:4] + "/" + str(req_date)[4:8] + "/economics.json"
            req = requests.get(url)
            json_result = req.json()

            # day = 0 是周日,无数据,不爬取
            for eachResult in json_result:
                # realTime = datetime.datetime.strptime(str(eachResult['pub_time']).replace("T", " ")[0:16],
                # "%Y-%m-%d %H:%M") \ + datetime.timedelta(hours=8)
                utc_time = datetime.datetime.strptime(eachResult['pub_time'], "%Y-%m-%dT%H:%M:%S.%fZ")
                local_time = str(utc_time + datetime.timedelta(hours=8))
                item['_id'] = eachResult.get("id")
                item['date'] = local_time[0:10].replace("-","")
                item['time'] = local_time[11:16]
                item['state'] = eachResult.get("country")
                if eachResult.get("unit") is not "%" and eachResult.get("unit") is not None and eachResult.get("unit") is not "":
                    item['title'] = eachResult['country'] + eachResult['time_period'] + \
                                    eachResult['name'] + "(" + eachResult['unit'] + ")"
                else:
                    item['title'] = eachResult['country'] + eachResult['time_period'] + eachResult['name']

                item['importance'] = eachResult['star']

                item['timeNode'] = eachResult['time_period']
                item['details'] = eachResult['name']

                # 判断影响的标志位
                affect = eachResult['affect']
                # 前值
                before = eachResult['previous']
                # 预测值
                forecast = eachResult['consensus']
                # 公布值
                reality = eachResult['actual']

                if eachResult['revised'] is not None:
                    if eachResult.get("unit") is "%":
                        item['before'] = eachResult['revised'] + "%"
                    else:
                        item['before'] = eachResult['revised']
                else:
                    if (before is not None) and (before is not "%" and before is not ""):
                        if eachResult.get("unit") is "%":
                            item['before'] = before + "%"
                        else:
                            item['before'] = before
                    else:
                        item['before'] = None

                if (forecast is not None) and (forecast is not ""):
                    if eachResult.get("unit") is "%":
                        item['forecast'] = forecast + "%"
                    else:
                        item['forecast'] = forecast
                else:
                    item['forecast'] = "---"

                if (reality is not None) and (reality is not ""):
                    if eachResult.get("unit") is "%":
                        item['reality'] = reality + "%"
                    else:
                        item['reality'] = reality
                else:
                    item['reality'] = "未公布"

                if (forecast is None) or (forecast is ""):
                    forecast = before

                if affect is 0:
                    if (reality is not None) and (reality is not ""):
                        if float(reality) > float(forecast):
                            item['influence'] = "利多"
                        elif reality == forecast:
                            item['influence'] = "影响较小"
                        else:
                            item['influence'] = "利空"
                    else:
                        item['influence'] = "未公布"
                else:
                    if (reality is not None) and (reality is not ""):
                        if float(reality) > float(forecast):
                            item['influence'] = "利空"
                        elif reality == forecast:
                            item['influence'] = "影响较小"
                        else:
                            item['influence'] = "利多"
                    else:
                        item['influence'] = "未公布"
                yield item
