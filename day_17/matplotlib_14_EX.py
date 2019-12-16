# -*- coding: utf-8 -*-

# 임의의 로또번호를 생성(100개)
# - 생성된 로또번호는 리스트에 저장
# - [(1,2,3,4,5,6),(7,8,9,10,11,12)...]

from random import random

lotto_count = 100
lotto_numbers = []

for _ in range(lotto_count):
    # 로또 번호 생성
    lotto = set()
    while len(lotto) < 6 :
        lotto.add(int(random() * 45 + 1))
    # 생성된 로또 번호를 리스트로 변환
    lotto_ordered = list(lotto)
    # 로또 번호의 정렬
    lotto_ordered.sort()
    # 로또 번호를 리스트에 추가
    lotto_numbers.append(lotto_ordered)

print(lotto_numbers)

# 임의의 생성된 로또번호를 조사하여 
# 각 숫자의 빈도수를 Bar 차트로 출력
x = list(range(1,46))
y = [0] * 45

for lotto in lotto_numbers :
    for index in lotto :
        y[index-1] += 1
        
from matplotlib import pyplot as plt

plt.bar(x, y)
plt.show()


















