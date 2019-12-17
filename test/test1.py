# -*- coding: utf-8 -*-
# @Time    : 2019/12/17
# @Author  : Yifei Duan
# @Summary :
import json
import requests

content = {
   "group": "panic/abc",
   "business": "服务运行",
   "title": "生产环境 发现服务运行错误",
   "section": "panic",
   "content": "test-panic-alert-test12345",
   "source": "服务监控"
}

send_data = json.dumps(content)

r = requests.post("http://alarm.pri.ibanyu.com:8188/alert", data=send_data)

print(r.text)
