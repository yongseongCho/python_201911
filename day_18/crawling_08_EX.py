# -*- coding: utf-8 -*-

import urllib.request as req

url='https://www.naver.com/'
html = req.urlopen(url)

from bs4 import BeautifulSoup as bs
soup = bs(html, 'html.parser')
#print(soup.prettify())

ul=soup.find(name='ul',attrs={'class':'ah_l'})

ranks=ul.findAll(name='span', 
                   attrs={'class':'ah_r'})
contents=ul.findAll(name='span', 
                   attrs={'class':'ah_k'})

#print(len(ranks))
#print(ranks)

for r, c in zip(ranks, contents) :
    print(f'{r.text.strip()} : {c.text.strip()}')














