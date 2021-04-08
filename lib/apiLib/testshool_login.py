import requests,json,data,ddt,unittest
from config.config1 import  HOST1


def loginMethod(inData):
    url = f"{HOST1}/jiekou/mobile/index.php?act=login"
    inData = json.loads(inData)  # 将字符串转成字典
    payload = inData
    res = requests.post(url, data=payload)
    # print(res.text)
    # print(loginMethod(data1, True).text)
    return res


@ddt
class testShoolLogin(unittest.TestCase):
    test_adta1 = [{"username": "kaixin", "password": "123456", "client": "android", "expect": "kaixin"},{"username": "kaixin", "password": "123456", "client": "android", "expect": "kaixin"},{"username": "kaixin", "password": "123456", "client": "android", "expect": "kaixin12"}]
    for i in test_adta1:
        name = loginMethod(json.dumps(i)).json()['datas']['username']
    @data(*test_adta1)
    def test_res(self,data_info):
        self.assertEqual(data_info["expect"],self.name)


if __name__ == '__main__':
    # print(ShoolLogin().loginMethod('''{"username":"kaixin","password":"123456","client":"android"}'''))
    unittest.main()
