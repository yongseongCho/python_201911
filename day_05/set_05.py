# -*- coding: utf-8 -*-

set_numbers = set([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9])
# set 타입은 중복을 제거하기 때문에
# 크기는 9가 됩니다.
print(len(set_numbers))

# Set 내부의 데이터를 삭제하는 방법

# remove 메소드를 사용하여 특정 데이터를 제거
set_numbers.remove(3)
print(len(set_numbers))
print(set_numbers)

set_numbers.remove(6)
print(len(set_numbers))
print(set_numbers)

set_numbers.remove(4)
print(len(set_numbers))
print(set_numbers)

# pop 메소드를 활용하여 Set 내부의 데이터를 삭제
# pop 메소드는 삭제한 데이터를 반환합니다.
# - set 내부의 저장된 가장 앞의 데이터를 삭제
removed = set_numbers.pop()
print(len(set_numbers))
print(set_numbers)
print(removed)

removed = set_numbers.pop()
print(len(set_numbers))
print(set_numbers)
print(removed)

# Set 타입의 clear 메소드는 Set 내부의 모든
# 데이터를 삭제합니다.
set_numbers.clear()
print(len(set_numbers))
print(set_numbers)

# 컬렉션 타입의 데이터를 저장할 수 있는 
# 파이썬의 데이터 타입
# - 데이터 저장의 크기에 제약이 없음

# - list
# : 값의 중복을 허용, 저장 순서를 유지

# - dictionary (JSON 포멧으로 데이터를 저장)
# : (키 : 밸류)의 형태로 저장되는 타입
# : 키 값의 중복을 허용하지 않음
#   (Value의 값은 중복이 허용됨)
# : 만약 동일한 키 값으로 데이터가 입력되면
# 기존의 키값이 가지고 있는 데이터가 수정됩니다.

# - set
# : 데이터의 중복이 허용되지 않음
# : 데이터 저장의 순서가 유지되지 않음















