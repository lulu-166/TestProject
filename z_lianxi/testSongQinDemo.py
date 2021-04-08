import requests

# 使用cookie 原生和组装
# def login(inData):
#     url ="http://120.55.190.222:7080/api/mgr/loginReq"
#     payload = inData
#     res = requests.post(url,data=payload)
#     # print(res.text)
#     #原生态cookie
#     # print(res.cookies)
#     #封装cookie使用
#     # print(res.cookies['sessionid'])
#     return res.cookies,res.cookies['sessionid']
# #原生态
# cookies1 = login({"username":"auto","password":"sdfsdfsdf"})[0]
# #其他接口使用
# res = requests.post('url',cookies=cookies1)
#
# #组装
# session = login({"username":"auto","password":"sdfsdfsdf"})[1]
# cookies2 = {"sessionid":"session"}
# user_cookie = requests.post("url",cookies2)



import urllib3
requests.packages.urllib3.disable_warnings() #或略警告
def login(inData):
    url ="https://120.55.190.222/api/mgr/loginReq"
    payload = inData
    res = requests.post(url,data=payload,verify=False) #不验证警告
    # print(res.text)
    #原生态cookie
    # print(res.cookies)
    #封装cookie使用
    # print(res.cookies['sessionid'])
    return res.cookies,res.cookies['sessionid']

login({"username":"auto","password":"sdfsdfsdf"})
