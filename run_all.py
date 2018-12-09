import unittest
#import HTMLTestRunner_PY3
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from conf import config
from lib.send_email import send_report

#发现并搜集用例得到一个测试集合
suite = unittest.defaultTestLoader.discover("./testcase")
#使用文本测试运行器 运行测试集合

if __name__ == '__main__':

    #unittest.TextTestRunner(verbosity=2).run(suite)
    config.logging.info("测试开始"+"="*50)
    with open(config.report_file, 'wb') as f:
        HTMLTestRunner(stream=f, title="User接口测试",description='测试报告').run(suite)

    if config.is_send_report:
        send_report()
        config.logging.info("邮件发送成功")
    config.logging.info("测试结束"+"="*50)