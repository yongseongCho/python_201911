# -*- coding: utf-8 -*-

# 도시 이름을 입력받아 해당 도시의 정보를
# 출력하는 프로그램을 작성하세요
# - sakila 데이터베이스의 city 테이블을
#  참조하여 작성하세요.
city = input('도시 이름을 입력 : ')

import pymysql
conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1234',
        db='sakila')
cursor=conn.cursor()

# 문자열을 비교하는 쿼리문을 작성할 때
# 반드시 문자열 앞뒤로 작은 따옴표를
# 추가해야 합니다.
sql = f"""
select *
from city
where city = '{city}' 
"""

cursor.execute(sql)

if cursor.rowcount > 0 :
    print(f'{city} 도시 정보를 검색했습니다.')
    
    city_id, _, country_id, last_update = \
    cursor.fetchone()
    
    print('=' * 25)
    print('검색 결과 (city_id, country_id, last_update)')
    print('=' * 25)
    print(f'{city_id}, {country_id}, {last_update}')
    print('=' * 25)
    
else :
    print(f'{city} 정보가 존재하지 않습니다.')

















