import csv  # 导入csv模块，用于处理CSV文件的读写

class CarHomePipeline:
    def open_spider(self, spider):
        # 当爬虫开启时调用此方法
        self.file = open('car_data.csv', 'w', newline='', encoding='utf-8')  # 打开一个名为'car_data.csv'的文件用于写入，指定编码为utf-8
        self.writer = csv.writer(self.file)  # 创建一个csv写入器
        self.writer.writerow(['序号', '车名', '详情链接', '用户评分', '级别', '官方指导价'])  # 写入CSV文件的头部信息

    def close_spider(self, spider):
        # 当爬虫关闭时调用此方法
        self.file.close()  # 关闭文件

    def process_item(self, item, spider):
        # 对每个item进行处理的方法
        self.writer.writerow([item['serial_number'], item['car_name'], item['info_url'], item['score_number'], item['info_gray'], item['price']])  # 将item中的数据写入CSV文件
        return item  # 返回item
