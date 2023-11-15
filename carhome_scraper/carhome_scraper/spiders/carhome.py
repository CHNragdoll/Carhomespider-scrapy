import scrapy  # 导入scrapy框架
from carhome_scraper.items import CarHomeItem  # 从项目的items模块导入CarHomeItem类
import re  # 导入正则表达式库

class CarHomeSpider(scrapy.Spider):  # 定义一个CarHomeSpider类，继承scrapy.Spider
    name = 'carhome'  # 爬虫的名字
    allowed_domains = ['car.autohome.com.cn']  # 允许爬取的域名
    start_urls = ['https://car.autohome.com.cn/price/list-100_0-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html']  # 开始爬取的URL

    max_pages = 10  # 最大爬取页数
    current_page = 1  # 当前页数
    items_per_page = 15  # 每页最大条目数
    current_item_global = 1  # 全局条目计数器

    def parse(self, response):  # 定义解析响应的方法
        # 定义正则表达式用于匹配网页中的特定信息
        url_name_re = re.compile(r'<a href="/price/series-(\d+).html#pvareaid=(\d+)" target="_self" class="font-bold">(.*?)</a>')
        score_number_re = re.compile(r'<span class="score-number">(.*?)</span>')
        info_gray_re = re.compile(r'别：<span class="info-gray">(.*?)</span>')
        price_re = re.compile(r'指导价：<span class="lever-price red"><span class="font-arial">(.*?)</span>')

        # 使用正则表达式提取网页内容
        url_name_li = url_name_re.findall(response.text)
        score_number_li = score_number_re.findall(response.text)
        info_gray_li = info_gray_re.findall(response.text)
        price_li = price_re.findall(response.text)

        # 遍历提取出的信息，并封装成item
        for i, (url_id1, url_id2, car_name) in enumerate(url_name_li):
            if i < self.items_per_page:
                item = CarHomeItem()
                item['serial_number'] = self.current_item_global
                item['car_name'] = car_name
                item['info_url'] = f'https://car.autohome.com.cn/price/series-{url_id1}.html#pvareaid={url_id2}'
                item['score_number'] = score_number_li[i] if i < len(score_number_li) else "N/A"
                item['info_gray'] = info_gray_li[i] if i < len(info_gray_li) else "N/A"
                item['price'] = price_li[i] if i < len(price_li) else "N/A"

                self.current_item_global += 1
                yield item  # 生成item
            else:
                break

        # 准备爬取下一页
        if self.current_page < self.max_pages:
            self.current_page += 1
            next_page = response.urljoin(f"/price/list-100_0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-{self.current_page}.html")
            yield scrapy.Request(next_page, callback=self.parse)  # 发起对下一页的请求
