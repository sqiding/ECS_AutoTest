import unittest
import time
import yagmail
from TestRunner import HTMLTestRunner


# 发送测试报告邮件
def send_mail(report):
    yag = yagmail.SMTP(user="trendy_sender@126.com",
                       password="PEIUFPZDOBJNKAOQ",
                       host='smtp.126.com')
    subject = "ECS/web自动化测试报告"
    contents = "报告见附件"
    receivers = ['dingshuaiqi@trendytech.com.cn',
                 'zhoushuoheng@trendytech.com.cn',
                 'wangbuchao@trendytech.com.cn',
                 'tangtianyin@trendytech.com.cn',
                 'handong@trendytech.com.cn',
                 'liuyongqian@trendytech.com.cn',
                 'wupengwei@trendytech.com.cn',
                 'caifei@trendytech.com.cn',
                 'gaochang@trendytech.com.cn',
                 'yansunbin@trendytech.com.cn']
    yag.send(receivers, subject, contents, report)
    print('邮件发送成功')


if __name__ == '__main__':
    # 指定测试用例目录
    test_dir = './cases'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

    # 测试报告命名
    now_time = time.strftime("%Y.%m.%d %H.%M.%S")
    html_report = './test_report/' + now_time + 'result.html'
    fp = open(html_report, 'wb')
    # 运行测试用例
    runner = HTMLTestRunner(stream=fp,
                            title="ECS测试报告",
                            description="运行环境：Windows 10，Firefox浏览器，172.23.1.31")
    runner.run(suit)
    fp.close()
    send_mail(html_report)  # 发送报告
