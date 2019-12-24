# -*- coding: utf-8 -*-
import datetime
import time
import scrapy
import requests
from lxml import etree
import html
import json
import re

# Author :  Li HaiTao
# Date   :  2019/12/02
# Description : 财经要闻数据抓取模块 (抓取当日数据)
from EraytSpider.items.FinanceNewsItem import FinanceNewsItem


class FinanceNewsSpider(scrapy.Spider):
    name = 'FinanceNewsSpider'
    allowed_domains = ['forex.fx168.com/']
    start_urls = ['https://forex.fx168.com/top/']

    def trim(self, textStr):
        if textStr is not None and textStr.endswith(' '):
            return re.sub(r"^(\s+)|(\s+)$", "", textStr)
        return textStr

    def parse(self, response):
        date = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime("%Y%m%d")
        currentTime = int(round(time.time() * 1000))
        item = FinanceNewsItem()

        # reqUrl = "https://api3.fx168api.com/cms/GetIndexNewsById.aspx?chid=2934&pnum=1&psize=20&callback=GetHistory&_="+str(currentTime)
        reqUrl = "https://api3.fx168api.com/cms/GetNewsByLmId.aspx?chid=2822&pnum=1&psize=150&callback=GetHistory"  # &_="+str(currentTime)
        reqData = requests.get(reqUrl)
        reqDealData = reqData.content.decode().replace("GetHistory(", "").strip(")")

        dataList = json.loads(reqDealData)
        if len(dataList):
            for eachData in dataList:
                if "forex.fx168.com" in eachData['appfilePath'] or "非农" in eachData['firstkey']:
                    # 唯一标识
                    item['_id'] = eachData['docid']
                    # 标题
                    item['title'] = eachData['doctitle']
                    # 图片路径
                    item['imgPath'] = eachData['appfilePath'] + "/" + eachData['appfile']
                    # 在线详情内容
                    if "讯 " in eachData['zhaiyao']:
                        item['outline'] = eachData['zhaiyao'].split(" ", 1)[1]
                    else:
                        item['outline'] = eachData['zhaiyao']
                    # 日期
                    item['date'] = eachData['docfirstpubtime'].replace("-", "")[0:8]
                    # 时间
                    item['time'] = eachData['docfirstpubtime']
                    # 详情内容
                    reqDetail = requests.get(eachData['docpuburl'])
                    # 获取html中的详情文本内容
                    divContainer = etree.HTML(reqDetail.content).xpath('//div[@class="TRS_Editor"]')[0]
                    divDataFormat = html.unescape(str(etree.tostring(divContainer)))
                    divContent = str(divDataFormat).replace("b'<div class=\"TRS_Editor\">", "").replace("</div>\\n", "")
                    divContentDeal = divContent.replace("(北美)", "").replace("24K99", "Erayt").strip("'").replace(
                        "FX168财经报社(香港)", "Erayt")
                    divDetails = re.sub(r'<img\b[^>]*>', '', divContentDeal).replace("<p align=\"justify\">  </p>", "")
                    item['detailsText'] = divDetails.rstrip().replace('\\t',"")
                    yield item


