import pandas as pd
import requests
from urllib import parse
from bs4 import BeautifulSoup
import time

# names = ['佳源科技股份有限公司', '凯易讯网络技术开发（南京）有限公司', '南京东大智能化系统有限公司']
headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
    }
names = []
with open('storage/names.txt', 'r', encoding="utf-8") as r:
    for line in r:
        names.append(line.strip('\n'))
# print(names)
# for name in names:
#     print(name)
def get_cookies(): #  通过访问主页获取cookie
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
    }
    url = "https://www.qcc.com/"
    res = requests.get(url=url, headers=headers)
    # print(res.headers)
    return res.cookies

def urlEcode(name):
    url_0 = 'https://www.qcc.com/web/search?key='
    name_code = parse.quote(name.encode('utf-8'))  # 中文转码为url代码
    url = url_0 + name_code
    print(url)
    return url

def getUlr(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    return soup.find(class_='title copy-value', href=True).attrs['href']

def getNames(): #  到指定路径处names.txt获得待查询企业
    names = []
    with open('storage/names.txt', 'r', encoding="utf-8") as r:
        for line in r:
            names.append(line.strip('\n'))
    # print(names)
    return names

def getContents_1(url):
    res = requests.get(url=url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    contents = {
        '统一社会信用代码': soup.select('tr:nth-child(1) > td:nth-child(2) > div > span.copy-value')[0].text,
        '企业名称': soup.select('tr:nth-child(1) > td:nth-child(4) > div > span.copy-value')[0].text.strip(),
        '法定代表人': soup.select('tr:nth-child(2) > td.base-opertd > div > div > span.cont > span > span > a')[0].text.strip(),
        '曾用名': soup.select('tr:nth-child(7) > td:nth-child(6)')[0].text.replace('\n', '').strip(),
        '企业类型': soup.select('tr:nth-child(5) > td:nth-child(2)')[0].text.strip(),
        '所属行业': soup.select('tr:nth-child(6) > td:nth-child(2)')[0].text.strip(),
        '注册地址': soup.select('a.text-dk.copy-value')[0].text.strip()
    }
    return contents


cookies = get_cookies()
print(cookies)
# cookies.txt = 'qcc_did=93869394-c8bf-4638-bc39-0fba12337cdd; UM_distinctid=17fac24b389644-0ff34c45aed19a-9771539-240000-17fac24b38a75c; QCCSESSID=a7177a247e40dfa8fd690a3e9b; acw_tc=3ad8379916486553394534936edf64dfbfad19ce8e4d5fc1077c2cfd0a; CNZZDATA1254842228=593471583-1647850686-https%253A%252F%252Fwww.google.com%252F%7C1648649887'
urls = []
i = 1
# names = ['佳源科技股份有限公司']
names = ['江苏省建筑工程质量检测中心有限公司', '佳源科技股份有限公司']

# names = getNames()

for name in names:
    print(name)
    res = requests.get(url=urlEcode(name), headers=headers, cookies=cookies)
    # print(res.text)
    url_0 = getUlr(res)
    print('开始爬取第{}条数据'.format(i), url_0)
    urls.append(url_0)
    print('waiting-------------------------30s')
    time.sleep(30) # 已验证3秒被封，30秒安然无恙，10秒被封，验证15秒
    i += 1

print(urls)
url = urls[0]
contents = []
for url in urls:
    content = getContents_1(url)
    contents.append(content)
    time.sleep(30)

df = pd.DataFrame.from_dict(contents)

print(df)

df.to_excel('企业基本信息.xlsx')