# -*- coding: utf-8 -*-

# map 함수
# filter 함수와 유사함.

# filter 함수의 경우 True, False 의 값을 반환하는
# 함수를 사용하여 특정 데이터를 필터링하는 역할을
# 하지만 map 함수는 특정 연산을 모든 요소에
# 적용하기 위해서 활용합니다.

# 함수의 실행 결과 
# filter 함수는 원본 데이터의 개수보다 작을 수 있음
# map 함수는 원본 데이터와 개수가 같음

numbers = [1,2,5,7,9]

# map 함수를 사용하여 numbers 내부의 
# 모든 요소의 값을 제곱하는 코드
result=list(map(lambda n : n * n, numbers))
print(result)

# map 함수를 사용하여 numbers 내부의 
# 홀수인 요소 값을 제곱하는 코드
result=list(map(lambda n : n * n, 
    filter(lambda n : n % 2 == 0, numbers)))
print(result)















