import os

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl
from urllib.request import urlopen

path = 'drive/chromedriver.exe'
# url = 'https://www.qcc.com/'
stores = {}
# name = '艾德克斯电子（南京）有限公司'


# def wr(result):
#     pf = pd.DataFrame(result)
#     order = ['单位名称', '统一社会信用代码', '地址', '详情页网址']  # 指定列的顺序
#     pf = pf[order]
#     file_path = pd.ExcelWriter('企业信息.xlsx')  # 打开excel文件
#     # 替换空单元格
#     pf.fillna(' ', inplace=True)
#     # 输出
#     pf.to_excel(file_path, encoding='utf-8', index=False,sheet_name="sheet1")
#     file_path.save()

def wr(result):
    pf = pd.DataFrame(result)
    order = ['单位名称']  # 指定列的顺序
    pf = pf[order]
    file_path = pd.ExcelWriter('企业信息.xlsx')  # 打开excel文件
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False,sheet_name="sheet1")
    file_path.save()

def list():
    list = os.listdir('C:\\Users\\Administrator\\Desktop\\数据整理\\表内名称重命名')
    new_list = []

    for name in list:
        new_name = name.split('.', 1)[0]
        new_list.append(new_name)

    return new_list

def get_data(name):
    url = 'https://www.qcc.com/'
    cookie = {'QCCSESSID': '7eb501d6de46b85efda5e8a9be', ' qcc_did': 'bc45da25-c566-4ba0-9dad-4c59bf637560',
               ' UM_distinctid': '17fdeb215dc20-0c8539ad16f90d-9771a3f-1fa400-17fdeb215dd112d',
               ' CNZZDATA1254842228': '1855149829-1648698510-https%253A%252F%252Fwww.qcc.com%252F%7C1648702017',
               ' acw_tc': '3ad837a616487142723611862e19ec511eb43d94fdba57b9be7bb2451a'}

    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"')
    options.add_argument('--disable-gpu')
    # options.add_argument('cookie: QCCSESSID=7eb501d6de46b85efda5e8a9be; qcc_did=bc45da25-c566-4ba0-9dad-4c59bf637560; UM_distinctid=17fdeb215dc20-0c8539ad16f90d-9771a3f-1fa400-17fdeb215dd112d; acw_tc=3ad837a616487142723611862e19ec511eb43d94fdba57b9be7bb2451a; CNZZDATA1254842228=1855149829-1648698510-https%253A%252F%252Fwww.qcc.com%252F%7C1648712817')
    driver = webdriver.Chrome(executable_path=path, options=options) # Windows
    driver.add_cookie(cookie_dict=cookie)
    driver.implicitly_wait(3)
    driver.get(url)

    element = driver.find_element(By.ID, 'searchKey')
    element.send_keys(name)
    print('已输入查询企业名称', name)

    browser_from = driver.find_element(By.CLASS_NAME, 'input-group-btn')
    # time.sleep(2)
    browser_from.click()
    time.sleep(1)
    url_0 = driver.current_url
    print('点击查询后', url_0)
    driver.get(url_0)
    print('已打开详情页面')

    content = driver.find_element(By.CSS_SELECTOR, 'body > div > div.app-search > div.container.m-t > div.adsearch-list > div > div.msearch > div > table > tr:nth-child(1) > td:nth-child(3)')
    # content_name = driver.find_element(By.CSS_SELECTOR, 'body > div > div.app-search > div.container.m-t > div.adsearch-list > div > div.msearch > div > table > tr:nth-child(1) > td:nth-child(3) > div > div.app-copy-box.copy-hover-item > span.copy-title > a')
    # # print('get new url_1', content_a.get_attribute('href'))
    # # print('get new url_1', content_a.get_attribute('href'))
    # content_num = driver.find_element(By.CSS_SELECTOR, 'body > div > div.app-search > div.container.m-t > div.adsearch-list > div > div.msearch > div > table > tr.frtrt.tsd0 > td:nth-child(3) > div > div.relate-info > div.rline.over-rline > span:nth-child(4) > span > div > span.copy-value')
    # # print(content_num.text)
    # content_address = driver.find_element(By.CSS_SELECTOR, 'body > div > div.app-search > div.container.m-t > div.adsearch-list > div > div.msearch > div > table > tr.frtrt.tsd0 > td:nth-child(3) > div > div.relate-info > div:nth-child(3) > span > div > span.copy-value')
    # # content_url = content_name.get_attribute('href')
    print(content.text)
    yield {
        "单位名称": content.text
    }

def main():
    # lis = list()
    # for name in lis:
    name = '南京高达软件有限公司'
    try:
        contents = get_data(name)
        # break
    except Exception as e:
        print(name, e)
        pass
    else:
        # j = 0
        for i in contents:
            print(i)
            stores.update(i)

    print(stores)





if __name__ == '__main__':
    main()

