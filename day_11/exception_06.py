# -*- coding: utf-8 -*-

# 다수개의 예외가 발생할 가능성이 있는 코드입니다.
# 각각의 예외를 처리할 수 있도록 코드를 수정해보세요

# 여러 타입의 예외를 처리하기 위한 방법
# except 첫번째 예외 타입 as 변수명
#   첫번째 예외 타입이 발생한 경우의 실행 코드
# except 두번째 예외 타입 as 변수명
#   두번째 예외 타입이 발생한 경우의 실행 코드
# ...

# except Exception as 변수명
#   상단에 위치한 except 에서 예외가 처리되지 못한 경우
#   실행할 실행 코드

numbers = []

try :

    for i in range(1,3) :
        numbers.append(
                int(input(f'{i}번째 정수 : ')))
    
    numbers.append(numbers[0] / numbers[1])
    print(f'{numbers[0]} / {numbers[1]} = {numbers[3]}')

except ZeroDivisionError :
    print('예외 : 0으로 나눌 수 없습니다.')
except IndexError :
    print('예외 : 잘못된 인덱스를 사용했습니다.')
# 주의사항 
# Exception을 처리하는 except 선언은
# 모든 except 선언문의 최하단에 위치해야만합니다.
except Exception as msg :
    print(f'예외 : {msg}')






