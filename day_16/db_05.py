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
insert into user_info
values (1, 'Hello', 15)
"""

# 데이터베이스에 입력하는 과정에서 
# 기본키 중복과 같은 에러가 발생될 수 있으므로
# 반드시 예외처리를 해야만 합니다.
try :
    cursor.execute(sql)
except Exception as e :
    print(f'데이터 입력 에러 : {e}')
    # 예외가 발생한 경우
    # 현재까지의 작업을 취소함
    conn.rollback()
else :
    print('데이터 입력 성공')
    conn.commit()
finally :
    # 예외의 발생 여부와 관계없이
    # 리소스의 해제과정을 실행함
    cursor.close()
    conn.close()








