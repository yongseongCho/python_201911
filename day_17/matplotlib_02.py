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

# 선의 색상을 바꾸기 위한 방법
# plot 함수의 3번째 매개변수를 사용하여 변경
# r : 빨간색, b : 파란색, g : 초록색 등등
# (검정색 : k)
plt.plot(x, y, 'k')

plt.show()


























