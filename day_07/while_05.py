# -*- coding: utf-8 -*-

# 반복문과 break 키워드
# 반복문의 수행 도중 반복을 중단하고자하는 경우
# 사용되는 키워드
# break 키워드를 실행하면 현재 반복의 영역을
# 빠져나가게 됩니다.
# (반복문의 강제 종료 - 정상적인 종료가 아님)

n = 1

while n < 101 :
    # n 변수의 값이 55인 경우 반복의 영역을
    # 빠져나가는 코드
    if n == 55 :
        break
    
    # 위의 break 키워드로 인해서 
    # 54 까지만 출력
    print(f'n -> {n}')
    n += 1
    
print('프로그램 종료')

