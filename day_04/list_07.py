# -*- coding: utf-8 -*-

list_1 = [5, 1, 7, 3, 9, 11, 0]
print('Before : ', list_1)

# 정렬 기능
# 리스트 변수의 sort 메소드를 사용하여
# 오름차순으로 정렬할 수 있습니다.
list_1.sort(reverse=True)
print('After : ', list_1)

# reverse 메소드는 해당 리스트의 요소들을 역순으로
# 배치합니다.
# (정렬이 아님!)
list_1.reverse()
print('After : ', list_1)








