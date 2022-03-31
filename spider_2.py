import pandas as pd
import requests
from urllib import parse
from bs4 import BeautifulSoup
import time
from csv import DictWriter

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
# def get_cookies(): #  通过访问主页获取cookie
#     headers = {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
#     }
#     url = "https://www.qcc.com/"
#     res = requests.get(url=url, headers=headers)
#     # print(res.headers)
#     return res.cookies

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
    soup = BeautifulSoup(res.text, 'lxml')
    print(soup)
    contents = {
        '统一社会信用代码': soup.select('tr:nth-child(1) > td:nth-child(2) > div > span.copy-value')[0].text,
        '企业名称': soup.select('tr:nth-child(1) > td:nth-child(4) > div > span.copy-value')[0].text.strip(), # cominfo > div:nth-child(2) > table > tr:nth-child(1) > td:nth-child(4) > div > span.copy-value
        '法定代表人': soup.select('tr:nth-child(2) > td.base-opertd > div > div > span.cont > span > span > a')[0].text.strip(), # tr:nth-child(2) > td.base-opertd > div > div > span.cont > span > span > a
        '曾用名': soup.select('tr:nth-child(7) > td:nth-child(6)')[0].text.replace('\n', '').strip().replace(' ', ''),
        '企业类型': soup.select('tr:nth-child(5) > td:nth-child(2)')[0].text.strip(),
        '所属行业': soup.select('tr:nth-child(6) > td:nth-child(2)')[0].text.strip(),
        '注册地址': soup.select('a.text-dk.copy-value')[0].text.strip().split(' ', 1)[0]
    }
    return contents


def getContents_2(url):
    res = requests.get(url=url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(res.text, 'lxml')
    # print(soup)

    contents = {
        '统一社会信用代码': soup.select(
            '#cominfo > div:nth-child(2) > table > tr:nth-child(1) > td:nth-child(2) > div > span.copy-value')[0].text,
        '企业名称': soup.select(
            '#cominfo > div:nth-child(2) > table > tr:nth-child(1) > td:nth-child(4) > div > span.copy-value')[
            0].text.strip(),
        # cominfo > div:nth-child(2) > table > tr:nth-child(1) > td:nth-child(4) > div > span.copy-value
        '法定代表人': soup.select(
            '#cominfo > div:nth-child(2) > table > tr:nth-child(2) > td.base-opertd > div > div > span.cont > span > span > a')[
            0].text.strip(),
        # cominfo > div:nth-child(2) > table > tr:nth-child(2) > td.base-opertd > div > div > span.cont > span > span > a
        '曾用名': soup.select('#cominfo > div:nth-child(2) > table > tr:nth-child(7) > td:nth-child(6)')[0].text.replace(
            '\n', '').strip(),  # cominfo > div:nth-child(2) > table > tr:nth-child(7) > td:nth-child(6)
        '企业类型': soup.select('#cominfo > div:nth-child(2) > table > tr:nth-child(5) > td:nth-child(2)')[0].text.strip(),
        # cominfo > div:nth-child(2) > table > tr:nth-child(5) > td:nth-child(2)
        '所属行业': soup.select('#cominfo > div:nth-child(2) > table > tr:nth-child(6) > td:nth-child(2)')[0].text.strip(),
        # cominfo > div:nth-child(2) > table > tr:nth-child(6) > td:nth-child(2)
        '注册地址': soup.select('#cominfo > div:nth-child(2) > table > tr:nth-child(9) > td:nth-child(2) > div')[
            0].text.strip().split(' ', 1)[0]
        # cominfo > div:nth-child(2) > table > tr:nth-child(9) > td:nth-child(2) > div
    }
    return contents


# cookies = get_cookies()
# cookies = {'acw_tc': '3ad837a616487086295404758ee1be6a6e57291f1369548606e8ef0769', ' QCCSESSID': '7eb501d6de46b85efda5e8a9be', ' qcc_did': 'bc45da25-c566-4ba0-9dad-4c59bf637560', ' UM_distinctid': '17fdeb215dc20-0c8539ad16f90d-9771a3f-1fa400-17fdeb215dd112d', ' CNZZDATA1254842228': '1855149829-1648698510-https%253A%252F%252Fwww.qcc.com%252F%7C1648698510'}
# cookies = {'QCCSESSID': '7eb501d6de46b85efda5e8a9be', ' qcc_did': 'bc45da25-c566-4ba0-9dad-4c59bf637560', ' UM_distinctid': '17fdeb215dc20-0c8539ad16f90d-9771a3f-1fa400-17fdeb215dd112d', ' CNZZDATA1254842228': '1855149829-1648698510-https%253A%252F%252Fwww.qcc.com%252F%7C1648702017', ' acw_tc': '3ad837a616487142723611862e19ec511eb43d94fdba57b9be7bb2451a'}
cookies = {'acw_tc': '3ad8379c16487156813944300e4a7de3ca6205938999c2c31ac1626434', ' QCCSESSID': '1859c2f1b4e8a31270aa78276e', ' MQCCSESSID': 'd7e094e04f474fb98aa4904e4e', ' qcc_did': '3a1b2704-a711-4641-8db0-f6a969d4e691', ' UM_distinctid': '17fdf2727363b5-046b233950d466-9771a39-1fa400-17fdf27273710eb', ' CNZZDATA1254842228': '1998958856-1648712817-https%253A%252F%252Fwww.qcc.com%252F%7C1648712817'}
# cookies = {'UM_distinctid': '17c64556c29a71-04defe5d6307ba-b7a1b38-1fa400-17c64556c2a100c', ' zg_294c2ba1ecc244809c552f8f6fd2a440': '%7B%22sid%22%3A%201637026518246%2C%22updated%22%3A%201637026518250%2C%22info%22%3A%201637026518248%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E4%BC%81%E6%9F%A5%E6%9F%A5%E7%BD%91%E7%AB%99%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22cn.bing.com%22%2C%22cuid%22%3A%20%22undefined%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201637026518246%7D', ' qcc_did': '6e92477e-ad83-4a9e-8cdf-a5657421d032', ' QCCSESSID': '381eabb18bdf2912f3c39cac44', ' zg_did': '%7B%22did%22%3A%20%2217c64556a72ca5-0c75115a11a1d8-b7a1b38-1fa400-17c64556a73e5a%22%7D', ' zg_d609f98c92d24be8b23d93a3e4b117bc': '%7B%22sid%22%3A%201648616057155%2C%22updated%22%3A%201648616057155%2C%22info%22%3A%201648516588898%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201648616057155%7D', ' acw_tc': '3ad7921a16487130105627071e76a2fcaba757300a46f88f1a499a9499', ' CNZZDATA1254842228': '557565422-1633766978-https%253A%252F%252Fwww.qcc.com%252F%7C1648712817'}
# print(cookies)
# cookies.txt = 'qcc_did=93869394-c8bf-4638-bc39-0fba12337cdd; UM_distinctid=17fac24b389644-0ff34c45aed19a-9771539-240000-17fac24b38a75c; QCCSESSID=a7177a247e40dfa8fd690a3e9b; acw_tc=3ad8379916486553394534936edf64dfbfad19ce8e4d5fc1077c2cfd0a; CNZZDATA1254842228=593471583-1647850686-https%253A%252F%252Fwww.google.com%252F%7C1648649887'
urls = []

names = ['佳源科技股份有限公司']
# names = ['江苏省建筑工程质量检测中心有限公司', '佳源科技股份有限公司']

# names = getNames()
contents = []
i = 1
for name in names:
    print(name)
    res = requests.get(url=urlEcode(name), headers=headers, cookies=cookies)
    # print(res.text)
    url_0 = getUlr(res)
    print('开始爬取第{}条数据'.format(i), url_0)
    # urls.append(url_0)
    print('waiting-------------------------20s')
    time.sleep(10) # 已验证15秒被封
    try:
        content = getContents_1(url_0)
    except IndexError as e:
        print('该企业为上市公司')
        content = getContents_2(url_0)
        print('新的方式抓取')
        print(f'爬取了第{i}条数据\n', content)
        print('writing data to csv')
        field_names = ['统一社会信用代码', '企业名称', '法定代表人', '曾用名', '企业类型', '所属行业', '注册地址']
        with open('1_1test.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames=field_names, dialect="excel")
            dictwriter_object.writerow(content)
            f_object.close()
        contents.append(content)
        pass

    print(f'爬取了第{i}条数据\n', content)
    print('writing data to csv')
    field_names = ['统一社会信用代码','企业名称','法定代表人','曾用名','企业类型','所属行业','注册地址']
    with open('1_1test.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=field_names, dialect="excel")
        dictwriter_object.writerow(content)
        f_object.close()
    contents.append(content)
    print('waiting for more-------------------------5s')
    i += 1


df = pd.DataFrame.from_dict(contents)
df.to_csv(r'test8.csv', index=False, header=True)





