# -*- coding: utf-8 -*-

# 1 ~ 12 사이의 정수를 입력받아 
# 해당 월의 일수를 출력하세요
# EX) 1 -> 31, 2 -> 28, 3 -> 31 ...

# 1. 입력 변수의 선언 및 입력과정 수행
month = int(input('1 ~ 12 사이의 정수를 입력 : '))

# 2. 입력된 값을 사용하여 처리 과정을 수행
# - 처리 과정에 필요한 변수의 선언 및 계산과정을 수행
day = None

month_31=[1,3,5,7,8,10,12]
month_30=[4,6,9,11]

if month in month_31 :
    day = 31
elif month in month_30 :
    day = 30
elif month == 2 :
    day = 28

# 3. 처리 결과를 출력/저장
if day :
    print(f'{month}월은 {day}일 까지 있습니다.')
else :
    print('(ERROR!)1 ~ 12 사이의 정수를 입력해야 합니다.')








