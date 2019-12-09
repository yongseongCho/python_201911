# -*- coding: utf-8 -*-

import pandas as pd

# 엑셀 파일 Read, Write 모듈 설치
# pip install xlrd xlwt
# pip install openpyxl

fname='sales_2013.xlsx'
sales=pd.read_excel(fname)