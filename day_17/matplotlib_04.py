# -*- coding: utf-8 -*-

# matplotlib
# 파이썬에서 데이타를 차트나 플롯(Plot)을 
# 그려주는 라이브러리 패키지
# 범용적으로 가장 많이 사용되는 데이타 시각화
# (Data Visualization) 패키지

# 홈페이지
# https://matplotlib.org 

from matplotlib import pyplot as plt

x = list(range(1,6))
y = list(range(10,51,10))

# 그래프의 제목 설정
# title 함수를 사용
plt.title('matplotlib example')

# 그래프의 라벨 설정
# xlabel, ylabel 함수를 사용
plt.xlabel('x label')
plt.ylabel('y label')

plt.plot(x, y, 'k^')

plt.show()


























