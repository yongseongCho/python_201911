# -*- coding: utf-8 -*-

fname = './data/file_02.txt'

# 파일 READ 처리
# open 함수의 모드 매개변수를 r 로 실행하면
# 파일의 내용을 읽을 수 있는 객체가 반환됨
input_file = open(fname, 'r')

# open 함수의 모드 매개변수를 r 로 지정한 경우
# 반환된 객체의 readline 메소드를 활용하여
# 파일의 내용을 한 줄씩 읽어올 수 있습니다.
# 파일의 내용을 읽어오면 문자열로 처리됩니다.
input_line = input_file.readline()
print(input_line)

input_file.close()









