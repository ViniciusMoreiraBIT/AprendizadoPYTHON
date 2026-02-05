'''Faça um programa que leia o peso de
cinco pessoas. No final, mostre qual foi o
maior e o menor peso lidos.'''

'''peso = []
for i in range(1,6):
    p=float(input(f'Peso da {i}º pessoa: '))
    peso.append(p)

print(f'O Maior peso lido foi: {max(peso)}')
print(f'O Menor peso lido foi: {min(peso)}')

del peso[int(input('Deletar: '))-1]

print(peso)
print(f'O Maior peso lido foi: {max(peso)}')
print(f'O Menor peso lido foi: {min(peso)}')

for i in peso:
    print(i)'''

maior = 0
menor = 0
for i in range(1 , 7):
    peso = float(input(f'Peso da {i} pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    else:
        menor = peso
print(f'O menor peso lido foi → {menor}Kg')
print(f'O maior peso lido foi → {maior}Kg')