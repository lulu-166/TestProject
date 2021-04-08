import requests,hashlib,json
from config.config1 import HOST
# def get_md5(psw):
#     md5 = hashlib.md5() #实例化对象
#     md5.update(psw.encode('utf-8')) # 加密操作
#     return md5.hexdigest() # hexdigets方法获取加密的结果
class LoginDemo:
    def login(self,inData,getToken=True):
        url = f'{HOST}/api/mgr/loginReq'
        # inData['password'] = get_md5(inData['password'])
        # inData = json.loads(inData)  #将字符串转换为字典
        payload = inData
        res = requests.post(url,data=payload)
        # print(res.text)
        if getToken:
            return  res.cookies['sessionid']
        else:
            return res.cookies


if __name__ == '__main__':
    print(LoginDemo().login({"username":"auto","password":"sdfsdfsdf"}),"%%")
    print("**")