import scrapy


class RealNewsItem(scrapy.Item):
    # 标识
    _id = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 时间
    time = scrapy.Field()
    # 重要性
    important = scrapy.Field()

    pass
