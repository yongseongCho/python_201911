# -*- coding: utf-8 -*-

list_1 = [11, 25, 35]

# list_1의 각 요소에 10을 곱한 값을 가지는
# list_2를 생성하세요

#list_2 = []
#for item in list_1 :
#    list_2.append(item * 10)

# 리스트 변수의 생성에 for 문이 활용되는 예제
# 리스트변수명 = [실행문 for 변수명 in 컬렉션]
list_2 = [item * 10 for item in list_1]
    
print(list_1)
print(list_2)









