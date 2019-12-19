# -*- coding: utf-8 -*-

# 파이선 언어에서 배열과 같은 형태의
# 데이터 처리를 위해 사용되는 모듈
# 일반적인 수치 계산에 관련된 기능을 제공
import numpy as np
import matplotlib.pyplot as plt

# X데이터를 이용하여 y 데이터를
# 예측하기 위한 함수
def linear_func(data) :
    # 1차방정식을 사용한 예측
    # -> 미지수X * 기울기 + 절편
    return data * 1.02758621 + 1.531034482758626

X=np.array([6, 8, 10, 14,   18])
y=np.array([7, 9, 13, 17.5, 18.7])

plt.figure(figsize=(7,7))
plt.title('Pizza Price DataSets(inch)')
plt.xlabel('inches')
plt.ylabel('prices')
plt.plot(X, y, 'ro')

plt.plot(X, linear_func(X), 'b--')

plt.axis([0,25,0,25])
plt.grid(True)
plt.show()












