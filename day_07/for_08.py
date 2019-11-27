# -*- coding: utf-8 -*-

# LIST 변수를 사용하여 사용자에게 3개의 정수를 입력받고
# 입력된 정수의 합계, 평균, 최대값, 최소값
"""
1번째 정수 : 10
2번째 정수 : 5
3번째 정수 : 20
입력된 정수 리스트 : [10, 5, 20]
합계 : 35, 평균 : 11.66, 최대값 : 20, 최소값 : 5
"""
# 입력된 정수들을 저장하기 위한 리스트 변수
numbers = []
# 입력받을 정수의 개수
size = 3

for i in range(size) : 
    # 아래의 코드는 비어있는 리스트 객체의 특정 
    # 인덱스에 접근하는 연산으로 에러가 발생
    # numbers[i] = int(input(f'{i + 1}번째 정수 : '))
    
    # 아래의 코드는 비어있는 리스트에 값을 추가   
    numbers.append(int(input(f'{i + 1}번째 정수 : ')))

# 리스트 내부의 값을 정렬하는 방법
numbers.sort()

print(f'입력된 정수 리스트 : {numbers}')

tot = maxValue = minValue = numbers[0]
for n in numbers[1:] :
    # 합계
    tot += n
    # 최대값
    if n > maxValue :
        maxValue = n
    # 최소값
    if n < minValue :
        minValue = n

# 평균
avg = tot / size

print(f'합계 : {tot}, 평균 : {avg:.2f}, 최대값 : {maxValue}, 최소값 : {minValue}')








