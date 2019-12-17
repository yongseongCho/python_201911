# -*- coding: utf-8 -*-

import urllib.request as req

html = req.urlopen('https://finance.naver.com/sise/lastsearch2.nhn')
print(html)

from bs4 import BeautifulSoup as bs
soup = bs(html, 'html.parser')

#print(soup)
#print(soup.prettify())

table = soup.find(name='table', attrs={'class':'type_5'})
#print(table)

company_names = table.findAll(name='a')

for i, name in enumerate(company_names) :
    print(f'{i+1} : {name.text}')
















