# -*- coding: utf-8 -*-

import datetime

#Description : 配置类
#Authon : Li Yipin
#Date : 2019/05/14

BOT_NAME = 'EraytSpider'
SPIDER_MODULES = ['EraytSpider.spiders']
NEWSPIDER_MODULE = 'EraytSpider.spiders'
ROBOTSTXT_OBEY = True

# 修改编码为utf-8
FEED_EXPORT_ENCODING = 'utf-8'

ITEM_PIPELINES = {
   'EraytSpider.pipelines.EraytspiderPipeline': 300,
}

#日志配置,无需修改
# LOG_LEVEL = 'ERROR'
# to_day = datetime.datetime.now()
# log_file_path = '/home/redis/PythonProject/logs/scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
# LOG_FILE = log_file_path


########数据库配置######
#主机名
# MONGODB_HOST='192.168.193.108'
MONGODB_HOST='127.0.0.1'
#端口号
MONGODB_PORT = 27017
#数据库名
MONGODB_DBNAME = 'Finance'

#财经日历集合实例名
MONGODB_DOCNAME = 'FinanceCalendar'
#事件集合实例名
MONGODB_DOCNAME1 = 'Event'
#资讯集合实例名
MONGODB_DOCNAME2 = 'Information'
#投行订单集合实例名
MONGODB_DOCNAME3 = 'BankData'
#财经日历详情集合实例名
MONGODB_DOCNAME4 = 'FinanceCalendarDetails'
#财经要闻集合实例名
MONGODB_DOCNAME5 = 'FinanceNews'
#实时资讯集合实例名
MONGODB_DOCNAME6 = 'RealNews'
#实时资讯集合实例名
MONGODB_DOCNAME7 = 'FinCalendar'
















