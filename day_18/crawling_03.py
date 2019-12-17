# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as bs

html = '''
<td class="title">
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=181710" 
        title="포드 V 페라리">포드 V 페라리</a>
    </div>
</td>
'''

soup = bs(html, 'html.parser')

# BeautifulSoup 객체의 find 메소드
# 태그의 이름과 속성의 정보를 조합하여
# 검색하는 경우 활용
# - find 메소드는 검색 결과를 하나만 반환
# - 최초에 발견된 첫 번째 태그를 반환

# 첫 번째로 검색된 td 태그의 객체를 반환
tag = soup.find(name='td')
print(f'tag -> {tag}')

# 첫 번째로 검색된 a 태그의 객체를 반환
tag = soup.find(name='a')
print(f'tag -> {tag}')

# 첫 번째로 검색된 
# class 속성이 title인 객체를 반환
tag = soup.find(attrs={'class':'title'})
print(f'tag -> {tag}')

# 첫 번째로 검색된 
# class 속성이 tit3인 객체를 반환
tag = soup.find(attrs={'class':'tit3'})
print(f'tag -> {tag}')

# 첫 번째로 검색된 
# 태그의 이름이 td이고,
# class 속성이 tit3인 객체를 반환
# - 존재하지 않는 경우 None 값이 반환
tag = soup.find(name='td',
                attrs={'class':'tit3'})
print(f'tag -> {tag}')


















