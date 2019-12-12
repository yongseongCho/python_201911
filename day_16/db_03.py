# -*- coding: utf-8 -*-

# 데이터베이스 처리
# 파이썬에서는 다양한 데이터베이스 벤더에 대한 
# 모듈을 사용할 수 있습니다.
# (데이터베이스 벤더사에 따른 모듈을 설치를 진행)

import pymysql

# 데이터베이스를 사용한 프로그래밍 과정
# 1. 데이터베이스 연결 객체 생성
conn = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1234',
        db='sakila')

# 2. 데이터베이스 서버에 쿼리문을 실행할 수 있는
# 객체를 생성(데이터베이스 연결 객체로 부터 생성)
cursor = conn.cursor()

# 3. SQL문 작성
# - 문자열로 작성
# - 대다수의 데이터베이스 처리 모듈은 ; 생략이 가능
sql = """
select *
from customer
"""

# 4. SQL문 실행
cursor.execute(sql)

# pymysql의 cursor 객체는 쿼리의 실행 결과 레코드 수를
# rowcount를 통해서 확인할 수 있음
print(f'쿼리 수행 결과 : {cursor.rowcount}건 검색')

# 5. SQL문의 실행 결과를 반복문을 통해서 확인
# - Select 절의 실행 결과를 반환받는 방법
# - fetchone 메소드
#  검색된 결과를 하나씩 전송받는 메소드
#  검색된 데이터가 하나만 나오는 경우 효과적
#  (본인의 회원정보 검색 쿼리와 같이 결과가 1개만 나오는 경우)

# 쿼리의 실행 결과 개수만큼 반복을 수행
for _ in range(cursor.rowcount) :
    # 각 레코드의 컬럼 단위로 데이터를 추출할 수 있음
    customer_id,_,first_name,_,email,_,_,_,_ = \
    cursor.fetchone()

    print(f'{customer_id} -> {first_name}, {email}')

# 6. 리소스 해제 처리 (close 메소드 호출)
cursor.close()
conn.close()




    
    
    
    
    
    
    
    
    
    
    
    
    
    