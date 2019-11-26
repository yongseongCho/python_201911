# -*- coding: utf-8 -*-

# 다음과 같이 구구단을 출력하세요
"""
2 * 2 = 4
2 * 4 = 8
2 * 6 = 12
...
3 * 1 = 3
3 * 3 = 9
3 * 5 = 15
...
4 * 2 = 8
4 * 4 = 16
4 * 6 = 24
...
"""
for dan in range(2, 10) :
    print(f'{dan}단을 출력합니다.')
    
    for mul in range(1, 10) :
        if dan % 2 == mul % 2 :
            print(f'{dan} * {mul} = {dan * mul}')
        
#        if dan % 2 == 0 and mul % 2 == 0 :        
#            print(f'{dan} * {mul} = {dan * mul}')
#        elif dan % 2 == 1 and mul % 2 == 1 :  
#            print(f'{dan} * {mul} = {dan * mul}')











