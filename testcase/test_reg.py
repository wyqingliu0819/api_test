import unittest
import requests
import json

from lib import db
from lib import load_data
from conf import config
from lib.case_log import case_log_info
#from lib.db import check_user, del_user


class TestReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet = load_data.get_sheet(config.data_file, "注册")
    def test_reg_normal(self):
        case_data = load_data.get_case(self.sheet, "test_reg_normal")
        url = case_data[2]
        data = json.loads(case_data[3])
        NAME  = data["name"]
        if db.check_user(NAME):
             db.del_user(NAME)
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url, json=data)
        # str =res.json()["msg"]
        # self.assertIn("成功", str)
        #self.assertTrue(fun.check_user("wangwu005"))
        #self.assertTrue(db.check_user("wangwu005"))
        case_log_info("test_reg_normal",url,case_data[3],case_data[4],res.text)
        self.assertDictEqual(excepted_res, res.json())
        #数据清理
        db.del_user(NAME)

    def test_reg_user_exis(self):
        case_data = load_data.get_case(self.sheet, "test_reg_user_exis")
        url = case_data[2]
        data = json.loads(case_data[3])
        excepted_res = json.loads(case_data[4])
        res = requests.post(url=url, json=data)
        case_log_info("test_reg_user_exis",url,case_data[3],case_data[4],res.text)
        self.assertDictEqual(res.json(), excepted_res)

if __name__ == '__main__':
    unittest.main(verbosity=2)