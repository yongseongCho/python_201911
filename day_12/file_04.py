# -*- coding: utf-8 -*-

fname = './data/file_02_gugudan.txt'
input_file=open(fname, 'r')

# 파일의 내용을 한줄이 아닌 경우의 처리 방법
# readlines 메소드와 반복문을 활용하여 
# 처리할 수 있습니다.
input_data=input_file.readlines()
print(type(input_data))

# input_data 리스트 변수를 map 함수를 사용하여
# 각 리스트 내부의 값들에 포함된 개행문자를
# 제거하세요.
input_data = map(str.rstrip, input_data)

for s in input_data :
#    print(s, end='')
#    print(s.strip())
    print(s)

input_file.close()










