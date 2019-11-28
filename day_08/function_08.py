# -*- coding: utf-8 -*-

# 함수의 매개변수 선언 시, 기본값을 지정하는 방법

# def 함수명(매개변수명 = 기본값)
# 기본값이 지정된 매개변수는 함수의 호출 시,
# 값을 전달하지 않아도 정상적으로 실행될 수 있습니다.
# (기본값을 사용하여 실행)

def calculator(n1, n2, operator='+', is_print=False) :
    r = n1
    
    if operator == '+' :
        r += n2
    elif operator == '-' :
        r -= n2
    elif operator == '*' :
        r *= n2
    elif operator == '/' :
        r /= n2
    elif operator == '%' :
        r %= n2

    if is_print :
        print(f'{n1} {operator} {n2} = {r}')
    
    return r

result = calculator(10, 5, '+', False)
print(result)

calculator(10, 20, '*', True)

result = calculator(10, 5)
print(result)

# 함수의 기본값이 활용되는 예제
print('Hello')
print('Python')

# print 함수의 종료 후, 개행하지 않고 공백을 추가
print('Hello', end=' ')
print('Python')

# print 함수의 출력 값이 다수개 인 경우
# 각 값 사이에 출력할 문자열을 제어하는 예제
print(1, 2, 3)
print(1, 2, 3, sep=', ')

file_name='./print_function_test.txt'
f = open(file_name, 'w')

print('Hello Python~!')
# print 함수의 출력을 파일로 변경하는 예제 코드
# - 파일에 즉시 출력되지 않음
print('Hello Python~!', file=f)

f.close()

f = open(file_name, 'w')
# print 함수의 출력을 파일로 변경하는 예제 코드
# - 파일에 즉시 출력됨
print('Hello Python~!', file=f, flush=True)

f.close()








