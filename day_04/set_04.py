# -*- coding: utf-8 -*-

numbers = set()
print(len(numbers))

# Set 타입에 데이터를 추가하는 방법
# add 메소드를 사용하여 처리할 수 있습니다.
# add 메소드는 단일 값을 추가하는 경우 사용
# (1개의 데이터 입력 시 사용)
numbers.add(2)
numbers.add(4)
numbers.add(6)
numbers.add(8)
numbers.add(10)
numbers.add(10)

print(len(numbers))
print(numbers)

# update 메소드는 다수개의 값을 
# 추가하는 경우 사용
numbers.update([12,14,16,18,20])

print(len(numbers))
print(numbers)




