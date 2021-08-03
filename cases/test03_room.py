from module import ECS
from selenium import webdriver
import unittest
from time import sleep
from ddt import ddt, data, file_data, unpack


@ddt()
class ECSTest(unittest.TestCase, ECS):

    @classmethod
    def setUpClass(cls):
        print("设备测试开始")
        # 浏览器驱动
        cls.driver = webdriver.Firefox()
        # 登录
        ecs = ECS(cls.driver)
        ecs.login("admin", "password")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("设备测试结束")

    @data({"data_center": "自动化测试数据中心"})
    @unpack
    def test01_data_center(self, data_center):
        """ 创建数据中心 """
        self.by_xpath("//span[contains(text(),'平台管理')]").click()
        sleep(1)
        self.by_xpath("//span[contains(text(),'数据中心')]").click()
        self.by_xpath("//span[contains(text(),'创建')]").click()
        self.by_xpath("/html/body/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div/div/input"). \
            send_keys(data_center)
        self.by_xpath("//span[contains(text(),'确定')]").click()
        sleep(1)

    @data({"region": "自动化测试局站", "big_screen": "自动化测试大屏"})
    @unpack
    def test02_region(self, region, big_screen):
        """ 创建局站 """
        self.by_xpath("//span[contains(text(),'自动化测试数据中心')]").click()
        self.by_xpath("//span[contains(text(),'创建')]").click()
        self.by_xpath("/html/body/div/div/div[2]/div[2]/div/div[2]/form/div[2]/div/div/input"). \
            send_keys(region)
        self.by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/form/div[8]/div/div/input"). \
            send_keys(big_screen)
        self.by_xpath("//span[contains(text(),'确定')]").click()
        sleep(1)

    @data({"room": "自动化测试机房", "length": "100", "width": "100", "high": "100"})
    @unpack
    def test03_room(self, room, length, width, high):
        """ 创建机房 """
        self.by_xpath("//span[contains(text(),'自动化测试局站')]").click()
        self.by_xpath("//span[contains(text(),'创建')]").click()
        self.by_xpath("/html/body/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div/div/input"). \
            send_keys(room)
        self.by_xpath("//input[@placeholder='请选择/搜索局站']").click()
        self.by_xpath("//span[contains(text(),'自动化测试局站')]").click()
        self.by_xpath("//input[@placeholder='长度']").send_keys(length)
        self.by_xpath("//input[@placeholder='宽度']").send_keys(width)
        self.by_xpath("//input[@placeholder='高度']").send_keys(high)
        self.by_xpath("//input[@placeholder='请选择外部制冷方式']").click()
        self.by_xpath("//span[contains(text(),'无')]").click()
        self.by_xpath("//input[@placeholder='请选择末端制冷方式']").click()
        self.by_xpath("//span[contains(text(),'风柜制冷')]").click()
        self.by_xpath("//input[@placeholder='请选择送风方式']").click()
        self.by_xpath("//span[contains(text(),'下送风不封闭冷热通道')]").click()
        self.by_xpath("//span[contains(text(),'确定')]").click()

    @data({"manufacturer": "自动化测试厂家", "model": "自动化测试厂家型号"})
    @unpack
    def test04_device_manufacturer(self, manufacturer, model):
        """ 创建设备参数 """
        self.by_xpath("//span[contains(text(),'系统管理')]").click()
        self.by_xpath("//span[contains(text(),'静态数据')]").click()
        self.by_xpath("//div[contains(text(),'设备参数')]").click()
        self.by_xpath("//span[contains(text(),'创建')]").click()
        self.by_xpath("/html/body/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div/div/input"). \
            send_keys(manufacturer)
        self.by_xpath("/html/body/div/div/div[2]/div[2]/div/div[2]/form/div[2]/div/div/input"). \
            send_keys(model)
        self.by_xpath("//input[@placeholder='请选择/搜索设备类型']").click()
        self.by_xpath("//span[contains(text(),'风柜')]").click()
        self.by_xpath("//span[contains(text(),'确定')]").click()
        sleep(1)

    @data({"device": "自动化测试设备", "x": "10", "y": "20", "z": "30"})
    @unpack
    def test05_device(self, device, x, y, z):
        """ 创建物理设备 """
        self.by_xpath("//span[contains(text(),'资源管理')]").click()
        self.by_xpath("//span[contains(text(),'物理设备')]").click()
        self.by_xpath("//span[contains(text(),'创建')]").click()
        self.by_xpath("/html/body/div/div/div[2]/div[2]/div/div[2]/form/div[2]/div/div/input"). \
            send_keys(device)
        self.by_xpath("//input[@placeholder='请选择/搜索平台']").click()
        self.by_xpath("//span[contains(text(),'ftp接口通用配置')]").click()
        self.by_xpath("//input[@placeholder='请选择']").click()
        self.by_xpath("//span[contains(text(),'制冷')]").click()
        self.by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/form/div[5]/div/div/div/input").click()
        self.by_xpath("//span[contains(text(),'风柜')]").click()
        self.by_xpath("//input[@placeholder='X坐标']").send_keys(x)
        self.by_xpath("//input[@placeholder='Y坐标']").send_keys(y)
        self.by_xpath("//input[@placeholder='Z坐标']").send_keys(z)
        self.by_xpath("//input[@placeholder='请选择/搜索设备厂家']").click()
        self.by_xpath("//span[contains(text(),'自动化测试厂家')]").click()
        self.by_xpath("//input[@placeholder='请选择/搜索设备型号']").click()
        self.by_xpath("//span[contains(text(),'自动化测试厂家型号')]").click()
        self.by_xpath("//span[contains(text(),'确定')]").click()

    @data({"device_module": "自动化测试模板"})
    @unpack
    def test06_device_module(self, device_module):
        """ 创建模板 """
        self.by_xpath("//span[contains(text(),'模板管理')]").click()
        self.by_xpath("//span[contains(text(),'创建')]").click()
        self.by_xpath("//input[@placeholder='请选择设备种类']").click()
        self.by_xpath("//span[contains(text(),'制冷')]").click()
        self.by_xpath("//input[@placeholder='请选择设备类型']").click()
        self.by_xpath("//span[contains(text(),'风柜')]").click()
        self.by_xpath("//input[@placeholder='请输入模板名称']").send_keys(device_module)
        self.by_xpath("//span[contains(text(),'确定')]").click()


if __name__ == '__main__':
    # 创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(ECSTest("test01_data_center"))
    suit.addTest(ECSTest("test02_region"))
    suit.addTest(ECSTest("test03_room"))
    suit.addTest(ECSTest("test04_device_manufacturer"))
    suit.addTest(ECSTest("test05_device"))
    suit.addTest(ECSTest("test06_device_module"))

    # 创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)
