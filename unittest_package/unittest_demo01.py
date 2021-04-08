# -*- coding:utf-8 -*-
import unittest
class Baidu(unittest.TestCase):
    def setUp(self):
        print('start')
    def tearDown(self):
        print('end')
    def test_baidu_so(self):
        print('测试用例执行')
if __name__ == '__main__':
    unittest.main(verbosity=2)
#执行顺序：先执行setUp方法，再执行具体的测试用例
# test_baidu_so方法，最后执行tearDown方法。