# -*- coding: utf-8 -*-

import scrapy

#Description : 事件实体类
#Authon : Li Yipin
#Date : 2019/05/14

class EventspiderItem(scrapy.Item):

    #id
    _id = scrapy.Field()
    #日期
    date = scrapy.Field()
    #时间
    time = scrapy.Field()
    #国家
    state = scrapy.Field()
    #城市
    city = scrapy.Field()
    #重要性
    star = scrapy.Field()
    #指标
    title = scrapy.Field()

    pass
