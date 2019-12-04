# -*- coding: utf-8 -*-

str1 = 'Input : '

try :
    # ValueError
    number = int(input('숫자 입력 : '))
    # TypeError
    result = str1 + number
# try 영역 내부에서 
# ValueError가 발생된 경우 
# 실행되는 영역
# 에러(예외) 메세지를 전달받는 방법
# except 예외타입 as 변수명(메세지를 전달받을 변수) :
except ValueError as msg :
    print(f'예외가 발생했습니다 : {msg}')    
    result = '잘못된 입력'
# try 영역 내부에서 
# TypeError가 발생된 경우 
# 실행되는 영역
except TypeError as msg :
    print(f'예외가 발생했습니다 : {msg}')    
    result = '잘못된 타입 연산'
    
print(f'result -> {result}')





