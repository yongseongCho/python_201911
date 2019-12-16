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

# 출력 그래프의 크기 조정
# figure 함수의 figsize를 이용
# figure(figsize=(가로길이,세로길이))
plt.figure(figsize=(12,7))

plt.title('GuGuDan Chart!')

for i, data in enumerate(y) :
    plt.subplot(3,3,i+1)
    plt.plot(x, data, '--r', 
             label=f'{i+2} Dan')
    plt.legend(loc='best')

plt.show()









