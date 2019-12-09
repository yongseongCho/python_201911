# -*- coding: utf-8 -*-

import pandas as pd

data = {
        'year':[2017,2018,2019],
        'GDP Rate':[2.8,3.1,3.0],
        'GDP':['1.637M','1.859M','2.237M'],
}

df = pd.DataFrame(data)

print(df)

# year 컬럼의 데이터 중 
# 2018년도 이후인 데이터를 추출

# 조건식의 결과인 BOOLEAN 값이 반환
print(df.year >= 2018)
# 조건식의 결과를 사용하여 값을 반환
print(df[df.year >= 2018])

# 특정 조건에 맞는 일부분의 컬럼 데이터 조회
# 데이터프레임변수[열의이름][조건식]
print(df['GDP'][df.year >= 2018])

# 다수개의 열을 추출하는 경우
# 데이터프레임변수[ [열1,열2...열N] ][조건식]
print(df[['GDP', 'GDP Rate']][df.year >= 2018])

# pandas 에서 object 타입은 문자열을 의미합니다.
print(df.GDP)

# 문자열 타입이 제공하는 startswith 메소드
# 매개변수로 시작되는 경우 True

# 데이터프레임명.컬럼명 -> Series 타입이 반환됩니다.
# 정수또는 실수형의 경우 조건식을 사용하여 값을 비교하기 때문에
# 문제가 발생되지 않지만 아래와 같이 문자열을 비교하는 메소드의
# 경우 Serise 타입이 해당 메소드를 제공하지 않기 때문에
# 에러가 발생
print(df.GDP.startswith('1.'))

# Serise타입은 인덱스 연산을 사용할 수 있습니다.
# - 특정 인덱스 위치의 값을 반환
# - 아래의 코드는 첫번째 글자를 비교하는 연산이 아님!
print(df.GDP[0] == '1')

# Serise이 제공하는 str 속성
# 해당 Serise 내부의 데이터를 문자열 배열과 같은 형태로
# 반환하는 속성
print(df.GDP.str.startswith('1.'))

# GDP의 값이 1로 시작하는 연도를 반환하는 코드
print(df.year[df.GDP.str.startswith('1')])









