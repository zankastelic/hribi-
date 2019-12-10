from bs4 import BeautifulSoup
import requests
import csv


root_url = 'https://www.hribi.net'

with open('table.txt', 'r') as f:
    lines = f.readlines()
    filtered = []
    for line in lines:
        line = line.strip()
        filtered.append(line)
    
    table = "".join(filtered) # zduzitev vrstic v datoteki v en string

tabela_gor = BeautifulSoup(table, 'html.parser')
linki = tabela_gor.find_all('a')

generirani_linki = []

for link in linki:
    link =  root_url + link['href']
    generirani_linki.append(link)
#print(generirani_linki)

# jih zapišemo 
# podatki, ki ji bomo zapisali --> generirani linki: 
outF = open("gorovja.txt","w")
for link in generirani_linki: 
    outF.write(link)
    outF.write("\n")
outF.close()

for link in generirani_linki:
    content = requests.get(link).content
    page = BeautifulSoup(content, 'html.parser')
    vsebina_z_gorami = page.find(id='gorovjaseznam')
    linki = vsebina_z_gorami.find_all('a')[3:]

    podlinki = []

    for x in linki:
        x =  root_url + x['href']
        podlinki.append(x)
print("dela")

outV = open("vrhovi.txt","w")
for x in podlinki: 
    outV.write(x)
    outV.write("\n")
outV.close()

#    for element in podlinki: 
#        content = requests.get(element).content
#        page = BeautifulSoup(content, 'html.parser')
#        podatki_vrha = page.find(id='vsebina')
#        info = podatki_vrha.find_all('b')
#        #for i in info:
#         #   print(i.parent.text.split(':'))
#
#        #print(podatki_vrha.prettify())
#        #opis = podatki_vrha.find_all('p')
#        #for o in opis:
#        #    print('boy')
#        #    print(o.parent)
#        poti = podatki_vrha.find_all('table')[2]
#        print(podatki_vrha)
#        break
#
#    break



