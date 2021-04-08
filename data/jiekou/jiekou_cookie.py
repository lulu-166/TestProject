import requests
from config.config1 import HOST
def login(datas):
    url = f"{HOST}/api/mgr/loginReq"
    payload = datas
    res = requests.post(url,data=payload)
    # print(res.text)
    # print(res.json())
    print(res.cookies)
    print(res.cookies['sessionid'])
    return res.cookies,res.cookies['sessionid']
# cookies1 = login({'username':'auto','password':'sdfsdfsdf'})[0]
# res = requests.post('url',cookies=cookies1)


# session = login({'username':'auto','password':'sdfsdfsdf'})[1]
# user_cookies = {"sessionid":session}
# res = requests.post('url',cookies=user_cookies)
login({'username':'auto','password':'sdfsdfsdf'})
