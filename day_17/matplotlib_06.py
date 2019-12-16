# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

plt.rcParams['font.family']='NanumMyeongjo.ttf'
plt.rcParams['font.size']=17

x = list(range(1,6))
y = list(range(10,51,10))

# 그래프의 제목 설정
# title 함수를 사용
plt.title('matplotlib 예제')

# 그래프의 라벨 설정
# xlabel, ylabel 함수를 사용
plt.xlabel('x label')
plt.ylabel('y label')

plt.plot(x, y, 'k^')

plt.show()


























