# -*- coding: utf-8 -*-


import scrapy


#Description : 财经要闻实体类
#Authon : Li HaiTao
#Date : 2019/12/02

class FinanceNewsItem(scrapy.Item):

    _id = scrapy.Field()
    #日期
    date = scrapy.Field()
    #时间
    time = scrapy.Field()
    #标题
    title = scrapy.Field()
    #图片路径
    imgPath = scrapy.Field()
    #在线详情内容
    outline = scrapy.Field()
    #详情内容
    detailsText = scrapy.Field()

    pass
