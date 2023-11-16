# Scrapy设置，用于carhome_scraper项目
#
# 为了简化，此文件只包含被认为重要或常用的设置。
# 您可以通过以下文档了解更多设置：
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "carhome_scraper"  # 设置爬虫项目的名称

SPIDER_MODULES = ["carhome_scraper.spiders"]  # 设置包含爬虫的模块
NEWSPIDER_MODULE = "carhome_scraper.spiders"  # 设置新爬虫的模块

ITEM_PIPELINES = {
   'carhome_scraper.pipelines.CarHomePipeline': 300,  # 启用并设置项目管道
}

DOWNLOAD_DELAY = 2  # 设置下载延迟为2秒
CONCURRENT_REQUESTS = 16  # 设置最大并发请求数
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'  # 设置用户代理
COOKIES_ENABLED = False  # 禁用Cookies
LOG_LEVEL = 'INFO'  # 设置日志级别
AUTOTHROTTLE_ENABLED = True  # 启用自动限速
AUTOTHROTTLE_START_DELAY = 5  # 设置自动限速的起始延迟
AUTOTHROTTLE_MAX_DELAY = 60  # 设置自动限速的最大延迟
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # 设置目标并发率
AUTOTHROTTLE_DEBUG = False  # 设置自动限速的调试模式

# 负责地爬取，通过用户代理标识自己（及您的网站）
#USER_AGENT = "carhome_scraper (+http://www.yourdomain.com)"

# 遵守robots.txt规则
ROBOTSTXT_OBEY = False

# 配置Scrapy执行的最大并发请求（默认：16）
#CONCURRENT_REQUESTS = 32

# 配置对同一网站的请求之间的延迟（默认：0）
# 参考 https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# 也可以查看自动限速设置和文档
#DOWNLOAD_DELAY = 3
# 下载延迟设置将只尊重以下之一：
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# 禁用cookies（默认启用）
#COOKIES_ENABLED = False

# 禁用Telnet控制台（默认启用）
#TELNETCONSOLE_ENABLED = False

# 覆盖默认的请求头：
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# 启用或禁用爬虫中间件
# 参考 https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    "carhome_scraper.middlewares.CarhomeScraperSpiderMiddleware": 543,
}

# 启用或禁用下载器中间件
# 参考 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "carhome_scraper.middlewares.CarhomeScraperDownloaderMiddleware": 543,
}

# 启用或禁用扩展
# 参考 https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# 配置项目管道
# 参考 https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "carhome_scraper.pipelines.CarhomeScraperPipeline": 300,
#}

# 启用并配置自动限速扩展（默认禁用）
# 参考 https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# 初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# 在高延迟情况下设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# Scrapy应该并行发送到每个远程服务器的请求的平均数量
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 启用每个接收到的响应的限速统计显示：
#AUTOTHROTTLE_DEBUG = False

# 启用并配置HTTP缓存（默认禁用）
# 参考 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# 将默认值已弃用的设置设置为未来证明的值
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
