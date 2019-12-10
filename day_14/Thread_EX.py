# -*- coding: utf-8 -*-

# Lotto 번호를 생성한 후,
# 출력하는 쓰레드 클래스를 작성하세요
# - run 메소드에서 로또 번호를 생성하여
#  출력하세요.

from threading import Thread
from random import random

class LottoThread (Thread) :
    def run(self) :
        # 6자리의 숫자
        # 1 ~ 45
        # 중복 X
        lotto_numbers = set()
        while len(lotto_numbers) < 6 :
            number = int(random() * 45 + 1)
            lotto_numbers.add(number)

        lotto_numbers = list(lotto_numbers)
        lotto_numbers.sort()
        print(lotto_numbers)

lottoes = []
limit = int(input('출력할 로또 개수를 입력 : '))

for i in range(1, limit+1) :    
    t = LottoThread()
    lottoes.append(t)

for t in lottoes :
    t.start()

for t in lottoes :
    t.join()

print('로또번호 생성 완료')


















