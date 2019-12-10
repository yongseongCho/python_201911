# -*- coding: utf-8 -*-

import pandas as pd

fname='./data/sales_2013.xlsx'

sales=pd.read_excel(fname,
                    sheet_name='january_2013',
                    header=3)

print(sales)

print(sales[['Invoice Number','Sale Amount','Purchase Date']])

# pandas dataframe 의 iloc 메소드
# iloc[ 행의 정보(시작인덱스:종료인덱스) , [열의 정보] ]
# - 행을 제어하는 경우
print(sales.iloc[0:2])
# - 전체 행에서 열을 제어하는 경우
print(sales.iloc[:,2:])
# - 전체 행에서 열을 제어하는 경우
# (열의 정보가 연속되지 않은 경우)
print(sales.iloc[:,[0,2,3]])














