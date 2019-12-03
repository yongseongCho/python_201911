# -*- coding: utf-8 -*-

class Animal :
    def __init__(self, name, age, color) :
        self.name = name
        self.age = age
        self.color = color

class Dog (Animal) :
    pass

class Cat (Animal) :
    pass

# Dog, Cat 클래스의 객체를 생성하려면
# 부모로부터 물려받은 생성자의 매개변수를
# 전달해야합니다.
    
# 자식클래스 Dog 클래스의 객체 생성
d = Dog('바둑이', 10, '흰색')
# 자식클래스 Cat 클래스의 객체 생성
c = Cat('나비', 3, '검은색')











