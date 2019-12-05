# -*- coding: utf-8 -*-

numbers = []
for i in range(5) :
    numbers.append(int(input(f'{i+1}번째 정수 : ')))

print(numbers)

import pickle

# pickle 모듈
# 파이썬의 변수를 외부로 출력(저장)하는 기능
# - 변수 자체를 저장
# 외부에 출력된 변수를 불러(복원)들이는 기능
# - 변수의 복원

f = open('numbers.dat', 'wb')

pickle.dump(numbers, f)
f.close()











