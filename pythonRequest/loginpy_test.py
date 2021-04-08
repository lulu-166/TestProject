# -*- coding:utf-8 -*-
import requests
import unittest
class Login_demo(unittest.TestCase):
    #  组建一个post请求 以登录接口为例
    login_url = "http://47.92.229.35/jiekou/mobile/index.php?act=login"
    login_data = {
        "username": "lulu123",
        "password": 123123,
        "client": "android"
    }
    login_header = {"Content_type": "application/x-www-form-urlencode"}
    rep = requests.post(url=login_url, data=login_data, json=login_header)
    @classmethod
    def setUpClass(cls):
        print('111')
    @classmethod
    def tearDownClass(cls):
        print("ok123")

    def test_001(self):
       a=self.rep.status_code
       self.assertEqual(a, 200)

    def test_002(self):
        a="lulu123"
        b = self.rep.text
        self.assertIn(a, b)
        print(b)
if __name__=='__main__':
    unittest.main(verbosity=2)