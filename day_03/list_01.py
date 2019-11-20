# -*- coding: utf-8 -*-

# LIST 타입의 변수 사용
# 기존의 배열과 유사한 타입의 변수 (동적 배열)
# - 배열의 정의
# - 동일한 타입의 연속된 집합

# 비어있는 리스트 변수의 선언
list_1 = []
# 3개의 정수 요소를 가지는 리스트의 선언
list_2 = [10, 20, 30]
# 다양한 타입의 요소를 가지는 리스트 선언
# - 배열과의 차이점!
list_3 = [10, 11.5, 'Python_List', True]

print(list_1)
print(list_2)
print(list_3)

# 모든 리스트 변수들은 내부에 저장된 요소에 관계없이
# 동일한 리스트 타입으로 인식됩니다.
print(type(list_1))
print(type(list_2))
print(type(list_3))

# len 함수를 사용하여 리스트 내부의 요소 개수를
# 반환받을 수 있습니다.
print('list_1의 요소 개수 : ', len(list_1))
print('list_2의 요소 개수 : ', len(list_2))
print('list_3의 요소 개수 : ', len(list_3))

# 리스트 내부의 요소(데이터)를 접근하는 방법
# 인덱스 연산을 사용 (시작은 0)
print(list_2)
print('list_2[0] -> ', list_2[0])
print('list_2[1] -> ', list_2[1])
print('list_2[2] -> ', list_2[2])

# 범위를 벗어나는 인덱스를 사용하는 경우
# 에러가 발생됩니다.
# - IndexError
print('list_2[3] -> ', list_2[3])

# 리스트 내부에 저장된 마지막 요소에 접근하기 위해서
# -1 인덱스를 활용합니다.
print('list_2[-1] -> ', list_2[-1])

# 리스트 내부 요소의 데이터 변경
# - 특정 인덱스 위치의 데이터를 변경할 수 있음
print(list_2)
list_2[1] = 200
print(list_2)

# 리스트 변수의 슬라이싱 연산
# 리스트변수명[시작인덱스:종료인덱스]
# (종료인덱스 이전까지의 값이 추출됨)
print(list_3)
list_3_part = list_3[1:3]
print(list_3_part)

# 슬라이싱된 리스트는 원본 리스트와 분리됩니다.
# (슬라이싱된 리스트의 데이터를 수정해도 원본
# 리스트의 데이터에는 영향이 없습니다.)
list_3_part[0] = 111
print(list_3_part)
print(list_3)






