from selenium import webdriver
import unittest
from module import ECS


class ECSTest(unittest.TestCase, ECS):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        print("登录登出测试开始")

    def test01_login(self):
        """ ECS登录测试 """
        self.ecs = ECS(self.driver)
        self.ecs.login("admin", "password")

    def test02_logout(self):
        """ ECS登出测试 """
        self.ecs = ECS(self.driver)
        self.logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("登录登出测试结束")


if __name__ == '__main__':
    # 创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(ECSTest("test01_login"))
    suit.addTest(ECSTest("test02_logout"))

    # 创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)
