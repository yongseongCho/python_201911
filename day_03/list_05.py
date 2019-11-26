# -*- coding: utf-8 -*-

list_1 = [1,2,3,4,5,6,7,8,9,10]
print(list_1)

# 리스트의 데이터를 삭제하는 방법
# 1. 슬라이싱 연산과 빈 리스트 객체를 활용하는 방법
list_1[3:6] = []
print(list_1)

# 리스트의 데이터를 삭제하는 방법
# 2. del 연산자를 활용하는 방법
del list_1[3]
print(list_1)

# 리스트의 데이터를 삭제하는 방법
# 3. remove 메소드를 활용하는 방법
# - 특정 데이터를 검색하여 삭제
# - 아래의 코드는 list_1에서 9를 검색하여 삭제
# - 만약 삭제할 데이터가 존재하지 않는 경우 에러가 발생
list_1.remove(9)
print(list_1)

# (시작 위치부터 검색하여 최초로 발견된 데이터만 삭제)
list_1 = [1,5,2,5,3,5,4,5]
list_1.remove(5)
print(list_1)
list_1.remove(5)
print(list_1)

# pop 메소드는 해당 리스트의 마지막 요소를 삭제합니다.
# (삭제한 데이터를 반환)
# del 리스트변수[-1] 과 유사하게 동작합니다.
list_1.pop()
print(list_1)









