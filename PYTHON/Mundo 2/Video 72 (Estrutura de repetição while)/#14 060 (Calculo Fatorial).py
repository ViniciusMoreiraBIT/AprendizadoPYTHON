'''Faça um programa que leia um número qualquer
e mostre o seu fatorial.

Ex:.
5! = 5x4x3x2x1 = 120'''

n = int(input('Número: '))
fat = n - 1
soma = n
print(n, end= '')
while fat >= 1:
    soma *= fat
    print(f' x {fat}', end='')
    fat -= 1
print(f' = {soma}')
print(f'\nO fatorial de {n} é {soma}')