# -*- coding: utf-8 -*-

# 구구단의 짝수단만 출력하는 예제를 작성하세요.

#for dan in range(2, 10, 2) :
for dan in range(2, 10) :    
    # 1. if 문의 제어영역을 사용하여 짝수인 경우만 실행
    # - 들여쓰기를 주의해야함...
    if dan % 2 == 0 :
        print(f'{dan}단을 출력합니다.')        
        for mul in range(1, 10) :
            print(f'{dan} * {mul} = {dan * mul}')

for dan in range(2, 10) :    
    # 2. 홀수인 경우 반복을 실행하지 않고 다음 순번으로
    # 이동하는 방법
    # - continue 키워드를 사용
    # - continue : 현재 반복을 중지하고 반복문의 
    # 종료 지점으로 이동하는 명령
    # - continue : 반복문 내부에서만 사용할 수 있음
    if dan % 2 == 1 :
        continue
    
    print(f'{dan}단을 출력합니다.')        
    for mul in range(1, 10) :
        print(f'{dan} * {mul} = {dan * mul}')





