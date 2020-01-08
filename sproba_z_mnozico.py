from bs4 import BeautifulSoup
import requests
import csv
import os
import sys
import errno

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

print("sem končal")

# do tukaj je kul 

# gorovja niti ne rabmo zapisat v svoj .txt file 

# zdej bi radi da on nardi 8 datotek in v vsako shrani vse podlinke posameznega gorovja: 


def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)


print("sem končal drugič")

podlinki = set() # vsi linki vseh podstrani ---> sem dobil vse linke ------> množica =set()

for link in generirani_linki:
    content = requests.get(link).content
    page = BeautifulSoup(content, 'html.parser')
    vsebina_z_gorami = page.find(id='gorovjaseznam')
    linki = vsebina_z_gorami.find_all('a')[3:]


    for x in linki:
        x =  root_url + x['href']
        podlinki.add(x)
print("delajo podlinki")

#podlinki = list(dict.fromkeys(podlinki)) 

def shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False):
    '''Vsebino strani na danem naslovu shrani v datoteko z danim imenom.'''
    try:
        print('Shranjujem {} ...'.format(url), end='')
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke) and not vsili_prenos:
            print('shranjeno že od prej!')
            return
        r = requests.get(url)
        r.encoding='UTF-8'
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        pripravi_imenik(ime_datoteke)
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')

print('lahko delaš') 

# ustavaril bom imena datotek
imena_datotek = []
for x in range(len(generirani_linki)):
    niz = generirani_linki[x].split('/')[4]
    imena_datotek.append(niz)

print(imena_datotek)

outVSI = open("VSI_vrhovi_z_mnozico.txt","w")
for x in podlinki: 
    outVSI.write(x)
    outVSI.write("\n")
outVSI.close()

print('zdej jih je 1937')


for i, link in enumerate(podlinki):
    shrani_spletno_stran(link, 'files/' + link.split('/')[4]+ str(i) + '.txt')
    print(i)