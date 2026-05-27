'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três geradas'''

nuns = []
#Minha resolução ↓
'''while True:
    nuns.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? [S/N] ')).strip().upper()
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()
    if res == 'S':
        continue
    else:
        break

par = []
impar = []
for i in nuns:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'A lista completa é: {nuns}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é: {impar}')'''

pares = []
impares = []
while True:
    nuns.append(int(input('Digite um número: ')))
    res = str(input('Quer continuar ? [S/N] '))
    if res in 'Nn':
        break

for i, v in enumerate(nuns):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'A lista completa é: {nuns}')
print(f'A lista de pares é: {pares}')
print(f'A lista de impares é: {impares}')