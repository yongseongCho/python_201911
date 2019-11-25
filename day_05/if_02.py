# -*- coding: utf-8 -*-

# input 함수
# 기본 입력(키보드)을 처리할 수 있는 함수
# 변수명 = input("Message")
# Message가 화면에 출력이 되고, 키보드로 입력된 정보가
# '문자열'로 변수에 대입됨

number = input('숫자를 입력하세요 : ')
print(f'입력된 숫자는 {number} 입니다')

# input 함수를 통해서 대입된 데이터는 
# 문자열 타입입니다.(str)
print(f"number's type : {type(number)}")

# 문자열을 정수로 변환
number = int(number)

if number % 2 == 1 :
    print('홀수')
    
if number % 2 == 0 :
    print('짝수')









