# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import urllib.request

url = 'https://www.pudim.com.br'
urllib.request.urlopen(url)