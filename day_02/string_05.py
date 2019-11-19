# -*- coding: utf-8 -*-

msg = "Hello Python~!"
print('msg -> {}'.format(msg))

# 문자열 슬라이싱
# 인덱스를 사용하여 특정 영역을 추출할 수 있는 연산
# [시작인덱스:종료인덱스]
# 종료인덱스는 포함되지 않습니다.
part = msg[0:5]
print('part -> {}'.format(part))

# 시작인덱스가 0인 경우 생략이 가능함
part = msg[:5]
print('part -> {}'.format(part))

part = msg[6:14]
print('part -> {}'.format(part))

# 종료지점까지 슬라이싱하는 경우
# 종료인덱스는 생략할 수 있음
part = msg[6:]
print('part -> {}'.format(part))






