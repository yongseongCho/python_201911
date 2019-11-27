# -*- coding: utf-8 -*-

# break 키워드 동작 방식
# if 문을 제외한 첫 번째 영역을 빠져나가는 키워드
n = 1
while n < 101 :    
    if n == 55 :
        # if문의 영역을 제외한 첫번째 영역인
        # while 문을 빠져나가도록 동작합니다.
        break    
    
    print(f'n -> {n}')
    n += 1

n1 = 1
while n1 < 11 :
    
    if n1 == 6 :
        # 외부의 while 문을 종료하는 break 명령
        break
    
    n2 = 1
    while n2 <= 3 :
        if n2 == 1 :
            # 내부의 while 문을 종료하는 break 명령
            break
        
        print(f'n1 -> {n1}, n2 -> {n2}')
        n2 += 1

    print(f'n1 -> {n1}')
    n1 += 1













