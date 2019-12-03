# -*- coding: utf-8 -*-

class Animal :
    def __init__(self, name, age, color) :
        self.name = name
        self.age = age
        self.color = color
    def showInfo(self) :
        print(f'name : {self.name}')
        print(f'age : {self.age}')
        print(f'color : {self.color}')    

# 생성자 재정의(오버라이딩)를 통한
# 상속 문법 구현
class Dog (Animal) :
    def __init__(self, name, age, color, power) :
        # 자식클래스에서 부모클래스의 생성자를 
        # 사용하지 않고 새롭게 생성자를 정의하는 경우
        # 부모클래스의 생성자를 명시적으로 호출하여
        # 부모클래스의 인스턴스 변수들이 올바르게
        # 생성될 수 있도록 해야합니다.
        self.power = power
        
        # super() 함수는 부모클래스에 접근하기 위한
        # 참조값을 반환하는 함수
        # 1. 부모 클래스의 생성자 호출
        # 2. 오버라이딩된 부모클래스의 메소드 호출
        super().__init__(name, age, color)
    
    # 부모클래스로부터 물려받은 showInfo 메소드는
    # power 값을 출력할 수 없음
    # 이러한 경우 부모클래스를 새롭게 재정의하여
    # 사용할 수 있습니다. (메소드 오버라이딩)
    # 메소드 오버라이딩을 구현하면 부모의 메소드는
    # 무시되고 오버라이딩된 자식클래스의 메소드가
    # 호출됩니다.
    def showInfo(self) :
        # super()를 사용하여 부모클래스의 
        # 오버라이딩된 메소드를 호출할 수 있습니다.
        super().showInfo()
        print(f'power : {self.power}')   

class Cat (Animal) :
    def __init__(self, name, age, color, speed) :
        super().__init__(name, age, color)
        self.speed = speed
    def showInfo(self) :
        super().showInfo()
        print(f'speed : {self.speed}')   
        
d = Dog('바둑이', 10, '흰색', 
        '무는힘이 아주 강해요...')
c = Cat('나비', 3, '검은색', 
        '너무 빨라서 잡을수가 없어요...')

d.showInfo()
c.showInfo()


















