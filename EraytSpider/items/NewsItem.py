# -*- coding: utf-8 -*-


import scrapy


#Description : 资讯实体类
#Authon : Li Yipin
#Date : 2019/05/14

class NewsspiderItem(scrapy.Item):

    _id = scrapy.Field()
    #日期
    date = scrapy.Field()
    #时间
    time = scrapy.Field()
    #标题
    title = scrapy.Field()

    pass
