# -*- coding: utf-8 -*-

import pandas as pd

# 엑셀 파일 Read, Write 모듈 설치
# pip install xlrd xlwt openpyxl

input_file = './data/sales_2013.xlsx'

# pandas 모듈을 활용한 엑셀 파일 로딩 처리
# pandas 모듈의 read_excel 함수
# read_excel(엑셀파일명, sheetname="읽어올sheet이름")
# - sheetname을 생략하는 경우 첫번째 시트가 선택됨
sales = pd.read_excel(input_file)
print(sales)

# DataFrame에 저장된 정보를 엑셀파일로 출력
output_file = './data/sales_2013_temp.xlsx'
# 엑셀 파일로 출력할 수 있는 개체 생성
writer = pd.ExcelWriter(output_file)
# DataFrame변수를 사용하여 Writer 객체에
# DataFrame의 내용을 출력
sales.to_excel(writer, sheet_name='1st Sheet')
# Writer 객체의 save 메소드를 호출하여
# 파일에 내용을 저장함
writer.save()
















