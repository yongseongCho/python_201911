# -*- coding: utf-8 -*-

import pandas as pd

# pandas를 사용하여 CSV 파일을 로딩한 후,
# DataFrame을 생성하는 방법
# - read_csv 함수
fname = './data/iris.csv'

iris = pd.read_csv(fname)

print(iris)

print(iris.info())

print(iris.describe())
















