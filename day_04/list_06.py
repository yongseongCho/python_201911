# -*- coding: utf-8 -*-

# 리스트에 데이터를 추가하는 방법(중간에 삽입)
# insert 메소드를 활용
# 리스트변수.insert(인덱스, 데이터)
list_1 = [1,3,5,7,9]
print(list_1)

# list_1 의 인덱스 1 위치에 2를 추가
# 기존의 인덱스 1 위치의 데이터는 뒤로 밀려납니다.
list_1.insert(1, 2)
print(list_1)

list_1.insert(-1, 8)
print(list_1)

# 리스트의 index 메소드는 문자열 변수의
# find 메소드와 같이 특정 값의 인덱스를
# 반환합니다.
list_1.insert(list_1.index(5), 4)
print(list_1)

list_1.insert(list_1.index(7), 6)
print(list_1)

# insert 메소드를 사용하여 리스트의 가장 앞에
# 데이터를 추가할 수 있습니다.
list_1.insert(0, 0)
print(list_1)
# (insert 메소드는 리스트의 마지막에 데이터를 
# 추가할 수 없습니다. - append 를 사용해야함)
list_1.insert(-1, 10)
print(list_1)

list_1.append(10)
print(list_1)






