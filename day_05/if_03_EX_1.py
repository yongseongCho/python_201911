# -*- coding: utf-8 -*-

# 사용자에게 주민번호 7번째 자리수를 입력받아
# 성별을 출력하는 코드를 작성하세요.

gender_code = int(input('주민번호 7번째 자리수를 입력하세요 : '))

# 1, 3 : 남성
# 2, 4 : 여성
if gender_code == 1 or gender_code == 3 :
    print('당신은 남성입니다.')
else :
    print('당신은 여성입니다.')











