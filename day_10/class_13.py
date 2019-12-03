# -*- coding: utf-8 -*-

# 더하기 기능을 제공하는 PlusCalculator 클래스
# 를 작성하세요.
# PlusCalculator 클래스는 plus 메소드가 제공되며
# 정수 타입 두개를 매개변수로 전달받아
# 덧셈의 결과를 출력합니다.

class PlusCalculator :
    def plus(self, n1, n2) :
        r = n1 + n2
        print(f'{n1} + {n2} = {r}')

plus_cal = PlusCalculator()
plus_cal.plus(11, 9)

# PlusCalculator 클래스를 확장한 
# PlusMinusCalculator 클래스를 작성하세요.
# PlusMinusCalculator 클래스는 + 기능을 제공하는
# plus 메소드, - 기능을 제공하는 minus 기능이 제공됨

class PlusMinusCalculator (PlusCalculator) :
    def minus(self, n1, n2) :
        r = n1 - n2
        print(f'{n1} - {n2} = {r}')

pm_cal = PlusMinusCalculator()
pm_cal.plus(10, 7)
pm_cal.minus(10, 7)







