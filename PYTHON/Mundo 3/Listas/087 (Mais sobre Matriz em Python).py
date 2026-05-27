'''Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha'''

#Minha resolução ↓
'''um = []
dois = []
tres = []
pares = []

for i in range(0,9):
    if i <= 2:
        v = int(input(f'Digite o valor para [0, {i}]: '))
        um.append(v)
        if v % 2 == 0:
            pares.append(v)
    elif i <= 5:
        v = int(input(f'Digite o valor para [1, {i - 3}]: '))
        dois.append(v)
        if v % 2 == 0:
            pares.append(v)
    elif i <= 8:
        v = int(input(f'Digite o valor para [2, {i - 6}]: '))
        tres.append(v)
        if v % 2 == 0:
            pares.append(v)


print(pares)
print('=-' * 30)
for i in um:
    print(f'[ {i} ]', end='')
print()
for i in dois:
    print(f'[ {i} ]', end='')
print()
for i in tres:
    print(f'[ {i} ]', end='')

print()
print('=-' * 30)
print(f'A Soma dos valores pares é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {um[2] + dois[2] + tres[2]}')
print(f'O maior valor da Segunda linha é {max(dois)}')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0,3):
    for c in range(0,3):
        matriz[linha][c] = int(input(f'Digite um valor para [{linha},{c}]: '))
print('-=' * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-='*30)
print(f'A soma dos valores pares é {spar}')
for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')