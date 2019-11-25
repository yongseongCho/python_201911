# -*- coding: utf-8 -*-

# 제어문
# 실행문의 실행 여부 및 반복 실행을 제어할 수 있는 문법

# if문 : 특정 조건의 True, False 여부에 따라 실행문의
# 실행을 결정할 수 있는 문법
"""
if 조건식(참과 거짓으로 분리되는 식) :
    실행문
    ...
"""

# 제어문을 사용하지 않은 코드
# - 제어문이 포함되징 않은 코드는 항상 실행
number = 17
print(f'number -> {number}')

# number 변수가 저장하고 있는 값이
# 홀수 인 경우 홀수, 짝수인 경우 짝수로 출력하세요.

if number % 2 == 1 :
    print('홀수')
    
if number % 2 == 0 :
    print('짝수')

# jumin 변수의 값을 참조하여
# 성별을 출력하세요.
jumin = '901212-2033987'

gender_code=jumin[7]
gender_code=jumin.split('-')[1][0]

if gender_code == '1' or gender_code == '3' :
    print('남성입니다.')
    
if gender_code == '2' or gender_code == '4' :
    print('여성입니다.')














