# -*- coding: utf-8 -*-

from threading import Thread
from time import sleep
# 파이썬에서 제공하는 난수에 관련된 모듈
# 난수 : 0 ~ 1 사이의 임의의 수
from random import random

class RandomArrive (Thread) :
    def __init__(self, name) :
        # 부모클래스 Thread의 생성자를 통한
        # 쓰레드의 이름 설정
        super().__init__(name=name)
    def run(self) :
        # _의 의미는 전달되는 값을
        # 사용하지 않겠다는 의미
        for _ in range(10) :
            # random 모듈의 random 함수는 난수를 반환합니다.
            # (0~1 사이의 값 반환 - float)
            # 1 ~ 10 사이의 수가 반된되도록 제어
            sleep_time = int(random() * 10 + 1)
            sleep(sleep_time)
            
        print(f'{self.getName()}님 도착!!')

clients = []
limit = int(input('참여자 수를 입력 : '))

for i in range(1, limit+1) :
    name = input(f'{i}번째 참여자 이름 : ')
    t = RandomArrive(name)
    clients.append(t)

for t in clients :
    t.start()















