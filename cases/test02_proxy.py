from module import ECS
from selenium import webdriver
import unittest
from ddt import ddt, data, file_data, unpack


@ddt
class ECSTest(unittest.TestCase, ECS):

    @classmethod
    def setUpClass(cls):
        print("代理测试开始")
        cls.driver = webdriver.Firefox()
        # 登录
        ecs = ECS(cls.driver)
        ecs.login("admin", "password")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("代理测试结束")

    @data({"proxy": "自动化测试proxy", "ip": "172.23.1.31", "port": "18001"})
    @unpack
    def test01_proxy(self, proxy, ip, port):
        """ 创建代理测试 """
        self.by_xpath("//span[contains(text(),'节能管理')]").click()
        self.by_xpath("//span[contains(text(),'代理管理')]").click()
        self.by_xpath("//span[contains(text(),'创建')]").click()
        self.by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div[2]/form/div[1]/div/div/input").send_keys(proxy)
        self.by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div[2]/form/div[2]/div/div/input").send_keys(ip)
        self.by_xpath("/html/body/div/div[1]/div[2]/div[2]/div/div[2]/form/div[3]/div/div/input").send_keys(port)
        self.by_xpath("//span[contains(text(),'确定')]").click()

    @data({"platform": "自动化测试平台"})
    @unpack
    def test02_platform(self, platform):
        """ 创建平台测试 """
        self.by_xpath("//span[contains(text(),'平台管理')]").click()
        self.by_xpath("/html/body/div/div/div[1]/div[2]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li").click()
        self.by_xpath("//span[contains(text(),'创建')]").click()
        self.by_xpath("/html/body/div/div/div[2]/div[2]/div/div[2]/form/div[1]/div/div/input").send_keys(platform)
        self.by_xpath("//input[@placeholder='请选择']").click()
        self.by_xpath("//span[contains(text(),'动环')]").click()
        self.by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div[2]/form/div[3]/div/div/div/input").click()
        self.by_xpath("//span[contains(text(),'172.23.1.31')]").click()
        self.by_xpath("//span[contains(text(),'确定')]").click()

    @data({"task": "自动化测试任务"})
    @unpack
    def test03_schedule_task(self, task):
        """ 创建采集任务测试 """
        self.by_xpath("//span[contains(text(),'自动化测试平台')]").click()
        self.by_xpath("//span[contains(text(),'创建')]").click()
        self.by_xpath("//input[@placeholder='请输入任务名称']").send_keys(task)
        self.by_xpath("//input[@placeholder='请选择']").click()
        self.by_xpath("//span[contains(text(),'逻辑变量历史数据计算任务')]").click()
        self.by_xpath("//input[@placeholder='请选择时间类型']").click()
        self.by_xpath("//span[contains(text(),'cron表达式')]").click()
        self.by_xpath("//input[@placeholder='请选择cron表达式']").click()
        self.by_xpath("//span[contains(text(),'每分钟执行一次')]").click()
        self.by_xpath("//span[contains(text(),'确认')]").click()


if __name__ == '__main__':
    # 创建测试套件
    suite = unittest.TestSuite()
    suite.addTest(ECSTest("test01_proxy"))
    suite.addTest(ECSTest("test02_platform"))
    suite.addTest(ECSTest("test03_schedule_task"))

    # 创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suite)
