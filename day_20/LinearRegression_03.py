# -*- coding: utf-8 -*-

import numpy as np

X=np.array([6, 8, 10, 14,   18]).reshape(-1, 1)
y=np.array([7, 9, 13, 17.5, 18.7])

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)

print('학습 데이터에 대한 평가 : ', model.score(X, y))

# LinearRegression 클래스의 비용(손실)함수
# (머신러닝 모델의 비용(손실)함수는 
# 머신러닝 모델의 학습 완성도를 판단하는 기준)
# (성능이 좋은 머신러닝 모델은 비용(손실)함수의 
# 결과가 작음)

# 잔차 : 훈련데이터(X)를 통해서 예측된 결과(predict)과 
# 실제 정답(y) 사이의 오차
# 일반적으로 머신러닝 모델의 손실함수는 모든 잔차들의 합계를
# 계산한 후, 평균을 취한 값을 손실의 값으로 정의

# 1. 예측 결과
predicted = model.predict(X)

# 2. 예측 결과와 실제 정답 사이의 오차를 계산한 후, 
# 제곱 연산한 결과를 반환
loss_merge = (predicted - y) ** 2

# 3. 제곱된 값의 합계를 계산한 후, 평균값을 반환
loss_avg = np.mean(loss_merge)

print('머신러닝 모델의 오차 : ', loss_avg)

# 평균제곱오차
# 평균제곱오차의 값을 반환하는 함수
# - mean_squared_error
from sklearn.metrics import mean_squared_error
print('머신러닝 모델의 평균제곱오차 : ', 
      mean_squared_error(y, predicted))















