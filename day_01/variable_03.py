# -*- coding: utf-8 -*-

# 관계연산자
# 좌항과 우항의 비교를 통한 값을 반환하는 연산자
# 관계연산자의 반환 값은 bool 타입입니다.
# (True, False의 값이 반환됨)

n1 = 10
n2 = 5

r = n1 > n2
print('{0} {1} {2} = {3}'.format(n1, '>', n2, r))

r = n1 < n2
print('{0} {1} {2} = {3}'.format(n1, '<', n2, r))

# >= : 이상
r = n1 >= n2
print('{0} {1} {2} = {3}'.format(n1, '>=', n2, r))

# <= : 이하
r = n1 <= n2
print('{0} {1} {2} = {3}'.format(n1, '<=', n2, r))

r = n1 == n2
print('{0} {1} {2} = {3}'.format(n1, '==', n2, r))

r = n1 != n2
print('{0} {1} {2} = {3}'.format(n1, '!=', n2, r))





