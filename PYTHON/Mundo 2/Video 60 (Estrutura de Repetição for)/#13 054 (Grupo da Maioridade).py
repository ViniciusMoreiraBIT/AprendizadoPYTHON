'''Crie um programa que leia o ano de
nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
'''p = []
idadee = []
for i in range(1, 7):
    ano = int(input(f'{i}º Ano de Nascimento: '))
    p.append(ano)
ma = 0
me= 0
for i in range(0,6):
    idade = 2026 - p[i]
    if idade < 18:
        print(f'{idade} Anos, ainda não atingiu a maioridade!')
        idadee.append(idade)
        me += 1
    else:
        print(f'{idade} Anos, Maior de idade!')
        idadee.append(idade)
        ma += 1

print(f'
{ma} pessoas de Maior.
{me} pessoas de Menor.')


for i in range(0 , len(idadee)):
    if idadee[i] >= 18:
        print(f'De maior:+ {idadee[i]}')
    else:
        print(f'De menor:- {idadee[i]}')'''

maior=0
menor=0
for i in range(0,6):
    ano = int(input(f'{i + 1} Ano de Nascimento: '))
    if 2026 - ano >= 18:
        maior += 1
    else:
        menor += 1

print(f'Maiores: {maior}')
print(f'Menores: {menor}')






