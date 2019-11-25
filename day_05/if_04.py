# -*- coding: utf-8 -*-

# 조건이 다수개인 경우 처리하는 방법
# if ~ elif ~ else
# if 1번째 조건식:
#   1번째 조건식이 참일 경우 실행문장
# elif 2번째 조건식:
#   2번째 조건식이 참일 경우 실행문장
# ...
# else:
#   모든 조건식이 거짓일 경우 실행문장

print('1. 한식')
print('2. 일식')
print('3. 중식')
menu = int(input('메뉴를 선택하세요 : '))

if menu == 1 :
    print('오늘의 한식메뉴는 김치찌개입니다.')
    
elif menu == 2 :
    print('오늘의 일식메뉴는 우동입니다.')
    
elif menu == 3 :
    print('오늘의 중식메뉴는 짬뽕입니다.')








