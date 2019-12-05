# -*- coding: utf-8 -*-

# 구구단의 내용을 ./data/file_02_gugudan.txt에
# 출력하세요.

fname = './data/file_02_gugudan.txt'
output = open(fname, 'w')

# 파이썬에서는 리스트 타입의 객체를 활용하여
# 파일에 일괄적으로 출력할 수 있습니다.
output_data = []

for dan in range(2, 10) :    
    output_data.append(f'{dan}단을 출력합니다.')
    for mul in range(1, 10) :        
        output_data.append(f'{dan} * {mul} = {dan*mul}')

# 리스트 내부의 데이터를 사용하여
# 다수개의 문자열을 출력할 수 있는 기능
#output.writelines(output_data)
        
# 각 문자열에 개행문자를 추가하여 출력
output.writelines(
        map(lambda x : x + '\n',output_data))


#for dan in range(2, 10) :
#    #print(f'{dan}단을 출력합니다.')
#    output.write(f'{dan}단을 출력합니다.\n')
#    for mul in range(1, 10) :
#        #print(f'{dan} * {mul} = {dan*mul}')
#        output.write(f'{dan} * {mul} = {dan*mul}\n')

output.close()











