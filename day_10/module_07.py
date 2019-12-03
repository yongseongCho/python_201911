# -*- coding: utf-8 -*-

# 특정 모듈에 존재하는 변수/함수/클래스에
# 모듈명이나 별칭의 사용없이 접근하기 위한 방법
# from 모듈명 import 변수,함수,클래스명 
# - 모듈명 자체를 사용하지 않고 접근이 가능
#from module_05 import number, func_05, Class_05

# 아래와 같이 * 를 사용하는 경우 모든 요소를
# 모듈의 이름없이 사용할 수 있습니다.
from module_05 import *

# 별칭의 사용없이 특정 모듈의 변수/함수/클래스를
# 사용하는 예제
print(number)
func_05()
obj=Class_05()
del obj
