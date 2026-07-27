'''Crie um programa onde o usúario possa digitar sete valores
numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e impares. No final, mostre
os valores pares e ímpares em ordem crescente.'''

#Minha resolução ↓
'''numeros = []

cont = 0
for i in range (0,7):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        numeros.append(n)
    elif n % 2 == 1:
        numeros.insert(0,n)
        cont += 1

numeros = numeros[0:cont],numeros[cont:]

numeros[1].sort()
numeros[0].sort()

print('=-' * 30)
print(f'Os valores pares digitados foram: {numeros[1]}')
print(f'Os valores impares digitados foram: {numeros[0]}')'''

num = [[],[]]
valor = 0
for i in range(1, 8):
    v = int(input(f'Digite o {i}º valor: '))
    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)

print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'OS valores impares digitados foram: {num[1]}')