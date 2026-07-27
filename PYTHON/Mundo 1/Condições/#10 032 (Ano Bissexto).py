'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO'''
from datetime import date
print('Coloque 0 para o ano atual')
ano=int(input('ANO: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano %400 == 0:
    print('\033[32m'+f'Ano {ano}','bissexto'.upper()+'\033[m')
else:
    print('\033[33m'+f'Ano {ano} Normal'+'\033[m')