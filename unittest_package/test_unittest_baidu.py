# -*- coding:utf-8 -*-
import unittest
from selenium import webdriver
class baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("ok")
    @classmethod
    def tearDownClass(cls):
        print("ok123")
    def test_001(self):
        a = '111'
        b = '112'
        self.assertEqual(a, b)
        print("yy")
'''      
    def test_002(self):
         print("lala")
'''
if __name__=='__main__':
    unittest.main(verbosity=2)
