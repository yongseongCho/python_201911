# -*- coding: utf-8 -*-

# 지역변수와 전역변수 그리고 함수
# 지역변수 : 함수 내부에 선언된 모든 변수
# 전역변수 : 함수 외부에 선언된 모든 변수

# 전역변수로 선언된 변수는 
# 모든 함수 내부에서 
# 자유롭게 접근할 수 있는 변수입니다.

# 전역변수 선언
count = 0

def add() :
    # 전역변수 count 접근하기 위한 선언
    # global 전역변수명
    global count
    count += 1
    print(f'add.count -> {count}')
    
add()

print(f'count -> {count}')