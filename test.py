import os
import urllib
from random import randint

import requests

# 第一种方法
with open('cookies.txt','r',encoding='utf-8') as f:
    # print(f.read().split(';'))
    list = f.read().split(';')
cookie = {}
cookies = []
for line in list:
    key,value = line.split('=', 1)
    cookie[key] = value

print(cookie)
# import requests
# cookies = {'acw_tc': '3ad837a616487086295404758ee1be6a6e57291f1369548606e8ef0769', ' QCCSESSID': '7eb501d6de46b85efda5e8a9be', ' qcc_did': 'bc45da25-c566-4ba0-9dad-4c59bf637560', ' UM_distinctid': '17fdeb215dc20-0c8539ad16f90d-9771a3f-1fa400-17fdeb215dd112d', ' CNZZDATA1254842228': '1855149829-1648698510-https%253A%252F%252Fwww.qcc.com%252F%7C1648698510'}
# headers = {
#    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
#     'referer': 'https://www.qcc.com/weblogin?back=%2F'
#     }
# url = 'https://www.qcc.com/'
# res = requests.get(url=url, headers=headers, cookies=cookies)
# print(res)
# # cookie = requests.utils.dict_from_cookiejar(res.cookies)
# print(res.cookies)
# for
# time = randint(20,30)
