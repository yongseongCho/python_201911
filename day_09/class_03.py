# -*- coding: utf-8 -*-

class Person :
    # 클래스 변수
    # 클래스 변수는 클래스 내부에 선언된 변수로써
    # 모든 객체들이 공유하게 되는 변수입니다.
    # 클래스 변수는 단 하나만 생성되며, 모든 객체들은
    # 클래스이름.클래스변수명 으로 접근할 수 있습니다.
    # 만약 클래스변수명과 동일한 인스턴스 변수가 없다면
    # self.클래스변수명 으로 값을 꺼내올수 있습니다.
    name = "Person Class's Name"
    age = "Person Class's Age"
    
    def setInfo(self, n, a) :
        # 인스턴스 변수의 생성 코드
        # 인스턴스 변수는 해당 클래스의 각 객체마다
        # 별도로 생성되는 변수
        # (모든 객체가 공유하지 않음)
        # 인스턴스 변수를 생성하기 위해서
        # self.인스턴스변수명 = 값
        self.name = n
        self.age = a
        
        # 클래스 변수에 명시적으로 접근하기 위해서는
        # 클래스명.클래스변수명
        Person.name = 'Global Name'
        Person.age = 'Global Age'
        
    def showInfo(self) :
        print(f'name -> {self.name}')
        print(f'age -> {self.age}')

p1 = Person()
p2 = Person()

p1.showInfo()
p2.showInfo()

print('=' * 20)

p1.setInfo('A', 11)

p1.showInfo()
p2.showInfo()










