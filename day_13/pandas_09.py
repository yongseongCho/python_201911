# -*- coding: utf-8 -*-

import pandas as pd

fname='./data/winequality-red.csv'

wine=pd.read_csv(fname, sep=';')

print(wine)
print(wine.info())

print(wine.quality.value_counts())

# 낮은 등급의 정보를 저장하고 있는
# 데이터프레임 변수 선언
low_quality = wine[wine.quality == 3]
print(low_quality.info())

# DataFrame 객체는 파일로 저장될 수 있습니다.
# - 다양한 포맷이 지원됨
# - 주의사항 : 데이터프레임의 인덱스 정보가 출력됨
low_quality.to_csv('./data/low_quality.csv')

# - 인덱스 정보를 제외하고 출력하는 예제
low_quality.to_csv('./data/low_quality.csv', index=False)

# - 구분문자를 , 가 아닌 다른 값을 수정하는 예제
low_quality.to_csv('./data/low_quality.csv', 
                   index=False, sep=';')

# - 헤더정보를 제외하고 저장하는 예제
low_quality.to_csv('./data/low_quality.csv', 
                   index=False, header=False)

# - 문자열 인코딩을 제어하여 저장하는 예제
low_quality.to_csv('./data/low_quality.csv', 
                   index=False, encoding='utf-8')












