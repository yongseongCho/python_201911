# -*- coding: utf-8 -*-

# csv 모듈
# csv 포맷으로 데이터를 저장하거나
# 불러오고자 하는 경우 손쉽게 사용할 수 있는
# 기능을 제공하는 모듈
import csv

count = 3
scores=[]

for i in range(1, count+1) :
    scores.append(
            int(input(f'{i}번째 성적 : ')))

fname='./data/file_08.txt'
# newline 옵션
# 개행 문자를 처리하기 위한 옵션 값
# 개행 문자를 newline 매개변수에 전달된 값으로
# 대체해서 출력할 수 있는 옵션
# w, a 모드에 사용
with open(fname, 'a', newline='') as output :
    # 파일에 CSV 포맷으로 출력할 수 있는
    # csv 모듈의 writer 객체 생성
    csv_writer=csv.writer(output)
    csv_writer.writerow(scores)











