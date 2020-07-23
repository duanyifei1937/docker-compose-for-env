# -*- coding: utf-8 -*-
# @Time    : 2020/1/19
# @Author  : Yifei Duan
# @Summary :



import io
import sys
import time
from flask import Flask, Response, request
import requests
import logging
import json
import locale

# # 系统输出utf-8编码
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
# locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

app = Flask(__name__)

# 定义日志格式、级别
console = logging.StreamHandler()
# fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
# formatter = logging.Formatter(fmt)
# console.setFormatter(formatter)
# log = logging.getLogger("flask_webhook_dingtalk")
log = logging.getLogger("")
log.addHandler(console)
log.setLevel(logging.DEBUG)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/<profiledd>/send/', methods=['POST'])
def hander_session(profiledd):

    dingtalk_profile = dict(
        {
            'duanyifei':
                'https://oapi.dingtalk.com/robot/send?access_token=346569526a79756ab9f44dacf2ede800d43656e1da9086a875857a1ef396d988'
        }
    )
    # 判断是否存在send key
    if profiledd in dingtalk_profile:

        # profile_url为dingtalk link
        profile_url = dingtalk_profile[profiledd]

        # json转换为python dict
        post_data = request.get_data()
        # print("--- {}".format(post_data))
        log.info(post_data)

        # 由alertmanager dict截取需要的报警信息
        post_data = json.loads(post_data.decode("utf-8"))['alerts']
        for i in post_data:
            try:
                try:
                    alert_status = i['status']
                except:
                    alert_status = "unkown!"
                try:
                    alert_name = i['labels']['alertname']
                except:
                    alert_name = "no alertname"
                try:
                    startat = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime())
                except:
                    startat = i['startsAt']
                try:
                    summary123 = i['annotations']['summary']
                except Exception:
                    try:
                        summary123 = i['annotations']['message']
                    except Exception:
                        summary123 = 'unknow!'
                try:
                    instances123 = i['labels']['instance']
                except:
                    instances123 = "unknow instance"
                try:
                    service_name = i['labels']['service']
                except:
                    service_name = "unknow server name"
                try:
                    alert_url = i['generatorURL']
                except:
                    alert_url = "http://prometheus.qyvideo.net/alerts"
                try:
                    alert_job = i['labels']['job']
                except:
                    alert_job = "unkown job"
                try:
                    severity = i['labels']['severity']
                except:
                    severity = "p1"
                log.info(i)
                message = "[{}] {} \n\n**Labels** \n\n> alertname: {} \n\n" \
                          "> instance: {} \n\n> service: {} \n\n> job: {} \n\n>severity: {} \n\n**Annotations** \n\n" \
                          "> {} \n\n**Time** \n\n> {} " \
                    .format(alert_status, alert_name, alert_name, instances123,
                            service_name, alert_job, severity, summary123, startat)
                status = alert_data(message, summary123, profile_url)
                log.info(status)
                return status
            except Exception as e:
                log.error(repr(e))
                return repr(e)


# 发送数据
def alert_data(data, title, profile_url):
    headers = {'Content-Type': 'application/json'}
    # send_data = """{"msgtype": "markdown", "markdown": {"title": {} ,"text": {} }}""".format(title, data)
    send_data = '{"msgtype": "markdown","markdown": {"title": \"%s\" ,"text": \"%s\" }}' % (title, data)

    # type: str
    send_data = send_data.encode('utf-8')
    reps = requests.post(url=profile_url, data=send_data, headers=headers)
    return reps.text


if __name__ == '__main__':
    app.debug = 'false'
    app.run(host='0.0.0.0', port='8080')