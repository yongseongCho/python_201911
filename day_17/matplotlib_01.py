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

# plot 메소드는 매개변수로 전달된 
# 두개의 리스트 타입을 사용하여 
# 선을 그리는 메소드
plt.plot(x, y)

# show 메소드는 화면에 표시하는 메소드
plt.show()


























