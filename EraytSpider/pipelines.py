# -*- coding: utf-8 -*-

from scrapy.conf import settings
import pymongo

# Author :  Li Yipin
# Date   :  2019/06/17
# Description : 数据落地


class EraytspiderPipeline(object):

    #初始化参数
    def __init__(self):

        # 获取setting主机名、端口号和数据库名称
        self.host = settings['MONGODB_HOST']
        self.port = settings['MONGODB_PORT']
        self.dbname = settings['MONGODB_DBNAME']
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.mdb = self.client[self.dbname]

    #根据不同的spiderName存入不同的MongoDB实例
    def process_item(self, item, spider):

        #财经日历(两种情况:1、每周日爬取下两周 2、每天抓取当日)
        if spider.name == 'Jin10Spider' or spider.name == 'JinSpider':
            self.post = self.mdb[settings['MONGODB_DOCNAME']]
            data = dict(item)
            self.post.save(data)
            return item

        # 事件数据(两种情况:1、每周日爬取下两周 2、每天抓取当日)
        if spider.name == 'Jin10EventSpider' or spider.name == 'JinEventSpider':
            self.post = self.mdb[settings['MONGODB_DOCNAME1']]
            data = dict(item)
            self.post.save(data)
            return item

        #资讯数据
        if spider.name == 'Jin10NewsSpider' :
            self.post = self.mdb[settings['MONGODB_DOCNAME2']]
            data = dict(item)
            self.post.save(data)
            return item

        #投行订单数据
        if spider.name == 'Jin10BankSpider' :
            self.post = self.mdb[settings['MONGODB_DOCNAME3']]
            data = dict(item)
            self.post.save(data)
            return item

        #财经日历详情数据
        if spider.name == 'Jin10CalendarDetailsSpider' :
            self.post = self.mdb[settings['MONGODB_DOCNAME4']]
            data = dict(item)
            self.post.save(data)
            return item

        #财经要闻数据
        if spider.name == 'FinanceNewsSpider' :
            self.post = self.mdb[settings['MONGODB_DOCNAME5']]
            data = dict(item)
            self.post.save(data)
            return item

        # 财经资讯数据
        if spider.name == 'Jin10RealNewsSpider':
            self.post = self.mdb[settings['MONGODB_DOCNAME6']]
            data = dict(item)
            self.post.save(data)
            return item

        # 财经日历html页面数据抓取 [测试]
        if spider.name == 'FinanceCalendarSpider':
            self.post = self.mdb[settings['MONGODB_DOCNAME7']]
            data = dict(item)
            self.post.save(data)
            return item



















