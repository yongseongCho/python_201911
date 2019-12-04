# -*- coding: utf-8 -*-

try :
    n1 = int(input('1번째 정수 : '))
    n2 = int(input('2번째 정수 : '))
    r = n1 / n2
    
    print(f'{n1} / {n2} = {r}')
# except 영역에 선언된 예외의 타입이 실제로 발생된
# 예외와 다르다면 예외를 처리할 수 없습니다.
except TypeError as msg :
    print(f'예외발생 : {msg}')