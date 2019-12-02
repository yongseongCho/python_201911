# -*- coding: utf-8 -*-

class Food :
    # 인스턴스 변수의 생성을 위한 메소드
    # 메소드를 통한 인스턴스 생성은
    # 사용자에 의해서 호출되지 않으면
    # 인스턴스 변수들이 생성되지 않기때문에
    # 위험한 접근방식입니다.
    # (생성자를 통한 접근을 해야만 에러를 
    # 줄일 수 있음)
    def init(self, name, price) :
        self.name = name
        self.price = price
        
    def showInfo(self) :
        print(f'음식명 : {self.name}', end=', ')
        print(f'가격 : {self.price}원')

f1 = Food()
f1.init('짜장면', 6000)
f1.showInfo()

f2 = Food()
f2.showInfo()












