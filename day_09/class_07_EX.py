# -*- coding: utf-8 -*-

class Calculator :
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        # 연산의 결과를 저장하는 변수
        self.r = None
        
    def plus(self) :
        self.r = self.n1 + self.n2
        # 출력을 위한 멤버 메소드의 호출
        self.showResult('+')
    
    def minus(self) :
        self.r = self.n1 - self.n2
        # 출력을 위한 멤버 메소드의 호출
        self.showResult('-')
        
    def showResult(self, op) :
        print(f'{self.n1} {op} {self.n2} = {self.r}')

# 생성자를 활용한 객체의 생성
calculator = Calculator(10, 5)

# 멤버 메소드의 사용
calculator.plus()   # 10 + 5 = 15
calculator.minus()   # 10 - 5 = 10





