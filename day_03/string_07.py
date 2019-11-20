# -*- coding: utf-8 -*-

data = 'abcdefg'
delim = ','

# data 변수의 각 문자 사이에 ,를 추가하는 예제
# r 은 a,b,c,d,e,f,g
r_join = delim.join(data)
print('r_join -> {}'.format(r_join))

# 문자열 분할을 제공하는 split 메소드
# 매개변수(sep)를 지정하지 않으면 공백을 기준으로 문자열을
# 분할하고, 매개변수를 사용하면 매개변수의 값을 기준
# 으로 해당 문자열 분할한 결과를 리스트 형태로 반환
r_split = r_join.split(sep=',')
print('r_split -> {}'.format(r_split))

jumin = '870519-1015798'

year = jumin[:2]
month = jumin[2:4]
day = jumin[4:jumin.find('-')]

# 다수개의 변수를 초기화하는 예제
year,month,day = jumin[:2],jumin[2:4],jumin[4:6]

print('{0}년 {1}월 {2}일 생입니다.'.format(
        year, month, day))

gender = jumin[7] == '1' or jumin[7] == '3'
gender = jumin.split('-')[1][0] == '1'

# 형변환을 사용한 생년월일 출력
# - 문자열 타입의 값을 정수/실수로 변환할 수 있음
n_year = int(year)
n_month = int(month)
n_day = int(day)

print('{0}년 {1:>2}월 {2:>2}일 생입니다.'.format(
        n_year, n_month, n_day))











