# -*- coding: utf-8 -*-

import pandas as pd

fname='./data/sales_2013.xlsx'

sales=pd.read_excel(fname,
                    sheet_name='january_2013',
                    header=3)

print(sales)
print(sales.info())

# Purchase Date 컬럼의 값이 
# 2013-01-01 이거나 2013-01-31 인 
# 데이터를 추출하세요.
dates=['2013-01-01','2013-01-31']
# paddas의 Series 타입이 제공하는 
# isin 메소드
# - 리스트를 매개변수로 전달받아
# 해당 리스트 내부의 값과 일치하는 데이터를
# True로 반환하는 메소드
result=sales[
        sales['Purchase Date'].isin(dates)]
print(result)














