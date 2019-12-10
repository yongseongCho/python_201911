# -*- coding: utf-8 -*-

import pandas as pd

fname='./data/sales_2013.xlsx'

# - header 속성은 시트 내에
# 헤더정보가 위치하고 있는 행의 인덱스를 입력
# - nrows 속성은 읽어올 데이터 행의 개수
sales=pd.read_excel(fname,
                    sheet_name='january_2013',
                    header=3,
                    index_col=0,
                    nrows=3)

print(sales)









