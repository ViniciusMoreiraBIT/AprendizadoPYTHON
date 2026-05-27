'''Faça um programa que leia nome e meso de várias pessoas, guardando tudo em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas.
b)Uma listagem com as pessoas mais pesadas.
c)Uma listagem com as pessoas mais leves.'''

#Minha resolução ↓
'''pessoas = []
peso = []
dados = []

while True:
    n = str(input('Nome: '))
    p = float(input('Peso: '))
    pessoas.append(n)
    pessoas.append(p)
    peso.append(p)
    dados.append(pessoas[:])
    pessoas.clear()
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    while res not in 'NS':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res == 'N':
        break

maior = max(peso)
menor = min(peso)
cont = 0

print('=-' * 30)
print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for i in dados:
    if i[1] == maior:
        cont += 1
        if cont == 1:
            print(i[0], end='')
        elif cont > 1:
            print(f', {i[0]}', end='')
cont = 0

print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in dados:
    if p[1] == menor:
        cont += 1
        if cont == 1:
            print(p[0], end='')
        elif cont > 1:
            print(f', {p[0]}')
print()
print('=-' * 30)'''

temp = []
princ = []
maior = menor = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer contiunar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ',end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ',end='')