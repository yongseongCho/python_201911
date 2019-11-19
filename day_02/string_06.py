# -*- coding: utf-8 -*-

msg = 'Hello Python~!'

# 문자열의 길이를 반환하는 len 함수
msg_size=len(msg)
print('msg 문자열의 길이 : {}'.format(msg_size))

print('msg 문자열의 마지막 글자는 {}'.format(msg[msg_size-1]))
print('msg 문자열의 마지막 글자는 {}'.format(msg[-1]))

# 문자열 내부에 특정 문자열의 개수 확인
msg_count = msg.count('o')
print('msg_count : {}'.format(msg_count))

# 특정 문자열의 위치 확인 
# (인덱스 값 반환)
msg_find = msg.find('Python')
print('msg_find : {}'.format(msg_find))

print(msg[6:12])
print(msg[msg.find('Python'):12])
print(msg[msg.find('Python'):msg.find('Python') + len('Python')])

# 공백 제거
msg = '       Hello     Python~!     '
print('msg : {}'.format(msg))

# 문자열의 좌측 공백을 제거
msg_l = msg.lstrip()
print('msg_l : {}'.format(msg_l))

# 문자열의 우측 공백을 제거
msg_r = msg.rstrip()
print('msg_r : {}'.format(msg_r))

# 문자열의 양측 공백을 제거
msg_ = msg.strip()
print('msg_ : {}'.format(msg_))

print(msg.strip(' H!'))

# 문자열 치환(변경)
# 모든 공백 문자열을 빈문자열로 변경
msg_re = msg.replace(' ', '')
print(msg_re)

msg_re = msg.replace(' ', '', 7)
print(msg_re)

value_s = '$1,150.55'










