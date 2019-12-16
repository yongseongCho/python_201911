# -*- coding: utf-8 -*-

# 각 구구단의 결과를 서브플롯을 사용하여
# 출력하는 예제
from matplotlib import pyplot as plt

x = list(range(1,10))
y = []

for dan in range(2, 10) :
    y.append([])    
    for mul in range(1, 10) :
        y[-1].append(dan*mul)

plt.title('GuGuDan Chart!')

for i, data in enumerate(y) :
    plt.subplot(3,3,i+1)
    plt.plot(x, data, '--r', 
             label=f'{i+2} Dan')
    plt.legend(loc='best')

plt.show()









