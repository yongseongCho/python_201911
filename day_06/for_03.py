# -*- coding: utf-8 -*-

# for 반복문은 정해진 횟수의 반복을 제어하는 경우 사용
# 특정 범위의 반복을 수행(리스트, 딕셔너리, Set 타입의 크기)

# for 변수명 in 컬렉션변수 : 
# 컬렉션 변수의 시작부터 끝까지 각 데이터를 추출하여
# 변수에 대입한 후 실행됨

# 리스트 타입의 컬렉션을 for 반복문으로 제어하는 방법
numbers=[1,2,3,4,5]
for item in numbers :
    print(f'item -> {item}')

# 컬렉션타입의 요소를 순회하는 경우
# 사용할 수 있는 함수
# enumerate : 특정 컬렉션 내부의 데이터를 추출하면서
# 인덱스의 정보도 같이 반환하는 함수
for index, item in enumerate(numbers) :
    print(f'number[{index}] -> {item}')

# 다수개의 컬렉션 타입으로부터 동일 인덱스 위치의 값들을
# 반환할 수 있는 zip 함수
# zip : 다수개의 커렉션을 매개변수로 입력받아
# 동일한 인덱스 위치의 데이터를 반환하는 함수
labels=['One','Two','Three','Four','Five']
numbers=[1,2,3,4,5]
for label, number in zip(labels, numbers) :
    print(f'label -> {label}, number -> {number}')

# 딕셔너리 타입의 컬렉션을 for 반복문으로 제어하는 방법
dict_numbers = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}

# 딕셔너리 타입을 for 문으로 순회하는 경우
# 딕셔너리에 저장된 키값들이 반환됩니다.
for key in dict_numbers :
    #print(key)
    # 키값을 사용하여 값을 추출하는 예제
    #print(dict_numbers[key])
    print(f'dict_numbers[{key}] -> {dict_numbers[key]}')
    
# 딕셔너리 타입 변수의 items 메소드는 key, value의 쌍으로
# 반환하는 메소드
for key, value in dict_numbers.items() : 
    print(key, value)

# Set 타입의 컬렉션을 for 반복문으로 제어하는 방법
message = set('Hello Python~!')
print(message)

for char in message :
    print(f'char -> {char}')














