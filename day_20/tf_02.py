# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

X_data=np.array([6, 8, 10, 14,   18])
y_data=np.array([7, 9, 13, 17.5, 18.7])

X=tf.placeholder(tf.float32, shape=[None])
y=tf.placeholder(tf.float32, shape=[None])

w = tf.Variable(0.0)
b = tf.Variable(0.0)

h = X * w + b

loss = tf.reduce_mean(tf.square(h - y))

optimizer=tf.train.GradientDescentOptimizer(
        learning_rate=0.0001)
train=optimizer.minimize(loss)

with tf.Session() as sess :
    # 세션을 사용하여 모든 변수를 초기화
    sess.run(tf.global_variables_initializer())

    # 텐서플로우의 X와 y에 값을 전달하기 위한 변수
    feed_dict = {X:X_data, y:y_data}
    
    for step in range(1, 1001) :
        sess.run(train, feed_dict=feed_dict)
        
        if step % 10 == 0 :
            # 손실 값을 반환
            loss_value = sess.run(
                    loss, feed_dict=feed_dict)
            # 손실 값을 출력
            print(f'{step} : {loss_value}')
    
    pred = sess.run(h, feed_dict=feed_dict)
    print(f'정답 : {y_data}')
    print(f'예측 : {pred}')
  








