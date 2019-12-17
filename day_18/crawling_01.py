# -*- coding: utf-8 -*-

# BeautifulSoup : HTML과 같이 태그 기반의 문서를 손쉽게
# 파싱(문자열 추출)할 수 있는 모듈
# 일반 XMl 문서도 파싱할 수 있음

# conda install beautifulsoup4
from bs4 import BeautifulSoup as bs

# HTML 문서의 표본
html = '''
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=181710" 
        title="포드 V 페라리">포드 V 페라리</a>
    </div>
</td>
'''

# BeautifulSoup 객체 생성
# BeautifulSoup(HTML문서, 문서파서)
# 생성된 BeautifulSoup 객체는 HTML문서의 요소들에
# 접근할 수 있는 객체가 됨
soup = bs(html, 'html.parser')

# BeautifulSoup 객체를 활용하여 각 태그에
# 접근하는 방법
# 접근연산자 (.)을 활용
# BeautifulSoup객체.태그명
# - 현재 문서의 내용에서 첫번째 태그를 추출
# - 특정 태그가 다수개 존재하는 경우 최초의
#   하나만 접근하게 됨
# - 해당 태그의 시작부터 종료 태그까지 추출함
tag_td = soup.td
print(f'tag_td -> {tag_td}')

tag_div = soup.div
print(f'tag_div -> {tag_div}')

tag_a = soup.a
print(f'tag_a -> {tag_a}')

# 태그의 이름을 추출하는 name 속성
print(f'tag_a.name -> {tag_a.name}')
# 태그의 문자열을 추출하는 text 속성
print(f'tag_a.text -> {tag_a.text}')





















