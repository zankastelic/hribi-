#regularni izrazi

import csv
import json
import os
import requests
import sys
import re
import orodja

#with open('vsebina_spletnih_strani.txt', encoding='utf-8') as f:
#    vsebina = f.read()

vzorec = (
    r'<title>([\D|\s]+)<\/.*e>\s*'#ime
    r'[\s|\D|\d]*'
    r'<tr>.*[0-9]>(?P<drzava>\D*?)<\/a.*tr>\s*' #država
    r'<tr>.*">(?P<gorovje>\D*?)<.*<\/tr>\s*'  #gorovje
    r'<tr>.*\s(?P<visina>\d{0,4}).*tr>\s*'  #višina
    r'[\s|\D|\d]*' 
    r'<tr><td><b>Vrs.*b>\s(?P<vrsta>\D.*)<\/td.*\s*' #vrsta
    r'[\s|\D|\d]*'
    r'<tr>.*<b>Ogledov.*b>\s(?P<ogledi>\d*)<.*tr>\s*' #ogledi 
    r'<tr.*Pr.*b>\s(?P<priljubljenost_v_procentih>\d{1,2})%.' #priljubljenost %
    r'.(?P<mesto_priljubljenosti>\d{1,5}).*tr>\s*' # priljubljenost (mesto) 
    r'<tr.*Št.*">(?P<stevilo_poti>\d+)<\/a>.*tr>\s*' #število poti
    r'[\s|\D|\d]*'
    r'<tr.*"justify">(?P<opis>[\s|\D|\d]*)\s<\/p><\/td><\/tr>' #opis gore 
)

vzorec_1 = (r'<title>(?P<ime>.*?)</title>.*?<a class=moder href=.*?>(?P<drzava>.*?)</a>')

# hribi = []
# for zadetek in re.finditer(vzorec_1, vsebina):
#     hribi.append(zadetek.groupdict())



# with open('hribi.json', 'w') as f:
#     json.dump(hribi, f, indent=2)
# f.close()

# with open('hribi.csv', 'w', encoding='utf-8') as csv:
#     #writer = csv.DictWriter(csv, fieldnames=['ime', 'država', 'gorovje', 'višina', 'vrsta', 'ogledi', 'priljubljenost_[%]', 'priljubljenost_[mesto]', 'število_poti', 'opis_gore'])
#     writer = csv.DictWriter(csv, fieldnames=['ime', 'država'])
#     writer.writeheader()
#     for x in hribi:
#         writer.writerow(x)
# csv.close() 

ime_datoteke = 'vsebina_spletnih_strani.html'

def pridobi_podatke_o_oglasih(ime_datoteke):
    #seznam_oglasov = posamezni_oglasi(ime_datoteke)  #seznam po oglasih
    slovar_iskanih_podatkov = []
    stevec = 0
    n = 100
    while n > 0:
        for zadetek in re.finditer(vzorec_1, ime_datoteke):
            slovar_zadetkov = zadetek.groupdict()
            slovar_iskanih_podatkov.append(slovar_zadetkov)
            stevec += 1
            n -= 1
            #print(stevec)
    print(stevec, slovar_iskanih_podatkov)

    orodja.zapisi_csv(slovar_iskanih_podatkov, ['naslov', 'podnaslov'], 'hribi1.csv')
    print('končano:', len(slovar_iskanih_podatkov))

    orodja.zapisi_json(slovar_iskanih_podatkov, 'hribi3.json')

