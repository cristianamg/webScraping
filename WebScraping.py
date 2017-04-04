import bs4 as bs
import urllib.request
import re
from lxml import etree
SafeLink = []
listanueva = []
AllURL=[]

URL = urllib.request.urlopen('https://www.encuentra24.com/costa-rica-es/autos-motos').read()
soup = bs.BeautifulSoup(URL, 'lxml')
for URL in soup.findAll('a', {'class': 'ann-box-title'}):
    LinkHref = (URL.get('href'))
    SafeLink.append(LinkHref)
    ListCast = list(set(SafeLink))
for i in ListCast:
    listanueva.append('https://www.encuentra24.com/'+i)
for i in listanueva:
    print(i)
print("Licalizacion,  Marca, Modelo,   Enviado,    Precio,     Año,  Kilometros,  Motor")
for i in listanueva:
    sauce2 = urllib.request.urlopen(i).read()
    soup2 = bs.BeautifulSoup(sauce2, 'lxml')
    ListTemporal = []
    ListTempora2 = []
    for f in soup2.findAll('span', {'class': 'info-name'}):
        ListTempora2.append(f.text)
    for f in soup2.findAll('span', {'class': 'info-value'}):
        ListTemporal.append(f.text)
        AllURL.append(ListTemporal)
print(AllURL)
