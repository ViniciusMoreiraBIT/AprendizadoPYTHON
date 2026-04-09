'''Cire um programa que simule o funcionamento de um caixa eletrônico. No
início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa var informar quantas células de cada valor serão entregues.

OBS:. Considere que o caixa possui células de 50,20,10,1'''

#Minha Resolução ↓
'''valor = int(input('Valor: R$ '))
c = v = d = u = 0
while True:
    while valor >= 50:
        c += 1
        valor -= 50
    while valor >= 20:
        v += 1
        valor -= 20
    while valor >= 10:
        d += 1
        valor -= 10
    while valor >= 1:
        u += 1
        valor -= 1
    break

c >= 1 and print(f'{c} notas de 50.')
v >= 1 and print(f'{v} notas de 20.')
d >= 1 and print(f'{d} notas de 10.')
u >= 1 and print(f'{u} notas de 1.')'''

print('=' * 30)
print(f'{'BANCO DO VINI':-^30}')
print('=' * 30)
valor = int(input('Que valor você quer sacar ? R$ '))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'{totalced} notas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break



