import pytest,allure,os
from lib.apiLib.login import LoginDemo
class TestPytestLogin:
    # @pytest.mark.parametrize('inData','{"username":"auto","password":"sdfsdfsdf"}')
    def test_login_data(self):
        res = LoginDemo().login({"username":"auto","password":"sdfsdfsdf"},False)
        assert len(res) != 0 ,"fouzecuole"

if __name__ == '__main__':
    # 报告路径
    pytest.main(['test_pytest_login.py','-s','--alluredir','../report/tmp'])
    #生成报告
    # allure generate
    #起服务  allure server
    os.system('allure server ../report/tmp')