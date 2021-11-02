"""
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
"""

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print('\033[1;31mO site do Pudim não está disponível!\033[m')

else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())
