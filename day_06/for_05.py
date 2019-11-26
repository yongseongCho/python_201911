# -*- coding: utf-8 -*-

# 중첩된 반복문을 활용한 구구단 예제
# 외부의 반복문을 단수 제어로 활용
# 내부의 반복문을 곱해지는 수로 제어

for dan in range(2, 10) :
    print(f'{dan}단을 출력합니다.')
    
    for mul in range(1, 10) :
        print(f'{dan} * {mul} = {dan * mul}')












