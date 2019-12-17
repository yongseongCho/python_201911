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

tag_td = soup.td
print(f'tag_td -> {tag_td}')
print(f'tag_td.attrs -> {tag_td.attrs}')
print(f'tag_td.attrs["class"] -> {tag_td.attrs["class"]}')

tag_a = soup.a
print(f'tag_a -> {tag_a}')
print(f'tag_a.attrs -> {tag_a.attrs}')
print(f'tag_a.attrs["href"] -> {tag_a.attrs["href"]}')
print(f'tag_a.attrs["title"] -> {tag_a.attrs["title"]}')













