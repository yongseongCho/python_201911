# -*- coding: utf-8 -*-

class Counter :
    # 클래스의 변수 선언
    # - 모든 객체가 공유하는 변수
    count = 0
    
    # 객체를 초기화하는 메소드
    def setObject(self) :
        # 각 객체의 멤버필드를 생성하는 코드
        # - 각각의 객체는 count 멤버를 가집니다.
        self.count = 1
        # 모든 객체가 공유하는 count 변수의 값을
        # 1 증가함
        Counter.count += 1
    
    def showInfo(self) :
        print(f'self.count -> {self.count}')
        print(f'Counter.count -> {Counter.count}')
        
c1 = Counter()
c1.setObject()

c1.showInfo()

c2 = Counter()
c2.setObject()

c2.showInfo()

c3 = Counter()
c3.setObject()

c3.showInfo()

# 클래스 변수인 Counter.count의 값이 
# 누적된 모습을 확인할 수 있음
# - 모든 객체가 Counter.count값이 3인 것을 확인
c1.showInfo()
c2.showInfo()
c3.showInfo()











