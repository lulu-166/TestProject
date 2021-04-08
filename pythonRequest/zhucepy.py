# -*- coding:utf-8 -*-
import requests
#  组建一个post请求 以登录接口为例
login_url="http://47.92.229.35/jiekou/mobile/index.php?act=login&op=register"
login_data={
    "username":"lulu12",
    "password":123123,
    "password_confirm":123123,
    "email":"51156731@qq.com",
    "client":"android"
}
login_header={"Content_type":"application/x-www-form-urlencode"}
rep=requests.post(url=login_url,data=login_data)
print(rep.json())