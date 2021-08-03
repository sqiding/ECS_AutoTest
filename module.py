from selenium.webdriver import ActionChains
from ECS_page import ECSPage

class ECS(ECSPage):
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://172.23.1.31"
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def login(self, username, password):
        """登录"""
        # self.driver.switch_to.frame('x-URS-iframe')
        page = ECSPage(self.driver)
        self.open(self.base_url + "/#/dashboard/index")
        page.username_input = username
        page.password_input = password
        js = 'return document.getElementsByClassName("identity")[0].__vue__.captchaCode'
        page.ver_code_input = self.driver.execute_script(js)
        page.login_button.click()

    def logout(self):
        """退出"""
        page = ECSPage(self.driver)
        above = self.driver.find_element_by_xpath("//span[@class='name']")
        ActionChains(self.driver).move_to_element(above).perform()
        page.logout_button.click()

    # 打开页面
    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    # id定位
    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    # name定位
    def by_name(self, name):
        return self.driver.find_element_by_name(name)

    # class定位
    def by_class(self, class_name):
        return self.driver.find_element_by_class_name(class_name)

    # XPath定位
    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # CSS定位
    def by_css(self, css):
        return self.driver.find_element_by_css_selector(css)

    # 获取title
    def get_title(self):
        return self.driver.title

    # 获取页面text，仅使用Xpath
    def get_text(self, xpath):
        return self.by_xpath(xpath).text

    # 执行JavaScript脚本
    def js(self, script):
        self.driver.execute_script(script)
