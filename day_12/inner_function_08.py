# -*- coding: utf-8 -*-

# 동일한 크기를 갖는 2개의 리스트
strNumbers = ['One','Two','Three','Four','Five']
numbers = [1,2,3,4,5]

# 동일한 위치의 인덱스 정보끼리 결합하는 함수
# zip 함수
combine = list(zip(strNumbers, numbers))
print(combine)

# 반복문에서 zip함수를 사용하는 예제
# - zip 함수의 매개변수 개수만큼의 
#  요소를 반환합니다.
for s, n in zip(strNumbers, numbers) :
    print(f'{s} = {n}')










