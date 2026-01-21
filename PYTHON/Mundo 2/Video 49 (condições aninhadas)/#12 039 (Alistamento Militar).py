'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com dua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é a hora de se alistar.
-Se ele ja passou tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou passou do prazo'''

ano = int(input('Ano de nascimento: '))
idade= 2025 - ano
print(f'Idade: {idade}')
if idade < 18:
    print(f'Falta {18 - idade} anos para seu alistamento.')
elif idade == 18:
    print('Esse ano você tem que se apresentar no Serviço Militar de sua região.')
elif idade > 18:
    print('Já passou do tempo se você se alistar, procure imediatamente o Serviço militar de sua cidade!')