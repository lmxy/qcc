import pandas as pd

field_names = ['统一社会信用代码', '企业名称', '法定代表人', '曾用名', '企业类型', '所属行业', '注册地址']


df = pd.DataFrame(columns=field_names)

df.to_csv('1_1test.csv', index=False, encoding='utf-8')