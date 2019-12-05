# -*- coding: utf-8 -*-

# 성적 처리를 위해서 3과목의 성적을 입력받고
# 총점과, 평균을 저장 (파일)

# 과목수
count = 3
# 과목 성적
numbers=[]
# 총점/평균
tot=0
avg=0

for i in range(1, count+1) :
    numbers.append(
            int(input(f'{i}번째 성적 : ')))

# 매개변수의 총합을 반환하는 sum 함수
tot = sum(numbers)
avg = tot / count

print(f'총점 : {tot}, 평균 : {avg}')

# 파일에 출력할 데이터의 생성
# - CSV 포맷으로 데이터 생성
output_data=','.join(
        map(lambda n: str(n), numbers))
output_data = f'{output_data},{tot},{avg}\n'

# 파일에 출력
fname='./data/file_05.txt'
# a 모드 : append 모드
# (기존의 데이터를 삭제하지 않고 유지하는 모드)
output_file=open(fname, 'a')
output_file.write(output_data)
output_file.close()

















