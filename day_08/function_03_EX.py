# -*- coding: utf-8 -*-

# 3개의 정수를 매개변수로 전달받아
# 최대값을 반환할 수 있는 custom_max 함수를 
# 정의한 후 결과를 확인하세요.
def custom_max(n1, n2, n3) :
    if n1 > n2 :
        r = n1
    else :
        r = n2
        
    if n3 > r :
        r = n3
    
    return r

r = custom_max(10, 5, 7)
print(r) # 10








