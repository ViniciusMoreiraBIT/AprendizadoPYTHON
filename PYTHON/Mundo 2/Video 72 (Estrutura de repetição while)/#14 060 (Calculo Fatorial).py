'''Faça um programa que leia um número qualquer
e mostre o seu fatorial.

Ex:.
5! = 5x4x3x2x1 = 120'''

#Minha resolução ↓
'''n = int(input('Número: '))
fat = n - 1
soma = n
print(n, end= '')
while fat >= 1:
    soma *= fat
    #print(f' x {fat}'if fat > 1 else ' = ', end='')
    print(f' x {fat}', end='')
    fat -= 1
print(f' = {soma}')
print(f'\nO fatorial de {n} é {soma}')'''

n = int(input('Número do Fatorial: '))
cont = n
fat = 1
while cont > 0:
    print(cont,end='')
    print(f' x 'if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print(fat)

#Resolução usando biblioteca Math
'''from math import factorial
n = int(input('Número: '))
fat = factorial(n)
print(fat)'''