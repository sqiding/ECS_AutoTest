from poium import Page, Element

class ECSPage(Page):
    """Page层，封装定位元素"""
    username_input = Element(css="[placeholder='用户名']", describe="登录名")
    password_input = Element(css="[placeholder='密码']")
    ver_code_input = Element(css="[placeholder='验证码']")
    login_button = Element(xpath="//span[contains(text(),'登录')]")
    user_button = Element(xpath="//span[@class='name']")
    logout_button = Element(xpath="//span[contains(text(),'退出登录')]", timeout=10)
