# -*- coding: utf-8 -*-

numbers = [3, 5, 1, 7, 2]

# sort 메소드를 활용하지 않고 
# 오름차순 정렬을 구현하는 예제

# 정렬의 기준 인덱스를 정하는 반복
for i in range(len(numbers) - 1):
    # 기준 인덱스 이후에 위치하는 모든 요소를 반복
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j] :
            numbers[i], numbers[j] = numbers[j], numbers[i]
        
print(numbers)










