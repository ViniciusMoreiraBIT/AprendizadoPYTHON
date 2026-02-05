'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com dua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se ele ja passou tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou passou do prazo'''
from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
#idade = date.today().year - ano
#idade= 2026 - ano
print(f'Idade: {idade}')
if idade < 18:
    print(f'Falta {18 - idade} anos para seu alistamento, será em {date.today().year - (idade - 18)}') # 2026 - (-numero) = menos com menos +
elif idade == 18:
    print('Esse ano você tem que se apresentar no Serviço Militar de sua região.')
else:
    print(f'Ja passou {idade - 18} Anos do tempo de você se alistar, seu alistamento foi em {atual - (idade - 18)}')