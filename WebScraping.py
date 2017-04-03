
import bs4 as bs
import urllib.request
import re
from lxml import etree

sauce = urllib.request.urlopen('http://motos.coches.net/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
lisa_all = []
listanueva = []
for sauce in soup.findAll('a', href=True, title= True, xtclib= True):
  valores = (sauce.get('href'))
  lisa_all.append(valores)
  lst = list(set(lisa_all))
for i in lst:
        if "#ctrl_comments"not in i:
            if ".net" not in i:
                if ".aspx" not in i:
                    if len(i)>30:
                        listanueva.append('http://motos.coches.net'+i)
for i in listanueva:
    print(i)


for i in listanueva:
    sauce2 = urllib.request.urlopen(i).read()
    soup2 = bs.BeautifulSoup(sauce2, 'lxml')

    valor = soup2.find_next('ul').find_all('li')
    print(valor.text )

#//*[contains(concat( " ", @class, " " ), concat( " ", "ftresto1", " " ))]
