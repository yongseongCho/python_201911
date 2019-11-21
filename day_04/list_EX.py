# -*- coding: utf-8 -*-

# 2개의 정수를 포함하는 리스트 변수
numbers = [15, 22]

# 정수의 합계를 리스트에 추가
numbers.append(numbers[0] + numbers[1])

# 합계의 결과를 확인
print(numbers)

# 리스트 내부의 요소를 문자열로 결합
# 15;22;37
msg = ';'.join(numbers)
msg = ';'.join(map(str, numbers))
print(msg)



















