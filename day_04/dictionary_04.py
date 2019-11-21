# -*- coding: utf-8 -*-

dict_numbers={'one':1,'two':2,
              'three':3,'four':4,
              'five':5}

# dict_numbers 딕셔너리에 저장된 요소의 개수 확인
c = len(dict_numbers)
print('딕셔너리에 저장된 요소의 개수 : ', c)

# Dictionary 변수의 keys 메소드는 해당 Dictionary 내부에
# 저장된 모든 키의 값을 dict_keys 타입으로 반환
# dict_keys 타입을 인덱스를 기반으로 손쉽게 사용하기
# 위해서 리스트 타입으로 변환할 수 있으며,
# list() 형변환을 통해 변환합니다.
keys = list(dict_numbers.keys())
print(keys)

print(keys[0])
print(keys[1])
print(keys[2])

# Dictionary 변수의 values 메소드는 
# 해당 Dictionary 내부에 저장된 모든 value 값을 
# dict_values 타입으로 반환
# dict_values 타입을 인덱스를 기반으로 손쉽게 사용하기
# 위해서 리스트 타입으로 변환할 수 있으며,
# list() 형변환을 통해 변환합니다.
values = list(dict_numbers.values())
print(values)

print(values[0])
print(values[1])
print(values[2])






