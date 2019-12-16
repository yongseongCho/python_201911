# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

x = list(range(1,6))
y = list(range(10,51,10))

plt.title('bar chart example')
plt.xlabel('x label')
plt.ylabel('y label')

# BAR 형태의 차트 생성 방법
# bar, barh 함수를 사용
# bar(가로방향), barh(세로방향)
# bar(x데이터, y데이터)

# 참고사이트
# https://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.bar

# alpha 속성은 투명도 지정
# (0 ~ 1)
plt.barh(x, y, color='red', alpha=0.5)
plt.show()










