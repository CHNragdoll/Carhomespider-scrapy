# 在此定义您的爬虫中间件模型
#
# 参考文档：
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals  # 从scrapy导入signals模块

# 用于通过单一接口处理不同类型项目的工具
from itemadapter import is_item, ItemAdapter  # 从itemadapter导入is_item和ItemAdapter

class CarhomeScraperSpiderMiddleware:
    # 不需要定义所有方法。如果未定义某个方法，
    # scrapy将表现得就像爬虫中间件没有修改传递的对象。

    @classmethod
    def from_crawler(cls, crawler):
        # Scrapy使用此方法创建您的爬虫。
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)  # 连接spider_opened信号
        return s

    def process_spider_input(self, response, spider):
        # 每个通过爬虫中间件进入爬虫的响应都会调用此方法。

        # 应返回None或引发异常。
        return None

    def process_spider_output(self, response, result, spider):
        # 在Spider处理完响应后，使用从Spider返回的结果调用此方法。

        # 必须返回Request或item对象的可迭代对象。
        for i in result:
            yield i  # 生成处理结果

    def process_spider_exception(self, response, exception, spider):
        # 当爬虫或process_spider_input()方法（来自其他爬虫中间件）引发异常时调用。

        # 应返回None或Request或item对象的可迭代对象。
        pass

    def process_start_requests(self, start_requests, spider):
        # 使用爬虫的起始请求调用此方法，工作方式类似于process_spider_output()方法，只是它没有关联的响应。

        # 必须只返回请求（不是项目）。
        for r in start_requests:
            yield r  # 生成起始请求

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)  # 记录爬虫开启的日志


class CarhomeScraperDownloaderMiddleware:
    # 不需要定义所有方法。如果未定义某个方法，
    # scrapy将表现得就像下载器中间件没有修改传递的对象。

    @classmethod
    def from_crawler(cls, crawler):
        # Scrapy使用此方法创建您的爬虫。
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)  # 连接spider_opened信号
        return s

    def process_request(self, request, spider):
        # 每个通过下载器中间件的请求都会调用此方法。

        # 必须：
        # - 返回None：继续处理此请求
        # - 或返回一个Response对象
        # - 或返回一个Request对象
        # - 或引发IgnoreRequest：将调用已安装的下载器中间件的process_exception()方法
        return None

    def process_response(self, request, response, spider):
        # 用从下载器返回的响应调用此方法。

        # 必须：
        # - 返回一个Response对象
        # - 返回一个Request对象
        # - 或引发IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # 当下载处理程序或process_request()
        # （来自其他下载器中间件）引发异常时调用。

        # 必须：
        # - 返回None：继续处理此异常
        # - 返回一个Response对象：停止process_exception()链
        # - 返回一个Request对象：停止process_exception()链
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)  # 记录爬虫开启的日志
