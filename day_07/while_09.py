# -*- coding: utf-8 -*-

# while 문을 사용하여 구구단을
# 출력하는 코드를 작성한 후,
# 출력 결과를 확인하세요.

print('while 문을 사용한 구구단 출력')

dan = 2

# 단을 제어하는 외부의 반복문
while dan <= 9 :
    print(f'{dan}단을 출력합니다.')
    
    # 곱해지는 수를 제어하는 내부의 반복문
    mul = 1
    while mul < 10 :
        print(f'{dan} * {mul} = {dan*mul}')
        mul += 1
        
    dan += 1







