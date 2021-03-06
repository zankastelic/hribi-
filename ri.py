#regularni izrazi

import csv
import json
import os
import requests
import sys
import re
import orodja

with open('vsebina_spletnih_strani.html', encoding='utf-8') as f:
    vsebina = f.read()

vzorec = (
    r'<title>(?P<ime>[\D|\s]+)<\/.*e>\s*'#ime
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

hribi = []

for zadetek in re.finditer(vzorec, vsebina):
    hribi.append(zadetek.groupdict())

with open('hribi.json', 'w') as f:
    json.dump(hribi, f, indent=2)
f.close()

with open('hribi.csv', 'w', encoding='utf-8') as csv:
    writer = csv.DictWriter(csv, fieldnames=['ime', 'država', 'gorovje', 'višina', 'vrsta', 'ogledi', 'priljubljenost_[%]', 'priljubljenost_[mesto]', 'število_poti', 'opis_gore'])
    writer.writeheader()
    for x in hribi:
        writer.writerow(x)
csv.close()


