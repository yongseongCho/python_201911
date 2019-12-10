# -*- coding: utf-8 -*-

import pandas as pd

fname='./data/sales_2013.xlsx'

sales=pd.read_excel(fname,
                    sheet_name='january_2013',
                    header=3)

print(sales)

# Customer Name 컬럼의 값이
# J로 시작하는 고객의 정보를 출력하세요.
# - str 속성을 사용
result=\
sales[ sales['Customer Name'].str.startswith('J')]
print(result)




















