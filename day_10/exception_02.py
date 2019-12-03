# -*- coding: utf-8 -*-

# 예외처리 문법
# try : 
#   예외가 발생할 가능성이 있는 코드
# except : 
#   예외가 발생한 경우 처리 코드
# else :
#   예외가 발생하지 않은 경우의 실행코드
# finally :
#   예외의 발생 여부와 상관없이 실행되는 코드

n1 = int(input('1번째 정수 입력 : '))
n2 = int(input('2번째 정수 입력 : '))

try :
    r = n1 / n2
    print(f'r -> {r}')
except :
    print('예외가 발생했습니다.')
else :
    print('프로그램이 올바르게 실행되었습니다.')









