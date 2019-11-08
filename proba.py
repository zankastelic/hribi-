from bs4 import BeautifulSoup
import requests

root_url = 'https://www.hribi.net/gorovja'

resp = requests.get(root_url)
content = resp.content

page = BeautifulSoup(content, 'html.parser')

vsebina_z_gorami = page.find(id='vsebina')
glavna_tabela = vsebina_z_gorami.find('table')
tabela_z_gorami = glavna_tabela.find_all('table')[1]
linki = tabela_z_gorami.find_all('a')

# print(tabela_z_gorami.prettify()), olepsa izpis

print(tabela_z_gorami)