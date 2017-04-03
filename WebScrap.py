import bs4 as bs
import urllib.request
import re
from lxml import etree

sauce = urllib.request.urlopen('https://www.encuentra24.com/costa-rica-es/autos-motos').read()
soup = bs.BeautifulSoup(sauce, 'lxml')
lisa_all = []
listanueva = []
lista2=[]
lista3=[]
for sauce in soup.findAll('a', {'class': 'ann-box-title'}):
    valores = (sauce.get('href'))
    lisa_all.append(valores)
    lst = list(set(lisa_all))
for i in lst:
    listanueva.append('https://www.encuentra24.com/'+i)
for i in listanueva:
    print(i)
print("Licalizacion,  Marca, Modelo,   Enviado,    Precio,     Año,  Kilometros,  Motor")
for i in listanueva:
    sauce2 = urllib.request.urlopen(i).read()
    soup2 = bs.BeautifulSoup(sauce2, 'lxml')
    lista4=[]
    for f in soup2.findAll('span', {'class': 'info-value'}):
        lista4.append(f.text)
        lista3.append(lista4)
print(lista3)


