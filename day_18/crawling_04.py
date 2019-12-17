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
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=187349" 
        title="쥬만지: 넥스트 레벨">쥬만지: 넥스트 레벨</a>
    </div>
</td>
'''

soup = bs(html, 'html.parser')

# 접근연산자 또는 find 메소드는 
# 첫번째 발견된 문서 정보만 추출
tag_a = soup.a
print(f'tag_a -> {tag_a}')

tag_a = soup.find(name='a')
print(f'tag_a -> {tag_a}')

# BeautifulSoup 객체의 findAll 메소드
# 특정 태그, 또는 태그와 속성의 조합이 
# 다수개인 경우 활용할 수 있음
# find 메소드와 달리 동일한 형태의 태그를
# 모두 검색하여 리스트 형태로 반환
tags_a = soup.findAll(name='a')
print(f'tags_a -> {tags_a}')

# findAll 메소드는 리스트를 반환하므로
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













