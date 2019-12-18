# -*- coding: utf-8 -*-

# 네이버에서 '파이썬'으로 검색했을때 
# 반환되는 이미지 중, 상단의 10개를 다운로드받아
# 저장하는 코드를 작성하세요.

# 파이썬 키워드로 검색한 이미지의 목록 페이지 주소
page_url='https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'

import requests
# 이미지 목록 페이지의 HTML 문저를 수신
response = requests.get(page_url)

from bs4 import BeautifulSoup as bs
html=bs(response.text, 'html.parser')

images=html.findAll(name='img',
                    attrs={'class':'_img'})

# 이미지 태그들을 순회하며, 이미지의 주소값을 확인
# print(len(images))

import requests
session = requests.Session()

for i, img in enumerate(images[:10]) :
    #print(f'이미지 주소 : \n{img.attrs["data-source"]}')
    response = session.get(img.attrs["data-source"])
    with open(f'./download_file_03_{i}.jpg', 'wb') as f :
        f.write(response.content)











