# -*- coding: utf-8 -*-

# db_06 파일을 참고하여 아래의 문제를 풀어보세요
# - 사용자에게 삭제할 유저의 ID를 입력받아
#  user_info 테이블에서 해당되는 유저의 정보를
#  삭제하는 프로그램을 작성하세요
# - 삭제의 성공여부를 확인하여 출력하세요

user_id = input('삭제할 유저의 아이디 입력 : ')

import pymysql

conn=pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1234',
        db='mydb')
cursor=conn.cursor()

# 삭제할 유저의 데이터 유무를 확인
select_sql=f"""
select *
from user_info
where id = {user_id}
"""
cursor.execute(select_sql)

if cursor.rowcount == 1: 
    delete_sql = f"""
        delete from user_info
        where id = {user_id}
    """
    cursor.execute(delete_sql)
    if cursor.rowcount == 1 :
        print('삭제 완료')
        conn.commit()
    else :
        print('삭제 실패')
else :
    print('입력된 ID의 유저 정보가 없음')



cursor.close()
conn.close()







