# -*- coding: utf-8 -*-

class Food :
    
    # 클래스의 생성자
    # __init__ 메소드
    # 클래스의 생성자는 클래스의 객체 생성시
    # 자동으로 호출되는 메소드
    # 각 객체가 생성될 때마다 실행됨
    # 생성자에서 필요한 매개변수를 객체 
    # 생성 시 전달하지 않으면 에러가 발생
    def __init__(self, name, price) :
        self.name = name
        self.price = price
        
    def showInfo(self) :
        print(f'음식명 : {self.name}', end=', ')
        print(f'가격 : {self.price}원')

# 생성자에 필요한 매개변수가 전달되지 않으므로
# 에러가 발생하는 코드
# f1 = Food()

# 생성자를 통한 객체 초기화 코드
# - 클래스의 생성자 __init__ 메소드는
# 클래스먕() 로 호출할 수 있습니다.
# - 반드시 생성자에 정의된 모든 매개변수가
# 전달되어야만 객체가 생성됩니다.
f1 = Food('짜장면', 6000)
f1.showInfo()












