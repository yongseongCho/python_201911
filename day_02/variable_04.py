# -*- coding: utf-8 -*-

# 논리연산자
# 다수개의 관계식의 결과를 조합하여 하나의 
# bool 값으로 반환하는 연산자
# AND, OR, NOT

# and 연산자
# 좌항과 우항의 관계식이 모두 참인 경우 
# True 를 반환하는 연산자
r = False and False
print('{0} {1} {2} = {3}'.format(
        False, 'and', False, r))

r = False and True
print('{0} {1} {2} = {3}'.format(
        False, 'and', True, r))

r = True and False
print('{0} {1} {2} = {3}'.format(
        True, 'and', False, r))

r = True and True
print('{0} {1} {2} = {3}'.format(
        True, 'and', True, r))

# or 연산자
# 좌항과 우항의 관계식 중 하나라도 참인 경우 
# True 를 반환하는 연산자
r = False or False
print('{0} {1} {2} = {3}'.format(
        False, 'or', False, r))

r = False or True
print('{0} {1} {2} = {3}'.format(
        False, 'or', True, r))

r = True or False
print('{0} {1} {2} = {3}'.format(
        True, 'or', False, r))

r = True or True
print('{0} {1} {2} = {3}'.format(
        True, 'or', True, r))

# not 연산자
# 단항연산자
# 우항의 관계식 결과를 부정하는 연산자
# True -> False, False -> True

r = not False
print('not {0} = {1}'.format(
        False, r))

r = not True
print('not {0} = {1}'.format(
        True, r))

# 나이(age)가 30대이면서
# 성별(gender)가 여성인 경우를 판단하는
# 관계식을 작성한 후, 결과를 확인하세요.
age=35
gender='여성'
#r = age >= 30 and age < 40
r = age // 10 == 3 and gender == '여성'
print(r)












