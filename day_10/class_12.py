# -*- coding: utf-8 -*-

# 구구단 클래스를 작성하세요.
# 구구단 클래스에는 두개의 메소드를 포함합니다.
# printAll 메소드와 printOne 메소드
# printAll 메소드는 매개변수가 없으며, 호출되면
# 전체 구구단을 출력
# printOne 메소드는 하나의 정수형 매개변수가 
# 있으며, 호출되면 전달된 매개변수의 구구단 출력

class GuGuDan :
    
    def printAll(self) :
        print('printAll 메소드 실행')
        for dan in range(2,10) :
            print(f'{dan}단을 출력합니다.')
            for mul in range(1, 10) :
                print(f'{dan} * {mul} = {dan*mul}')
                
    def printOne(self, dan) :
        print(f'{dan}단을 출력합니다.')
        for mul in range(1, 10) :
            print(f'{dan} * {mul} = {dan*mul}')

gugudan = GuGuDan()
#gugudan.printAll()
gugudan.printOne(3)









