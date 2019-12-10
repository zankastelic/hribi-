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

# te generirani_linki so vsi pravi in delujoči
# ma sej ubsitvu sploh ne rabmo zapisat? 


for link in generirani_linki:
    content = requests.get(link).content
    page = BeautifulSoup(content, 'html.parser')
    vsebina_z_gorami = page.find(id='gorovjaseznam')
    linki = vsebina_z_gorami.find_all('a')[3:]

    podlinki = []

    for x in linki:
        x =  root_url + x['href']
        podlinki.append(x)
#print("dela")

outV = open("vrhovi.txt","w")
for x in podlinki: 
    outV.write(x)
    outV.write("\n")
outV.close()

# ker mi for zanka ne deluje bom sprobal vsakega zapisati posebaj --- za vsako gorovje posebi: 

#content0 = requests.get(generirani_linki[0]).content
#page0 = BeautifulSoup(content0, 'html.parser')
#vsebina_z_gorami0 = page0.find(id='gorovjaseznam')
#linki0 = vsebina_z_gorami0.find_all('a')[3:]

#podlinki0 = []

#for x in linki0:
#    x =  root_url + x['href']
#    podlinki0.append(x)

#print('delajo podlinki 0')

# nevem zakaj mi vsak link dvakrat vn vrže: 

#podlinki0 = list(dict.fromkeys(podlinki0)) 

# bom sprobu vse skupi sprobu: 
vsi_podlinki = [] 
for x in range(len(generirani_linki)): 
    content = requests.get(generirani_linki[x]).content
    page = BeautifulSoup(content, 'html.parser')
    vsebina_z_gorami = page.find(id='gorovjaseznam')
    linki = vsebina_z_gorami.find_all('a')[3:]

    for y in linki:
        y =  root_url + y['href']
        vsi_podlinki.append(y)

vsi_podlinki = list(dict.fromkeys(vsi_podlinki)) 

outVSI = open("VSI_vrhovi.txt","w")
for x in vsi_podlinki: 
    outVSI.write(x)
    outVSI.write("\n")
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



