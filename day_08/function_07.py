# -*- coding: utf-8 -*-

# 매개변수가 정해지지 않은 경우 주의할 사항
# (매개변수가 고정되어 있지 않은 경우)

def calculator(*numbers, operator) :
    result = 0
    
    for n in numbers :
        if operator == '+' :
            result += n
        elif operator == '-' :
            result -= n
            
    return result

# 아래의 코드는 numbers 매개변수로 인해서
# "+" 문자를 operator 에 대입할 수 없어
# 실행 시 에러가 발생
#r = calculator(10, 20, 50, '+')
#print(f'r -> {r}')

# 동적인 매개변수 이후에 또다른 매개변수가
# 선언된 경우 반드시 명시적으로 매개변수의
# 이름을 통해 값을 전달해야 합니다.
r = calculator(10, 20, 50, operator='+')
print(f'r -> {r}')








