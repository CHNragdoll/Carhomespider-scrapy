import openpyxl  # 导入openpyxl模块

class CarHomePipeline:
    def open_spider(self, spider):
        # 当爬虫开启时调用此方法
        self.workbook = openpyxl.Workbook()  # 创建一个新的工作簿
        self.sheet = self.workbook.active  # 获取活动的工作表
        self.sheet.append(['序号', '车名', '详情链接', '用户评分', '级别', '官方指导价'])  # 写入表头

    def close_spider(self, spider):
        # 当爬虫关闭时调用此方法
        self.workbook.save('car_data.xlsx')  # 保存工作簿为car_data.xlsx文件
        self.workbook.close()  # 关闭工作簿

    def process_item(self, item, spider):
        # 对每个item进行处理的方法
        self.sheet.append([item['serial_number'], item['car_name'], item['info_url'], item['score_number'], item['info_gray'], item['price']])  # 将item数据添加到工作表
        return item  # 返回item
