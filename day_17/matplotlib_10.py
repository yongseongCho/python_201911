# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

x1 = list(range(1, 101))
y1 = list(map(lambda x : x * 1.2, x1))

x2 = list(range(1, 101))
y2 = list(map(lambda x : x * 1.7, x2))

plt.title('matplotlib example')
plt.xlabel('x label')
plt.ylabel('y label')

# 다수개의 그래프를 생성하는 경우
# 서브플롯 설정 방법
# subplot 함수를 사용
# subplot(행,열,위치)
# subplot(행열위치) -> , 없이 사용할 수 있음
plt.subplot(2,2,1)
plt.plot(x1, y1, '--r', label='first')
plt.legend(loc='upper left')

plt.subplot(224)
plt.plot(x2, y2, '-.g', label='second')
plt.legend(loc='upper left')

plt.show()











