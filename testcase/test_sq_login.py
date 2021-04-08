from tools.get_excel import get_excel,set_excel
import pytest,os,allure
#读取过来excel的数据
dataList = get_excel("loginData",0,6)
excel_name_new,new_excel_data = set_excel()

from lib.apiLib.login import LoginDemo
#链接请求
@allure.feature('测试用例功能')
class Test:
    def testDemo(self):
        for i in dataList:
            res = LoginDemo().login({"username":i[0],"password":i[1]},False)
            if len(res) !=0:
                print("正确")
            else:
                print("错了")


if __name__ == '__main__':
    pytest.main(['test_sq_login.py','-s','--alluredir','../report/tmp'])
    # 生成报告
    # allure generate
    # 起服务  allure server
    os.system('allure serve alluredir ../report/tmp')