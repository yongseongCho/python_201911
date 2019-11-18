# -*- coding: utf-8 -*-

# 주석문 : 소스 코드의 설명을 위해서 
# 사용되는 설명문

"""
여러
라인에
걸친
설명문
"""

# 변수의 선언
number = 10
number = 15

# 출력문 사용
# - print 함수를 사용
print(number)

print("Hello Python~!")
print('오늘은 {0}월 {1}일 입니다.'.format(11, 18))

import tkinter as tk

window=tk.Tk()
window.title('Hello Python Window')
window.geometry('300x300+300+300')
window.resizable(False, True)
window.mainloop()













