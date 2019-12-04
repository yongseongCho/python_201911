# -*- coding: utf-8 -*-

numbers = [22,23,11,15,17,90,33]
result = list(filter(lambda n : n % 3 == 0, numbers))
print(result)

messages = ["Hello", "Index", "Python", "Hi"]
# 람다 식과 filter 함수를 사용하여
# messages 리스트의 요소 중, 첫 글자가
# H로 시작하는 값을 추출하세요.
result = list(filter(lambda m : m[0] == 'H', messages))
print(result)


# 매개변수로 전달된 값이 3의 배수인지 
# 확인하는 함수
#def check_3(n) :
#    return n % 3 == 0
##print(check_3(9))
#    
#result = list(filter(check_3, numbers))
#print(result)



# numbers 내부의 데이터 중, 3의 배수만 
# 반환하는 함수를 작성하세요
#def check(numbers) :
#    result = []
#    for n in numbers :
#        if n % 3 == 0 :
#            result.append(n)
#    return result
#
#print(check(numbers))

# numbers 내부의 데이터 중, 3의 배수만 
# result 리스트에 추가하는 반복문을 작성하세요
#result = []
#for n in numbers :
#    if n % 3 == 0 :
#        result.append(n)
#
#print(result)