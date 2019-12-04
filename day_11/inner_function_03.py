# -*- coding: utf-8 -*-

numbers = [10, 15, 30, 55, 99]

# numbers 리스트 내부의 모든 요소를
# 순회하는 반복문
for n in numbers :
    print(n)

# for 문에서 인덱스 정보를 활용하기 위한 코드
# - 인덱스 정보를 직접 제어하는 방식
index = 0
for n in numbers :
    print(f'numbers[{index}] -> {n}')
    index += 1

# enumerate 함수는 인덱스 정보와 해당 위치의
# 값을 반환하는 함수입니다.
for i, n in enumerate(numbers) :
    print(f'numbers[{i}] -> {n}')
    












