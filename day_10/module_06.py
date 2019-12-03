# -*- coding: utf-8 -*-

# import 된 모듈 내부의 요소(변수, 함수, 클래스)에
# 접근하기 위해서는 모듈명을 사용해야만 합니다.
# 만약 모듈명이 너무 길거나 작성이 불편한 경우
# as 키워드를 사용하여 별칭을 지정할 수 있음
import module_05 as m

# number 변수의 값을 출력
print(m.number)
# func_05 함수의 실행
m.func_05()
# Class_05 클래스의 객체 생성 및 소멸
obj = m.Class_05()
del obj
