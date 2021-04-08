# -*- coding:utf-8 -*-
import unittest
from ddt import ddt, data


def A(a, b):
    # 测试函数
    return a+b


@ddt
class TestA(unittest.TestCase):
    # 测试数据
    test_data = [{"a": 3, "b": 5, "expect": 8},
                 {"a": 3, "b": 3, "expect": 6}]

    @data(*test_data)
    def test_right(self, data_info):
        # 测试用例
        self.assertEqual(data_info["expect"], A(data_info["a"], data_info["b"]), "用例执行失败")


if __name__ == '__main__':
    # 执行所有的用例
    unittest.main()