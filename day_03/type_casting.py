# -*- coding: utf-8 -*-

# 파이썬 변수의 형변환

# 문자열 타입의 변수를 정수로 변환
# int 함수를 사용
str_1 = '15'
str_2 = '7'
str_sum = str_1 + str_2
print('{0} + {1} = {2}'.format(str_1,str_2,str_sum))

n_1 = int(str_1)    # str_1 문자열 값을 정수로 변환
n_2 = int(str_2)    # str_2 문자열 값을 정수로 변환
n_sum = n_1 + n_2
print('{0} + {1} = {2}'.format(n_1,n_2,n_sum))

str_1 = '15.7'
str_2 = '7.5'
str_sum = str_1 + str_2
print('{0} + {1} = {2}'.format(str_1,str_2,str_sum))

# 문자열 타입의 변수를 실수로 변환
# float 함수를 사용
n_1 = float(str_1)    # str_1 문자열 값을 실수로 변환
n_2 = float(str_2)    # str_2 문자열 값을 실수로 변환
n_sum = n_1 + n_2
print('{0} + {1} = {2}'.format(n_1,n_2,n_sum))

# 문자열 타입의 변수를 진리형 값으로 변환
# bool 함수를 사용
# - True / False 여부를 판단하지 않고
#   값의 존재 유무를 판단하여 
#  값이 있다면 True / 값이 없다면 False가 반환됨
bool_s1 = 'True'
bool_s2 = 'False'
bool_and = bool(bool_s1) and bool(bool_s2)
bool_or = bool(bool_s1) or bool(bool_s2)

print(bool_and)
print(bool_or)

n1 = 10
n2 = 20
# 문자열 결합은 문자열 사이에서만 허용됩니다.
# - 아래의 경우 에러가 발생
msg = n1 + ' + ' + n2 + ' = ' + n1 + n2
# str 함수를 사용하여 숫자타입을 문자열로 변환
msg = str(n1) + ' + ' + str(n2) + ' = ' + str(n1 + n2)
# 문자열 변수의 format 메소드를 사용하여 문자열을 생성
msg = '{0} + {1} = {2}'.format(n1, n2, n1 + n2)
# 포맷팅 문자열을 사용하여 문자열을 생성
# - 파이썬 3.6 이상에서만 가능
msg = f'{n1} + {n2} = {n1 + n2}'
print(msg)










