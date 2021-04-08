import requests
from config.config1 import HOST

def Test_login_demo(inData,getToken = True):
    url = f"{HOST}/jiekou/mobile/index.php?act=login"

    payload = inData
    res = requests.post(url,data=payload)
    if getToken == True:
        print(res.json()["datas"]["key"])
    else:
        print(res.json())


Test_login_demo({"username":"renhongrui3","password":"123456","client":"ios"})