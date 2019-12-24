# -*- coding: utf-8 -*-


import scrapy

#Description : 财经日历实体类
#Authon : Li Yipin
#Date : 2019/05/14

class EraytspiderItem(scrapy.Item):

    #id
    _id = scrapy.Field()
    #日期
    date = scrapy.Field()
    #时间
    time = scrapy.Field()
    #国家
    state = scrapy.Field()
    #指标
    title = scrapy.Field()
    #重要性
    importance = scrapy.Field()
    #前值
    before = scrapy.Field()
    #后值
    forecast = scrapy.Field()
    #公布值
    reality = scrapy.Field()
    #影响(A类)
    influence = scrapy.Field()
    #事件节点
    timeNode = scrapy.Field()
    #日历详情
    details = scrapy.Field()
    pass
