# -*- coding: utf-8 -*-

import pymysql as pms

# 데이터베이스 연결 정보 변수들
host='localhost'
port=3306
user='root'
passwd='1234'
db='calculator'

# 데이터베이스 커넥션 객체 생성
conn=pms.Connect(
        host=host,
        port=port,
        user=user,
        passwd=passwd,
        db=db)
# 커서 객체 생성
cursor=conn.cursor()

# history 테이블의 전체 레코드 개수를
# 반환하는 함수 작성
def getHistoryCount(cursor) :
    sql="""
        select count(*)
        from history
    """
    cursor.execute(sql)
    count = cursor.fetchone()[0]
    return count

# history 테이블의 전체 레코드를 조회하여
# 조회 결과를 반환하는 함수 작성
def getHistories(cursor) :
    sql="""
        select *
        from history
    """
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

# history 테이블에 데이터를 입력하는 함수 작성
def putHistory(conn, cursor, 
               l_value, 
               r_value, 
               operator, 
               result) :
    sql=f"""
        insert into history 
        (l_value,r_value,operator,result)
        values 
        ({l_value},{r_value},'{operator}',{result})
    """
    cursor.execute(sql)   
    conn.commit()
    return cursor.rowcount

while True :
    if getHistoryCount(cursor) > 0 :
        print('s : 과거데이터조회')
    else:
        print('<과거데이터가 존재하지 않습니다>')
    print('i : 신규데이터추가')
    print('x : 종료')

    choice = input('선택 : ')
    if choice == 's' :
        result = getHistories(cursor)
        for i, r in enumerate(result) :
            l_val = r[1]
            r_val = r[2]
            op = r[3]
            op_r = r[4]
            print(f'{i} : {l_val} {op} {r_val} = {op_r}')
    elif choice == 'i' :
        code = input('연산식을 입력 : ').strip()
        l_val, op, r_val = code.split()
        op_r = eval(code)
        print(f'{code} = {op_r}')
        c = putHistory(conn, cursor, 
                   l_val, r_val, op, op_r)
        if c == 1 :
            print('저장완료')
        else:
            print('저장실패')
    elif choice == 'x' :
        print('프로그램 종료')
        break
    else:
        print('잘못된 메뉴를 선택했습니다.')

















