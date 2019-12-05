# -*- coding: utf-8 -*-

# 파일에 내용을 추가하는 방법
output_file_name = './data/file_02.txt'

# open 함수의 결과를 대입받는 변수
# open 함수의 모드 매개변수에 따라서
# 파일의 내용을 읽거나(R), 파일에 내용을
# 추가할 수 있는 변수가 됩니다.
output = open(output_file_name, 'w')

# w 모드를 사용하여 파일을 open 하게 되면
# 해당 변수를 사용하여 데이터를 파일에 추가할 수
# 있습니다.(write 메소드를 사용)
output.write('파일 내용 작성 테스트~!')

# 파일과 같이 시스템의 리소스에 접근하는 경우
# 반드시 close 메소드를 호출하여
# 연결을 종료해야만 합니다.
output.close()














