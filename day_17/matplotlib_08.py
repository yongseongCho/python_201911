# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

x1 = list(range(1, 101))
y1 = list(map(lambda x : x * 1.2, x1))

x2 = list(range(1, 101))
y2 = list(map(lambda x : x * 1.7, x2))

plt.title('matplotlib example')
plt.xlabel('x label')
plt.ylabel('y label')

# 다수개의 라인을 하나의 차트에 표현할
# 수 있음
plt.plot(x1, y1, '--r')
plt.plot(x2, y2, '-.g')

plt.show()











