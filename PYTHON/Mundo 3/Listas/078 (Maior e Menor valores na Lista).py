'''Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.'''

#Minha resolução ↓
'''num = []

for i in range (0,5):
    num.append(int(input(f'Digite um valor para a posição {i}: ')))

# Criar variavel com max/min reduz o consumo de memoria se for usar repetidamente.
maior = max(num)
menor = min(num)

print('Você digitou os valores ', *num)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num):
    if maior == num[i]: #criei um enumerate mas nem usei o "v"
        print(f'{i}..', end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num):
    if menor == v: #usando o v
        print(f'{i}..', end=' ')

#for i in range(0,5):
#   if max(num) == num[i]: #sem usar o v
#       print(i)'''

listanum = []
maior = menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum [c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]
print('=-'* 30)
print('Você Digitou os valores :', *listanum)
print(f'O Maior valor digitado foi: {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO Menor valor digitado foi: {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')