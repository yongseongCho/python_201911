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
update user_info
set name = '아무개'
where id = 1000
"""

try :
    cursor.execute(sql)
except Exception as e :
    print(f'데이터 수정 에러 : {e}')
    # 예외가 발생한 경우
    # 현재까지의 작업을 취소함
    conn.rollback()
else :
    if cursor.rowcount > 0 :
        print('데이터 수정 성공')
    else :
        print('수정된 레코드가 없음')
        
    conn.commit()
finally :
    # 예외의 발생 여부와 관계없이
    # 리소스의 해제과정을 실행함
    cursor.close()
    conn.close()








