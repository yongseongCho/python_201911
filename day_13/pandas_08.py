# -*- coding: utf-8 -*-

import pandas as pd

fname='./data/winequality-red.csv'

# CSV파일의 구분문자가 다른 경우
# - read_csv 함수의 sep 매개변수를 조정하여 
# 처리할 수 있음
wine=pd.read_csv(fname, sep=';')

print(wine)
print(wine.info())










