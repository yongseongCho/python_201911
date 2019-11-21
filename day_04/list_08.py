# -*- coding: utf-8 -*-

list_1 = [1,2,3,4,5]
print(list_1)

list_2 = list_1
print(list_2)

list_1[0] = 10
print(list_1)
print(list_2)

list_2[-1] = 50
print(list_1)
print(list_2)

# list_1이 참조하고 있는 리스트를 전체 복사하여
# 새로운 공간에 저장하고, 그 위치값을 list_2에 대입
# list_1과 list_2는 서로 다른 리스트를 참조
list_1 = [1,2,3,4,5]
list_2 = list_1[:]

print(f'list_1 -> {list_1}')
print(f'list_2 -> {list_2}')

# list_2가 참조하고 있는 리스트를 수정하는 코드
# (list_1이 참조하고 있는 공간에는 영향이 없음)
list_2[2] = 33
print(f'list_1 -> {list_1}')
print(f'list_2 -> {list_2}')






