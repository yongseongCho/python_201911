# -*- coding: utf-8 -*-

# 문자열 비교 연산
# == 연산자를 활용하여 문자열을 비교할 수 있음
str1 = 'Hello'
str2 = "Hello"
r = str1 == str2
print('str1 == str2 -> {}'.format(r))

# is 연산자를 활용한 문자열 비교 연산
r = str1 is str2
print('str1 is str2 -> {}'.format(r))

# str2 변수는 공백을 포함하고 있기때문에
# str1 과 같지 않음
str1 = 'Hello'
str2 = "Hello "
r = str1 == str2
print('str1 == str2 -> {}'.format(r))





