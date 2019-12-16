#regularni izrazi

import csv
import json
import os
import requests
import sys
import re

with open('vsebina_spletnih_strani.txt', encoding='utf-8') as f:
    vsebina = f.read()

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

x = 0
hribi = []
for zadetek in re.finditer(vzorec, vsebina):
    hribi.append(zadetek.groupdict())
    x += 1
print(x)