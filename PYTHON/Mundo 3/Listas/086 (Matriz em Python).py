'''Crie um programa que cria uma matriz de dimensão 3x3 e preencha
com valores lidas pelo teclado.
No final, mostre a matriz na tela, com a formatação correta'''

#Minha resolução ↓
'''um = []
dois = []
tres = []

for i in range(0,9):
    if i <= 2:
        v = int(input(f'Digite o valor para [0, {i}]: '))
        um.append(v)
    elif i <= 5:
        v = int(input(f'Digite o valor para [1, {i - 3}]: '))
        dois.append(v)
    elif i <= 8:
        v = int(input(f'Digite o valor para [2, {i - 6}]: '))
        tres.append(v)

print('=-' * 30)
for i in um:
    print(f'[ {i} ]', end='')
print()
for i in dois:
    print(f'[ {i} ]', end='')
print()
for i in tres:
    print(f'[ {i} ]', end='')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0,3):
    for c in range(0,3):
        matriz[linha][c] = int(input(f'Digite um valor para [{linha},:{c}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()