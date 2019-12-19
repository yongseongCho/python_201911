# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 사이킷런의 모든 예측기는 입력데이터의 형태를
# 2차원 배열로 가정하고 있기 때문에
# 전달할 입력데이터를 reshape를 통해서
# 형태를 변경
X=np.array([6, 8, 10, 14,   18]).reshape(-1, 1)
y=np.array([7, 9, 13, 17.5, 18.7])

# 회귀분석을 위한 머신러닝 클래스
# - 선형회귀 알고리즘을 기반으로 예측할 수 있는 클래스
# - 입력데이터 X와 라벨데이터 y에 대한 기울기 검색
# - 입력데이터 X와 라벨데이터 y에 대한 절편 검색
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X,y)

print('학습 데이터에 대한 평가 : ', model.score(X, y))

print('학습을 통해 찾아낸 기울기의 값 : ', model.coef_)
print('학습을 통해 찾아낸 절편의 값 : ', model.intercept_)

plt.figure(figsize=(7,7))
plt.title('Pizza Price DataSets(inch)')
plt.xlabel('inches')
plt.ylabel('prices')
plt.plot(X, y, 'ro')

plt.plot(X, model.predict(X), 'b--')

plt.axis([0,25,0,25])
plt.grid(True)
plt.show()












