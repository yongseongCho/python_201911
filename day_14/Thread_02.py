# -*- coding: utf-8 -*-

from threading import Thread
# 실행의 흐름을 잠시 중지시킬 수 있는 sleep 함수
from time import sleep

class MyThread (Thread) :
    def run(self) :
        # 쓰레드의 이름을 확인하는 방법
        # - 쓰레드 클래스의 getName 메소드
        # - getName 메소드는 쓰레드의 이름을 반환
        for i in range(1,11) :
            print(f'{self.getName()} -> {i}')
            # sleep 함수
            # 매개변수 전달된 정수에 해당되는 초만큼
            # 현재 쓰레드의 실행을 중지하는 기능을 제공
            # (실수도 가능)
            # 1 -> 1초, 0.5 -> 0.5초
            sleep(1)

# Thread 클래스의 생성자에는 이름을 지정할 수 있는 매개변수가
# name으로 지정되어 있으며, name에 대입된 값이 해당 쓰레드의
# 이름이 됩니다. 쓰레드의 이름은 getName 메소드를 사용하여
# 확인할 수 있습니다.
t1 = MyThread(name='T1')
t2 = MyThread(name='T2')
t3 = MyThread(name='T3')

# 쓰레드 객체에 run 메소드를 호출하면 일반 메소드 호출과
# 동일하게 동작합니다.(흐름의 분기가 없음 - 단일흐름)
t1.run()
t2.run()
t3.run()












