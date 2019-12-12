# -*- coding: utf-8 -*-

import pymysql

conn=pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1234',
        db='mydb')
cursor=conn.cursor()

sql="""
insert into user_info (name, age)
values ('Hello', 15)
"""

cursor.execute(sql)

# 5. 트랜잭션 처리(commit, rollback)
# 데이터를 검색하는 select 절과 같은 경우 데이터의 수정이 일어나지
# 않기 때문에 데이터 오류가 가능성이 존재하지 않습니다.
# 반면, 데이터의 입력, 수정, 삭제와 같은 경우
# 다수개의 쿼리 실행의 결과가 하나의 작업을 의미하는 경우가 많습니다.
# (이체와 같은 작업)
# 이런 이유로 insert, update, delete 와 같은 SQL 문은 
# 파이썬 모듈에 따라서 반드시 commit 을 해야만 실제 데이터베이스에
# 적용되는 경우가 있습니다.

conn.commit()

cursor.close()
conn.close()








