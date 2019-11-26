# -*- coding: utf-8 -*-

# 구구단의 각 단을 출력하기 전에
# 사용자에게 프로그램의 실행 여부를 확인하세요
# 만약 종료를 원하면 즉시 프로그램 종료합니다.

for dan in range(2, 10) :
    flag = input('종료할까요? (y/n) : ')
    if flag == 'y' :
        # break 키워드
        # 현재 반복문의 영역을 빠져나가는 명령
        # 반복의 종료를 의미함
        # - 강제 종료
        break
    print(f'{dan}단을 출력합니다.')    
    for mul in range(1, 10) :
        print(f'{dan} * {mul} = {dan * mul}')









