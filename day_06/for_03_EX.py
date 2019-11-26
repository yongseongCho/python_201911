# -*- coding: utf-8 -*-

# 사용자에게 3과목의 성적을 입력받아
# 총점과 평균을 출력하세요.
# 최고성적, 최하성적 점수를 포함하여 출력하세요

# 과목의 수를 저장하는 변수
count = 3
# 입력된 성적을 저장하기 위한 변수
scores = []
# 총점을 저장하기 위한 변수
tot = 0
# 평균을 저장하기 위한 변수
avg = 0
# 최고/최저 성적을 저장하기 위한 변수
max_score, min_score = 0, 0

# 입력과정
for index in range(1, count + 1) :
    temp = int(input(f'{index} 번째 성적을 입력 : '))
    
    # 성적 추가
    scores.append(temp)
    # 총점 계산
    tot += temp
    
    # 최고/최저 성적을 계산
    # - 최초로 입력된 값을 최고값/최저값을 설정
    if index == 1 :
        max_score = min_score = temp
    # - 최초에 입력받은 값을 기준으로
    # 최대값을 가장 큰 값을 가지도록..
    # 최소값을 가장 작은 값을 가지도록 조건에
    # 따라 값을 수정
    else :
        if temp > max_score :
            max_score = temp
        if temp < min_score :
            min_score = temp

# 평균 계산
avg = tot / count

print(f'입력된 성적 : {scores}')
print(f'총점 : {tot}, 평균 : {avg}')
print(f'최고점 : {max_score}, 최저점 : {min_score}')













