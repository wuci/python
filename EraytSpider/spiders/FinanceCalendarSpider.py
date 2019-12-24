import datetime
import scrapy
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from EraytSpider.items.FinanceCalendarItem import FinanceCalendarItem


class FinanceCalendarSpider(scrapy.Spider):
    name = 'FinanceCalendarSpider'
    allow_domains = ['rili.jin10']
    start_urls = ["https://rili.jin10.com/"]

    # def parse(self, response):
    #     # str(datetime.datetime.now().strftime("%Y%m%d"))
    #     item = FinanceCalendarItem()
    #     for dayNum in list(range(0, 9)):
    #         # ('https://rili.jin10.com/?date={}'.format(i) for i in dateList)
    #         # 获取从当日起，推迟10后之间的日期
    #         req_date = (datetime.datetime.now() + datetime.timedelta(days=dayNum)).strftime("%Y%m%d")
    #         req_url = "https://rili.jin10.com/?date="+req_date
    #         # browser = webdriver.Chrome()
    #         # browser.maximize_window()
    #         # 下面三行是隐藏页面加载，上面两行注释为显示加载[功能相同]
    #         chrome_options = Options()
    #         chrome_options.add_argument('--headless')
    #         browser = webdriver.Chrome(options=chrome_options)
    #
    #         browser.get(req_url)
    #         data = browser.page_source
    #         soup = BeautifulSoup(data, 'lxml')
    #         # CSS 选择器  #元素选择器grades = soup.find_all('tr')
    #         grades = soup.select("[id='J_economicsWrap'] tr")
    #         if len(grades) > 1:
    #             # 定义时间和国家临时变量，传递值用
    #             temp_dict = dict.fromkeys(['timeTemp', 'countryAreaTemp'], "--")
    #             for grade in grades:
    #                 if len(grade('td')) == 9:  # 说明是每次循环的第一个td
    #                     # 获取时间和国家
    #                     temp_dict['timeTemp'] = str(grade('td')[0].get_text())
    #                     temp_dict['countryAreaTemp'] = str(grade('td')[1]).split("/flag/")[1].split(".png")[0]
    #                     item['date'] = req_date
    #                     item['time'] = grade('td')[0].get_text()
    #                     item['countryArea'] = str(grade('td')[1]).split("/flag/")[1].split(".png")[0]
    #                     item['indexName'] = str(grade('td')[2].get_text()).strip().split("  ")[0]
    #                     item['importance'] = int(str(grade('td')[3]).split("width:")[1].split("%;\"")[0])//20
    #                     item['beforeValue'] = str(grade('td')[4].get_text()).lstrip().split(" ")[0]
    #                     item['predictiveValue'] = str(grade('td')[5].get_text()).strip()
    #                     item['publishedValue'] = str(grade('td')[6].get_text()).strip()
    #                     item['influence'] = grade('td')[7].get_text()
    #                     item['_id'] = int(str(grade('td')[8]).split("?id=")[1].split("\">")[0])
    #                     pass
    #                 else:
    #                     item['date'] = req_date
    #                     item['time'] = temp_dict.get("timeTemp")
    #                     item['countryArea'] = temp_dict.get("countryAreaTemp")
    #                     item['indexName'] = str(grade('td')[0].get_text()).strip()
    #                     item['importance'] = int(str(grade('td')[1]).split("width:")[1].split("%;\"")[0])//20
    #                     item['beforeValue'] = grade('td')[2].get_text().lstrip().split(" ")[0]
    #                     item['predictiveValue'] = str(grade('td')[3].get_text()).strip()
    #                     item['publishedValue'] = str(grade('td')[4].get_text()).strip()
    #                     item['influence'] = grade('td')[5].get_text()
    #                     item['_id'] = int(str(grade('td')[6]).split("?id=")[1].split("\">")[0])
    #                     pass
    #                 yield item
