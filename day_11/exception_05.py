# -*- coding: utf-8 -*-

try :
    n1 = int(input('1번째 정수 : '))
    n2 = int(input('2번째 정수 : '))
    r = n1 / n2
    
    print(f'{n1} / {n2} = {r}')
# 예외의 타입 짐작하지 못하는 경우 모든 예외를 처리할
# 수 있는 Exception 타입으로 예외를 처리할 수 있습니다.
# - Exception은 모든 예외의 최상위 부모클래스 타입입니다.
except Exception as msg :
    print(f'예외발생 : {msg}')