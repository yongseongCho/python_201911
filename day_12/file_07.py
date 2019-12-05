# -*- coding: utf-8 -*-

# with 절
# with 절은 자동 종료가 필요한 변수의 선언 시
# 사용할 수 있는 구문
# with 변수(변수의 생성코드) as 별칭 :
# with 절에 선언된 변수는 with 영역에서만
# 사용할 수 있고, with 구문이 종료되면
# 자동으로 close 메소드가 호출됩니다.

fname='./data/file_05.txt'

# input_file=open(fname, 'r')
with open(fname, 'r') as input_file :

    scores = input_file.readlines()
    
    for score in scores :
        # 문자열의 좌우 공백을 제거한 후,
        # ,를 기준으로 문자열을 분할
        data=score.strip().split(',')
        
        print(f'1번째성적 : {data[0]}')
        print(f'2번째성적 : {data[1]}')
        print(f'3번째성적 : {data[2]}')
        print(f'총점 : {data[3]}')
        print(f'평균 : {data[-1]}')

# with 절이 종료되면 input_file변수에 대해서
# 자동으로 close 메소드가 호출됩니다.
# input_file.close()









