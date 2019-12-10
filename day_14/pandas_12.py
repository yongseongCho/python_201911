# -*- coding: utf-8 -*-

import pandas as pd

fname='./data/sales_2013.xlsx'

sales=pd.read_excel(fname,
                    sheet_name='january_2013',
                    header=3)

print(sales)
print(sales.info())

# Sale Amount 컬럼의 값이 전체 Sale Amount의
# 평균 이상인 데이터만 출력하세요.
print('Sale Amount 컬럼의 평균 : ', 
      sales['Sale Amount'].mean())
result = sales[ 
        sales['Sale Amount']>=sales['Sale Amount'].mean()]
print('Sale Amount 컬럼의 평균 이상인 데이터 : \n',
      result)
      

















