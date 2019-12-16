# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

x = list(range(1,6))
y = list(range(10,51,10))

plt.title('matplotlib example')

plt.xlabel('x label')
plt.ylabel('y label')

plt.plot(x, y, 'b--')

# 그래프의 구간 확대 및 축소 방법
# xlim, ylim 함수를 사용
# xlim(x축의 최소값, x축의 최대값)
# ylim(y축의 최소값, y축의 최대값)
plt.xlim(2,4)
plt.ylim(20, 35)

plt.show()


























