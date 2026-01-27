'''Desenvolva um programa que leia o
primeiro termo e a razão de uma PA. No
final, mostre os 10 primeiros termos dessa progressão'''
'''p=1
pa=int(input('Número PA:'))
for i in range(0, 50, pa):
    if p <= 10:
        print(f'{p} Termo (a{p}) : {i}')
        p += 1'''

termo = int(input('Primeiro termo: '))
PA = int(input('Razão da PA: '))
for i in range (1, 11):
    valor = termo + (i - 1) * PA
    print(f'{i} Termo (a{i}): {valor}')
