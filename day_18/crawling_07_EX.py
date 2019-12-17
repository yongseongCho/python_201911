# -*- coding: utf-8 -*-

import urllib.request as req

url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
html = req.urlopen(url)

from bs4 import BeautifulSoup as bs
soup = bs(html, 'html.parser')
#print(soup.prettify())

ranks = soup.findAll(name='div', 
                     attrs={'class':'tit3'})
#print(ranks)

for i, movie in enumerate(ranks) :
    if i < 10 :
        print(f'{i+1} : {movie.text.strip()}')
    else :
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    