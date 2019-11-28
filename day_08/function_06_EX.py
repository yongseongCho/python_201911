# -*- coding: utf-8 -*-

# 가변매개변수를 사용하여
# 입력된 모든 정수들의 최대값, 최소값을
# 반환할 수 있는 max_and_min 함수를 
# 작성한 후, 결과를 확인하세요.
def max_and_min(*numbers) :
    if len(numbers) < 2 :
        return None, None
    
    max_value = min_value = numbers[0]
    for n in numbers[1:] :
        if max_value < n :
            max_value = n
        if min_value > n :
            min_value = n
    
    return max_value, min_value

r = max_and_min()
print(r)

r = max_and_min(10, 20) # 20, 10
print(r)
r = max_and_min(5, 3, 7, 15) # 15, 3
print(r)









