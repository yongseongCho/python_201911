# -*- coding: utf-8 -*-

# pandas는 데이터 분석을 위해서
# 사용되는 파이썬 라이브러리 패키지
# 데이터의 간단한 통계 정보 및
# 시각화를 위한 다양한 기능을 제공
# - 손쉬운 파일 입출력
# - 다양한 파일 포맷을 지원(csv, 엑셀, 데이터베이스)

# 설치방법
# pip install pandas
# conda install pandas

import pandas as pd

# pandas의 데이터 저장 구조
# 1차원 : Series
# 2차원 : DataFrame
# 3차원 : Panel

series_data = list(range(1, 10, 2))

# 1차원으로 데이터를 저장하는 
# pandas Series 객체 생성
s = pd.Series(series_data)

print(f'type(s) -> {type(s)}')
print(s)











