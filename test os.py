from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = 'https://www.qcc.com/'
cookie = {'QCCSESSID': '7eb501d6de46b85efda5e8a9be', ' qcc_did': 'bc45da25-c566-4ba0-9dad-4c59bf637560',
          ' UM_distinctid': '17fdeb215dc20-0c8539ad16f90d-9771a3f-1fa400-17fdeb215dd112d',
          ' CNZZDATA1254842228': '1855149829-1648698510-https%253A%252F%252Fwww.qcc.com%252F%7C1648702017',
          ' acw_tc': '3ad837a616487142723611862e19ec511eb43d94fdba57b9be7bb2451a'}

options = webdriver.ChromeOptions()
options.add_argument(
    'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"')
options.add_argument('--disable-gpu')
# options.add_argument('cookie: QCCSESSID=7eb501d6de46b85efda5e8a9be; qcc_did=bc45da25-c566-4ba0-9dad-4c59bf637560; UM_distinctid=17fdeb215dc20-0c8539ad16f90d-9771a3f-1fa400-17fdeb215dd112d; acw_tc=3ad837a616487142723611862e19ec511eb43d94fdba57b9be7bb2451a; CNZZDATA1254842228=1855149829-1648698510-https%253A%252F%252Fwww.qcc.com%252F%7C1648712817')
driver = webdriver.Chrome(executable_path='drive/chromedriver.exe', options=options)  # Windows
driver.get(url)
driver.add_cookie(cookie_dict=cookie)
driver.implicitly_wait(3)
# driver.get(url)
time.sleep(500)
