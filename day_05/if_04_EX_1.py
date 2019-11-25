# -*- coding: utf-8 -*-

# 3과목의 성적을 입력받아 총점과 평균
# 그리고 등급을 출력하세요
# 90 점이상 A, 80 점 이상 B ..

score_1 = int(input('1번째 성적 : '))
score_2 = int(input('2번째 성적 : '))
score_3 = int(input('3번째 성적 : '))

tot = score_1 + score_2 + score_3
avg = tot / 3

print(f'입력한 성적의 총점은 {tot} 점,')
print(f'평균은 {avg} 점 입니다.')

# null 값
# - 존재하지 않는 값
grade = None
if avg > 100 or avg < 0 :
    # 제어문의 영역을 실행하지 않고 넘어갈때
    pass
elif avg >= 90 :
    grade = 'A'
elif avg >= 80 :
    grade = 'B'
elif avg >= 70 :
    grade = 'C'    
elif avg >= 60 :
    grade = 'D'
else :
    grade = 'F'

# None 값을 체크하는 if문
# 파이썬에서 None 값은 False와 동일합니다.
if grade :
    print(f"성적의 등급은 '{grade}' 입니다.")
else :
    print('성적 점수를 확인하세요.')







