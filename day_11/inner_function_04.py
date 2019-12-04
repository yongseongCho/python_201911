# -*- coding: utf-8 -*-

a = 10
b = 3

exStr = input('연산식을 입력하세요 : ')
print(exStr)

# eval 함수
# 문자열로 저장된 실행문의 처리 결과를
# 반환하는 함수
print(f'{exStr} = {eval(exStr)}')


