# -*- coding: utf-8 -*-

class Calculator :
    def __init__(self) :
        # 아래의 코드는 숫자가 입력되지 않는 경우
        # 예외가 발생합니다.
        # 예외처리를 활용하여 숫자가 들어올때까지
        # 값을 입력받도록 수정하세요.
        while True :
            self.n1 = input('첫번째 정수 : ')
            try :
                self.n1 = int(self.n1)
            except :
                # 예외가 발생한 경우
                print(f'{self.n1}은 숫자타입이 아닙니다.')
            else :
                # 예외가 발생하지 않은 경우
                # - 올바르게 입력된 경우 반복을 종료
                break
        
        while True :
            self.n2 = input('두번째 정수 : ')
            try :
                self.n2 = int(self.n2)
            except :                
                print(f'{self.n2}은 숫자타입이 아닙니다.')
            else :
                break
        
        self.r = None
    def plus(self) :
        self.r = self.n1 + self.n2
        self.display('+')
    def minus(self) :
        self.r = self.n1 - self.n2
        self.display('-')
    def display(self, op) :
        print(f'{self.n1} {op} {self.n2} = {self.r}')
        
cal = Calculator()
cal.plus()
cal.minus()







