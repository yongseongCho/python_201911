# -*- coding: utf-8 -*-

# file_10.csv 파일에 저장된 총 금액의 합계를 출력하세요
# - $는 제외한 상태에서 합계를 계산하세요.

import csv
input_file_name = './data/file_10.csv'

total = 0
with open(input_file_name, 'r') as input_file :
    reader = csv.reader(input_file)
    
    for i, history in enumerate(reader) :
        print(f'{i+1} : {history}')
        # 금액 문자열을 추출
        str_money = history[1]
        # 금액 문자열에서 $를 제외
        str_money = str_money[1:]
        # 금액 문자열 사이에 존재할 수 있는
        # , 를 제외
        str_money = str_money.replace(',', '')
        
        total += int(str_money)

print(f'전체 데이터의 합계는 ${total} 입니다.')









