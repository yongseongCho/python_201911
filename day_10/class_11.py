# -*- coding: utf-8 -*-

class Test :
    # 클래스 변수(모든 객체가 공유하는 변수)
    # 클래스 변수의 올바른 접근방법
    # 클래스명.클래스변수명
    # - Test.var
    var = '클래스 변수'
    
    # 생성자 선언
    # 인스턴스 변수의 생성 및 초기화 역할
    # 인스턴스 변수 : 각 객체마다 생성되는 변수
    # 모든 클래스의 메소드는 첫번째 매개변수로
    # 현재 메소드를 실행하는 객체를 참조하기 위한
    # self 를 선언해야만 합니다.
    def __init__(self) :
        self.var = '인스턴스 변수'

    def showInfo(self) :
        print(f'Test.var -> {Test.var}')
        print(f'self.var -> {self.var}')

# 클래스의 객체를 생성하는 방법
# 변수명 = 클래스명()
# (self 값은 자동으로 전달되기 때문에 작성할
# 필요가 없음 - 임의로 값을 전달하는 경우 에러)
obj = Test()

# (self 값은 자동으로 전달되기 때문에 작성할
# 필요가 없음 - 임의로 값을 전달하는 경우 에러)
obj.showInfo()










