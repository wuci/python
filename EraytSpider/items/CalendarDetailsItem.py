# -*- coding: utf-8 -*-


import scrapy

#Description : 财经日历详情实体类
#Authon : Li Yipin
#Date : 2019/05/14

class CalendarDetailsItem(scrapy.Item):

    #id
    _id = scrapy.Field()
    #
    relationId = scrapy.Field()
    #下次公布日期
    nextTime = scrapy.Field()
    #公布机构
    publishAgencies = scrapy.Field()
    #公布频率
    reportFrequency = scrapy.Field()
    #统计方法
    statisticalMethod = scrapy.Field()
    #数据影响
    dataInfluence = scrapy.Field()
    #数据释意
    dataInterpretation = scrapy.Field()
    #趣味解读
    interestRead = scrapy.Field()

    pass