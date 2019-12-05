# -*- coding: utf-8 -*-

# CSV 포맷으로 저장된 file_05.txt 데이터를 
# 읽어와서 출력하는 코드를 작성하세요.

fname='./data/file_05.txt'
input_file=open(fname, 'r')

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

input_file.close()









