# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs

# 동일한 형태의 태그가 반복되는 문자열 변수
# 일반적으로 아래와 같이 HTML 문서가 구성됨
html = '''
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=181710" 
        title="포드 V 페라리">포드 V 페라리</a>
    </div>
</td>
<a href="/movie/bi/mi/basic.nhn?code=181710" 
        title="포드 V 페라리(외부)">포드 V 페라리(외부)</a>
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=187349" 
        title="쥬만지: 넥스트 레벨">쥬만지: 넥스트 레벨</a>
    </div>
</td>
<a href="/movie/bi/mi/basic.nhn?code=187349" 
        title="쥬만지: 넥스트 레벨(외부)">쥬만지: 넥스트 레벨(외부)</a>
'''

soup = bs(html, 'html.parser')

# BeautifulSoup 사용법에 관련된 홈페이지 URL
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#

# 태그의 위치 정보를 활용하여 검색하는 방법
# select, select_one 메소드를 활용
# 아래의 경우 div 태그 하위에 위치한 a 태그를 검색
# - css의 선택자 문법을 사용하여 특정 태그 요소를 검색
tags_a = soup.select('div > a')
print(f'tags_a -> {tags_a}')

# select 메소드는 리스트를 반환하므로
# 인덱스를 활용하여 접근할 수 있음
print(f'tags_a[0] -> {tags_a[0]}')
print(f'tags_a[1] -> {tags_a[1]}')

# 각 a태그의 텍스트 정보를 추출
print(f'tags_a[0].text -> {tags_a[0].text}')
print(f'tags_a[1].text -> {tags_a[1].text}')

# 반복문을 활용하여 손쉽게 텍스트 등의
# 정보에 접근할 수 있음
for t in tags_a :
    print(f't.text -> {t.text}')    













