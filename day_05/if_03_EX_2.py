# -*- coding: utf-8 -*-

# 사용자에게 3과목의 성적을 입력받아
# 평균점수가 90점이상이면 합격, 미만이면 
# 불합격을 출력하세요

score_1 = int(input('1번째 성적을 입력하세요 : '))
score_2 = int(input('2번째 성적을 입력하세요 : '))
score_3 = int(input('3번째 성적을 입력하세요 : '))

# 총점 처리
tot = score_1 + score_2 + score_3
# 평균 처리
avg = tot / 3

# 평균 점수에 따라 합격/불합격 처리
if avg >= 90 : 
    print('합격입니다.')
else :
    print('불합격입니다.')












