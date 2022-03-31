# -*- coding = utf-8 -*-
# @Time : 2022/3/27 21:09
# @Author : yaowei
# @File : dict_write.py
# @Software : PyCharm
# coding: utf-8
import pandas as pd
import openpyxl

result = [
    {'单位名称': '佳源科技股份有限公司', '统一社会信用代码': '91320115302570957C', '地址': '南京市雨花台区宁双路19号云密城7号楼14-17层',
     '详情页网址': 'https://www.qcc.com/firm/8a7ee9679a43308471a65a47d4844a4f.html'},
    {'单位名称': '中邮通建设咨询有限公司', '统一社会信用代码': '91320111135368160F', '地址': '南京市江北新区泰山街道浦园路7号',
     '详情页网址': 'https://www.qcc.com/firm/03a88dc6bb13128923ad133b6961b759.html'},
    {'单位名称': '中车南京浦镇车辆有限公司', '统一社会信用代码': '91320191663764650N', '地址': '南京市江北新区泰山园区浦珠北路68号',
     '详情页网址': 'https://www.qcc.com/firm/35341b7a8d8309f251c720ecdfd40d40.html'}
]
def wr(result):
    pf = pd.DataFrame(result)
    order = ['单位名称', '统一社会信用代码', '地址', '详情页网址']  # 指定列的顺序
    pf = pf[order]
    file_path = pd.ExcelWriter('企业信息.xlsx')  # 打开excel文件
    # 替换空单元格
    pf.fillna(' ', inplace=True)
    # 输出
    pf.to_excel(file_path, encoding='utf-8', index=False,sheet_name="sheet1")
    file_path.save()

# 写入excel
wb = openpyxl.Workbook
sh = wb.create_sheet('qiyexingxi')
wb.save('zz.xlsx')