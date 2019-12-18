# -*- coding: utf-8 -*-

# 네이버 영화 랭킹 페이지의
# 1 ~ 10위까지의 포스터 이미지 다운로드

import requests
import urllib.request as req
from bs4 import BeautifulSoup as bs

rank_url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
rank_page=req.urlopen(rank_url)
rank_html=bs(rank_page, 'html.parser')

rank_target_10=rank_html.findAll(name='div', 
                                 attrs={'class':'tit3'},
                                 limit=10)

for index, rank in enumerate(rank_target_10) :
    rank_title=rank.text.strip()
    rank_sub_url='https://movie.naver.com'
    rank_link=rank_sub_url + rank.a.attrs['href']
#    print(f'{index+1}. {rank_title} : {rank_link}')
    
    rank_sub_page=req.urlopen(rank_link)
    rank_sub_html=bs(rank_sub_page, 'html.parser')
    rank_sub_poster=rank_sub_html.find(name='div',
                                attrs={'class':'poster'})
    rank_img=rank_sub_poster.img
    rank_img_src=rank_img.attrs['src']
    
    #rank_img_src = rank_img_src.replace('?type=m77_110_2','')
    rank_img_src = rank_img_src.split('?')[0]
    
    print(f'{index+1}. {rank_title} : {rank_img_src}')
    
    session = requests.Session()
    response = session.get(rank_img_src)
    
    file_name = './' + rank_title + '.jpg'
    with open(file_name, 'wb') as f :
        f.write(response.content)
























