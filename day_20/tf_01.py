# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
print(tf.__version__)

X_data=np.array([6, 8, 10, 14,   18])
y_data=np.array([7, 9, 13, 17.5, 18.7])

# 1. 데이터를 전달받기 위한 실행매개변수 선언
X=tf.placeholder(tf.float32, shape=[None])
y=tf.placeholder(tf.float32, shape=[None])

# 2. 학습을 통해 갱신할 변수 텐서의 선언
# - 텐서플로우가 실행되는동안 지속적으로
# 값을 갱신(학습)하기 위한 기울기와 절편의 
# 변수를 선언
w = tf.Variable(0.0)
b = tf.Variable(0.0)

# 3. 머신러닝/딥러닝의 가설 선언
# - scikit-learn의 예측기 클래스가 제공하는
#   predict 메소드의 값을 생성할 수 있는 식 
# - 문제 해결을 위한 식
h = X * w + b

# 4. 손실(오차)의 값을 계산할 수 있는 식을 선언
# - 선형회귀에서의 오차 계산
# - 평균제곱오차
# - 실제 정답과 예측한 값의 차를 제곱하여 
#   평균을 계산하는 방식

# - 텐서플로우의 square 함수를 사용하여
# 실제 정답과 예측 값의 차를 제곱
# - 텐서플로우의 reduce_mean 함수를 사용하여
# 제곱된 오차의 평균을 계산
loss = tf.reduce_mean(tf.square(h - y))

# 5. 경사하강법 객체의 선언과 손실의 값을
# 줄여나가는 방향으로 학습을 할 수 있는 텐서 선언

# - 학습을 위한 경사하강법 구현 객체 텐서
# - tf.train.GradientDescentOptimizer 클래스
optimizer=tf.train.GradientDescentOptimizer(
        learning_rate=0.0001)

# 경사하강법 객체를 사용하여 loss의 값이 
# 줄어들 수 있도록 학습을 진행할 텐서를 생성
train=optimizer.minimize(loss)

# 텐서플로우를 실행하기 위한
# 세션 변수의 선언
sess = tf.Session()

# 세션을 사용하여 모든 변수를 초기화
sess.run(tf.global_variables_initializer())

# 텐서플로우의 X와 y에 값을 전달하기 위한 변수
feed_dict = {X:X_data, y:y_data}

# 기울기와 절편을 사용하여 값을 예측
pred = sess.run(h, feed_dict=feed_dict)

# 예측된 값을 출력
print(pred)

# 손실 값을 반환
loss_value = sess.run(loss, feed_dict=feed_dict)

# 손실 값을 출력
print(loss_value)

# 학습을 진행하여 손실의 값이 줄어들도록
# 제어하는 코드(경사하강법 객체를 실행)
sess.run(train, feed_dict=feed_dict)

# 손실 값을 반환
loss_value = sess.run(loss, feed_dict=feed_dict)

# 손실 값을 출력
print(loss_value)

sess.run(train, feed_dict=feed_dict)

# 손실 값을 반환
loss_value = sess.run(loss, feed_dict=feed_dict)

# 손실 값을 출력
print(loss_value)

sess.run(train, feed_dict=feed_dict)

# 손실 값을 반환
loss_value = sess.run(loss, feed_dict=feed_dict)

# 손실 값을 출력
print(loss_value)









