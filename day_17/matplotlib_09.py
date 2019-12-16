# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

x1 = list(range(1, 101))
y1 = list(map(lambda x : x * 1.2, x1))

x2 = list(range(1, 101))
y2 = list(map(lambda x : x * 1.7, x2))

plt.title('matplotlib example')
plt.xlabel('x label')
plt.ylabel('y label')

# 여러 라인을 하나의 그래프에 출력하는 경우
# 각 라인을 구분하기 위한 legend 출력 방법
# 1. plot 함수의 label 매개변수를 설정
# - 각 라인의 제목
# 2. legend 함수의 loc 매개변수를 설정하여
# 어느 위치에 출력할 것인지 지정 
plt.plot(x1, y1, '--r', label='first')
plt.plot(x2, y2, '-.g', label='second')

plt.legend(loc='upper left')

plt.show()











