# -*- coding: utf-8 -*-

# Set 타입의 데이터를 활용한 &(and), |(or), -
numbers_2 = set([2,4,6,8,10,12])
numbers_3 = set([3,6,9,12])

# Set 변수가 저장하고 있는 데이터의 교집합 추출
# (중복 데이터 추출)
print(numbers_2 & numbers_3)
# Set 변수가 저장하고 있는 데이터의 합집합 추출
# (중복되는 데이터는 하나만 유지)
print(numbers_2 | numbers_3)
# Set 변수가 저장하고 있는 데이터의 차집합 추출
# (서로 다른 Set 타입의 데이터에서 중복되는 
# 데이터를 제거한 결과를 반환)
print(numbers_2 - numbers_3)
print(numbers_3 - numbers_2)






