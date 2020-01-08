from bs4 import BeautifulSoup
import requests
import csv


root_url = 'https://www.hribi.net'

with open('table.txt', 'r') as f:
    lines = f.read()
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

# generirani_linki: ['https://www.hribi.net/gorovje/gorisko_notranjsko_in_sneznisko_hribovje/26', ...] 8 jih je 

podlinki = []

for link in generirani_linki:
    content = requests.get(link).content
    page = BeautifulSoup(content, 'html.parser')
    vsebina_z_gorami = page.find(id='gorovjaseznam')
    linki = vsebina_z_gorami.find_all('a')[3:]


    for x in linki:
        x =  root_url + x['href']
        podlinki.append(x)
print("delajo podlinki")




