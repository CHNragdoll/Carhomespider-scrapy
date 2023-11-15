import scrapy  # 导入scrapy框架

class CarHomeItem(scrapy.Item):  # 定义CarHomeItem类，继承自scrapy.Item
    serial_number = scrapy.Field()  # 定义一个字段，用于存储序列号
    car_name = scrapy.Field()       # 定义一个字段，用于存储汽车名称
    info_url = scrapy.Field()       # 定义一个字段，用于存储汽车信息的URL
    score_number = scrapy.Field()   # 定义一个字段，用于存储汽车评分
    info_gray = scrapy.Field()      # 定义一个字段，用于存储其他灰色信息（可能是一些附加信息）
    price = scrapy.Field()          # 定义一个字段，用于存储汽车价格
