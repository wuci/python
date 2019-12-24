# -*- coding: utf-8 -*-

import scrapy


class BankspiderItem(scrapy.Item):

    _id = scrapy.Field()
    #银行名称
    bank_name = scrapy.Field()
    #货币对
    currency = scrapy.Field()
    #货币对标识
    currency_code = scrapy.Field()
    #买卖方向
    order_type = scrapy.Field()
    #开单价格
    order_data = scrapy.Field()
    #目标价格
    target_data = scrapy.Field()
    #止损价格
    stop = scrapy.Field()
    #类型(基本面/技术面)
    type = scrapy.Field()
    #类型(长期/中期/短期)
    order_term = scrapy.Field()
    #日期
    date = scrapy.Field()
    pass
