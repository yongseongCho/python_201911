# -*- coding: utf-8 -*-

# 소멸자
# 클래스의 객체가 소멸될 때, 자동으로 호출되는 메소드
# (생성자와 반대의 개념)

# 객체를 소멸시키는 방법
# del 객체변수명
# - 소멸자는 위의 명령에 의해서
#  객체가 소멸될 때 자동 호출됨

# 클래스 내부에 소멸자를 선언하는 방법
# def __del__(self) :
#   객체의 소멸 시, 수행할 작업(파일, DB 처리 작업)

class Food :
    def __init__(self, name) :
        self.name = name
        
    # 소멸자의 선언
    # Food 클래스의 객체가 소멸되기 직전
    # 자동으로 실행되는 메소드
    def __del__(self) :
        print(f'{self.name} 음식을 다 먹었습니다.')

f1 = Food('짜장면')
f2 = Food('치킨')
f3 = Food('돈까스')

# f1 객체의 소멸(삭제)
del f1
# f2 객체의 소멸(삭제)
del f2
# f3 객체의 소멸(삭제)
del f3







