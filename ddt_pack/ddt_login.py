# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
from ddt import data,unpack,ddt
@ddt
class EcshopLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get('http://47.92.229.35/ecshop/')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/font/a[1]/img').click()
    def tearDown(self):
        self.driver.quit()
    @data(('lulu','123456','lulu'),('','','- 用户名不能为空。- 登录密码不能为空。'),('','123456','请输入用户名'))
    @unpack
    def test_login(self,username,password,result):
        '''验证ECShop登录三种情况'''
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/form/table/tbody/tr[1]/td[2]/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/form/table/tbody/tr[2]/td[2]/input').send_keys(password)
        self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/form/table/tbody/tr[4]/td[2]/input[3]').click()
        divTest=self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/ul/li[1]/font/font/font').text
        self.assertEqual(divTest,result)
if __name__ == '__main__':
    unittest.main(verbosity=2)
