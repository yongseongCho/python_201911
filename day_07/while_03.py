# -*- coding: utf-8 -*-

# while 반복문을 사용하여
# 1 ~ 100 까지 정수들의 합계를 출력

n = 1
end = 100

# 반복문을 통해서 누적된 값을 저장하는 변수는
# 반드시 반복문 외부에서 선언해야만 합니다
# (반복문의 외부에서 초기값을 지정해야함)
tot = 0

while n <= end :
    tot += n
    n += 1
    
print(f'1 ~ 100까지의 합계는 {tot} 입니다.')










