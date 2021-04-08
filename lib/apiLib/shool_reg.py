import requests,json
from config.config1 import  HOST1
class ShoolLogin:
    def loginMethod(self,inData,getToken = True):
        url = f"{HOST1}/jiekou/mobile/index.php?act=login&op=register"
        # inData = json.loads(inData) # 将字符串转成字典
        payload = inData
        res = requests.post(url,data=payload)
        print(res.text)

if __name__ == '__main__':
    print(ShoolLogin().loginMethod({"username":"kaixin","password":"123456","password_confirm":"123456","email":"34532423@qq.com","client":"android"}))

