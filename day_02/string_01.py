# -*- coding: utf-8 -*-

# 문자열
# 하나 이상의 문자들의 집합

# 파이썬에서 문자열을 지정하는 방법

# 1. 쌍따옴표를 사용하는 방법
str1="Hello Python 1"
print('str1 -> {}'.format(str1))

# 2. 작은따옴표를 사용하는 방법
str2='Hello Python 2'
print('str2 -> {}'.format(str2))

# - 문자열을 정의할 때 쌍따옴표를 사용하는 경우
# 문자열 내부에 작은따옴표를 문자로 취급합니다.
str1 = "Hello 'Python' 1"
print('str1 -> {}'.format(str1))

# - 문자열을 정의할 때 작은따옴표를 사용하는 경우
# 문자열 내부에 쌍따옴표를 문자로 취급합니다.
str2 = 'Hello "Python" 2'
print('str2 -> {}'.format(str2))

# 쌍따옴표로 저장된 문자열 내부에 쌍따옴표를
# 저장하기 위한 방법
# - 역슬러쉬 사용
str1 = "Hello \"Python\" 1"
print('str1 -> {}'.format(str1))

# 3. """ """를 사용하는 방법
str3 = """Hello Python 3"""
print('str3 -> {}'.format(str3))

# 4. ''' '''를 사용하는 방법
str4 = '''Hello Python 4'''
print('str4 -> {}'.format(str4))

# """과 '''를 활용하여 문자열을 지정하는 경우
# 여러 라인으로 구성된 문자열을 저장할 수 있음
str3 = """ 
Hello 
Python
3
"""
print('str3 -> {}'.format(str3))

# \n : 개행문자(다음 라인으로 커서를 이동)
str1 = "\nHello \nPython \n1"
print('str1 -> {}'.format(str1))






