import scrapy


# 用BeautifulSoup 4 + Scrapy实现财经日历数据爬取
# author: lee
# date: 2019-12-19 0:24
class FinanceCalendarItem(scrapy.Item):
    # 唯一标识
    _id = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 时间
    time = scrapy.Field()
    # 国/区
    countryArea = scrapy.Field()
    # 指标名称
    indexName = scrapy.Field()
    # 重要性
    importance = scrapy.Field()
    # 前值
    beforeValue = scrapy.Field()
    # 预测值
    predictiveValue = scrapy.Field()
    # 公布值
    publishedValue = scrapy.Field()
    # 影响
    influence = scrapy.Field()
    # 解读
    # unscramble = scrapy.Field()
    pass
