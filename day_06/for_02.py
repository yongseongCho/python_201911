# -*- coding: utf-8 -*-

# for 반복문
# for 변수명 in 컬렉션타입의데이터 :
#   컬렉션타입의데이터를 하나씩 추출하여 작업할 내용...

# range 함수 : 특정 영역의 값의 범위를 반환하는 함수
# 1. range(end)
# - range(5) -> [0,1,2,3,4]
# 2. range(start, end)
# - range(2, 5) -> [2,3,4]
# 3. range(start, end, step)
# - range(1, 11, 3) -> [1,4,7,10]

for i in range(10) :
    print(f'i -> {i}')

for i in range(5, 10) :
    print(f'i -> {i}')

for i in range(0, 10, 2) :
    print(f'i -> {i}')

# 1 ~ 100 사이의 정수 중, 3의 배수만 출력하세요
for i in range(3, 101, 3) :
    print(f'i -> {i}')

# 1 ~ 100 사이의 정수 중, 짝수의 합계를 계산한 후
# 출력하세요.

# 짝수의 합계를 누적하기 위한 변수
tot = 0

for i in range(1, 101) :
    if i % 2 == 0 :
        tot += i    # tot = tot + i
    
print(f'1 ~ 100까지 짝수들의 합계는 {tot} 입니다.')

# 1 ~ 100 사이의 정수를 사용하여 아래의 식의 결과를
# 출력하세요.
# 1 - 2 + 3 - 4 + 5 ..... + 99 - 100
tot = 0
for i in range(1, 101) :
    if i % 2 == 1 :
        tot += i
    else :
        tot -= i
print(f'1 ~ 100까지 계산의 결과는 {tot} 입니다.')





