# -*- coding: utf-8 -*-

list_1 = [11, 22, 33]

# list_1의 각 요소 중 짝수인 요소만 10을 곱하여
# list_2를 생성하세요
# list_2 = [220]

#list_2 = []
#for item in list_1 :
#    if item % 2 == 0 :
#        list_2.append(item * 10)

# 리스트 변수의 생성에 for 문이 활용되는 예제
# 조건식이 만족하는 경우에만 리스트에 값을 추가하는 코드
# 리스트변수명 = [실행문 for 변수명 in 컬렉션 if 조건식]
list_2 = [item * 10 for item in list_1 if item % 2 == 0]
        
print(list_1)
print(list_2)

list_1 = [11, 22, 33]

# list_1의 각 요소 중 짝수인 요소에는 10을 곱하고,
# 홀수인 요소는 10을 나누어서 list_2를 생성하세요
# list_2 = [1.1, 220, 3.3]

#list_2 = []
#for item in list_1 :
#    if item % 2 == 0 :
#        list_2.append(item * 10)
#    else :
#        list_2.append(item / 10)

list_2 = [item * 10 if item % 2 == 0 else item / 10 
          for item in list_1]

print(list_1)
print(list_2)








