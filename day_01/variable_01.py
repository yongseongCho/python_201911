# -*- coding: utf-8 -*-

# 변수
# 임의의 메모리 공간에 이름을 붙여 관리하는 방법
# 변수를 사용하여 프로그림이 진행되는 동안 처리되는 정보를
# 저장할 수 있습니다. (임시적 - 프로그램이 종료되면 사라짐)

# 파이썬 언어는 변수의 자료형을 지정하지 않습니다.

# 변수를 만드는 방법
# 변수명 = 값
# (변수명의 첫글자는 _ 또는 영문자로 작성합니다.)
num=100
print(num)

# 변수에 저장된 데이터의 타입을 확인하는 방법
# - type 함수
# - type(값 / 변수)
print(type(num))

""" 
파이썬에서 저장할 수 있는 데이터 타입
1. 정수형 - int
2. 실수형 - float
3. 문자열 - str
4. 진리형 - bool
 - 참과 거짓의 데이터
 - True, False
"""

var = 10
print(type(var))

var = 51.75
print(type(var))

var = "Hello"
print(type(var))

var = True
print(type(var))

var = False
print(type(var))




