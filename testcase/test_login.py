import unittest
import requests
import json

from lib import db
from lib import load_data
from conf import config
from lib.case_log import case_log_info


#声明测试类,继承unittest.TestCase
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):   #整个测试类的测试准备方法
        cls.sheet = load_data.get_sheet(config.data_file, "登录")

    @unittest.skipIf(not db.check_user("张三"), "跳过该条用例")
    def test_login_normal(self):
        case_data = load_data.get_case(self.sheet, "test_login_normal")
        url = case_data[2]
        data = json.loads(case_data[3])
        res = requests.post(url=url, data=data)

        case_log_info("test_login_normal",url,case_data[3],case_data[4],res.text)

        self.assertEqual(res.text, "<h1>登录成功</h1>")

    def test_login_password_wrong(self):
        case_data = load_data.get_case(self.sheet, "test_login_password_wrong")
        url = case_data[2]
        data = json.loads(case_data[3])
        res = requests.post(url=url, data=data)
        case_log_info("test_login_password_wrong",url,case_data[3],case_data[4],res.text)
        #self.assertEqual(res   ext, "<h1>失败，用户名或密码错误</h1>")
        self.assertIn("用户名或密码错误", res.text)
if __name__ == '__main__':
    unittest.main(verbosity=2)