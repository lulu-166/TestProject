# -*- coding:utf-8 -*-
import pytest
class Test():
    def setup(self):
        print("setup_function--->")
    def teardown(self):
        print("teardown_function-->")
    def test_01(self):
        print("0001")
    def test_02(self):
        print("0002")
    def test_03(self):
        print("0003")
if __name__=='__main__':
    # pytest.main(["-s","-v","demo1.py"])
#  参数说明 -s执行打印出详细结果 -v显示是否passed
     pytest.main(["-q", "demo1.py", "--html=d://report.html"])
# --html=report.html 生成测试报告，也可以自定义报告路径如：--html=d://report.html
