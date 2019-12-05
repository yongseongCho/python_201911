# -*- coding: utf-8 -*-

from pickle import load

f = open('numbers.dat', 'rb')

# numbers.dat 파일에 저장된
# 리스트 변수를 복원하는 코드
numbers = load(f)

print(numbers)
