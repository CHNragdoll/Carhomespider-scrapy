import json  # 导入json模块，用于处理JSON文件的读写

class CarHomePipeline:
    def open_spider(self, spider):
        # 当爬虫开启时调用此方法
        self.file = open('car_data.json', 'w', encoding='utf-8')  # 打开一个名为'car_data.json'的文件用于写入
        self.data = []  # 初始化一个列表，用于存储数据

    def close_spider(self, spider):
        # 当爬虫关闭时调用此方法
        json.dump(self.data, self.file, ensure_ascii=False, indent=4)  # 将数据写入JSON文件
        self.file.close()  # 关闭文件

    def process_item(self, item, spider):
        # 对每个item进行处理的方法
        self.data.append(dict(item))  # 将item转换为字典并添加到列表中
        return item  # 返回item
