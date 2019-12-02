# -*- coding: utf-8 -*-

# 객체지향과 정보은닉

# 클래스 멤버의 접근지정자
# - 객체지향의 정보은닉의 개념을 구현

# __ 를 활용한 접근이 제한된 인스턴스 변수 선언
# __변수명 으로 정의할 수 있으며, 외부에서 접근할 수
# 없는 인스턴스 변수를 선언할 수 있음
# 값을 접근할 수 없고, 값을 수정할 수 없음
# __ 가 선언된 변수는 되도록 외부에서 접근하지 않도록
# 주의해야함.

class Account :
    def __init__(self) :
        self.__balance = 0
    def deposit(self, money) :
        self.__balance += money
    def withdraw(self, money) :
        self.__balance -= money
    def showInfo(self) :
        print(f'현재 잔액은 {self.__balance}원 입니다.')
# 계좌 생성  
account = Account()
# 입금
account.deposit(100000)
# 잔고 확인
account.showInfo()
# 출금
account.withdraw(90000)
# 잔고 확인
account.showInfo()

# 클래스의 은닉된 멤버필드의 값을
# 수정할 수 없습니다.
account.__balance = 100000000

# 잔고 확인
account.showInfo()






