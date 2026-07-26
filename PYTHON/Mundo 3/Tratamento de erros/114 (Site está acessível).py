'''Crie um código em Python que teste se o site Pudim
está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.python.org')
# except Exception as erro:
#     print('Deu erro!')
#     print(erro) ← verificando qual é o erro que deu com o site do exercício Pudim
except urllib.error.URLError:
    print('Deu erro!')
else:
    print('Consegui acessar o site com sucesso!')
