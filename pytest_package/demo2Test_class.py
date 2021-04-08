# -*- coding:utf-8 -*-
import pytest
import unittest
import requests
class Test_01(unittest.TestCase):
    @classmethod
    def setup_class(cls): #格式固定
        print("这里是开始...")
    @classmethod
    def teardown_class(cls):
        print("这里是结束...")
    def test_01(self):
        login_url = "http://47.92.229.35/jiekou/mobile/index.php?act=login&op=register"
        login_data = {
            "username": "lulu012345678",
            "password": 123123,
            "password_confirm": 123123,
            "email": "5112673561@qq.com",
            "client": "android"
        }
        login_header = {"Content_type": "application/x-www-form-urlencode"}
        rep = requests.post(url=login_url, data=login_data)
        print(rep.json())
        a=rep.json()
        print(a)
        # 转化为json格式，才能进行断言
        # 断言的第一种方法：
        '''if a['code'] == 400:
         print('登录成功！')
        else:
         print('登录失败!')'''
        # 断言的第二种方法：类里需要导入unittest.TestCase才可以实现
        self.assertEqual(200,a['code'])#成功不会打印任何信息，失败会报错
        #assert a['code'] == 200  pytest框架可以用
    def test_02(self):
        print("0002")
    def yy(self):
        print("0003")
if __name__=="__main__":
    pytest.main(["-s", "demo2Test_class.py"])

#  setUp和tearDown 每个方法执行前后都会执行
# setup_class 和 teardown_class 在所有方法执行前后去执行一次