# -*- coding: utf-8 -*-

# 두개 이상의 값을 반환하는 함수의 선언
def max_and_min(n1, n2) :
    max_value = min_value = n1
    
    if max_value < n2 :
        max_value = n2
        
    if min_value > n2 :
        min_value = n2

    # 2개의 값을 반환하는 return 문
    # (다수개의 값을 반환하더라도, 컬렉션 타입으로 
    # 반환되기 때문에 1개의 변수로 값을 전달받을 수
    # 있습니다.)
    return max_value, min_value
   
# 컬렉션 타입으로 리턴 값을 전달받는 경우
# - 하나의 변수로 여러개의 값을 전달받음
r = max_and_min(15, 7)
print(f'r -> {r}')
print(f'최대값 : {r[0]}')
print(f'최소값 : {r[1]}')

# 리턴되는 다수개의 값을 각 변수에 대입받는 경우
m1, m2 = max_and_min(100, 200)
print(f'최대값 : {m1}')
print(f'최소값 : {m2}')  
        
        
        
        




