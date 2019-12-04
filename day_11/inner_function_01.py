# -*- coding: utf-8 -*-

# 파이썬에서 제공하는 함수의 사용
# - 내장 함수
# : import 의 선언없이 사용할 수 있는 함수
# : print, input, open ...
# - 외장 함수
# : 특정 모듈을 import 해야만 사용할 수 있는 함

values = [1,2,3,4,5]
print(values)

# all 함수는 매개변수로 대입된 모든 값이
# 참인 경우 참을 반환하는 함수
# - 파이썬에서 참을 의미하는 값
# - False, 0, None 을 제외한 모든 값
print(all(values))

values = [1,2,3,False,5]
print(all(values))

values = [1,2,3,0,5]
print(all(values))

values = [1,2,3,None,5]
print(all(values))

value = None

# value 변수의 값이 None일 경우 실행하는
# if 문을 작성하세요
# - 파이썬의 None 값은 비교가 가능한 값 입니다.
if value == None :
    print('value 변수는 None값 입니다.')
else:
    print('value 변수는 None값이 아닙니다.')

# any 함수는 매개변수로 대입된 값 중,
# 하나라도 참인 경우 참을 반환하는 함수

values = [1,2,3,False,5]
print(any(values))

values = [1,2,3,0,5]
print(any(values))

values = [1,2,3,None,5]
print(any(values))

values = [0,False,None]
print(any(values))









