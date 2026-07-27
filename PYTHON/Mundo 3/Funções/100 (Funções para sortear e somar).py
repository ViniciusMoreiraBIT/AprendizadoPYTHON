'''Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números
e vai coloca-los dentro da lista e a segunda função vai mostrar a soma
de todos os valores PARES sorteados pela função anterior.'''

from random import randint
from time import sleep

# Minha resolução ↓
numeros = []

# def sorteia(li):
#     print('Sorteando 5 valores da lista: ', end='')
#     for i in range(0,5):
#         li.append(randint(1,10))
#         print(li[i], end=' ')
#     print('PRONTO!')
#
# def somaPar(li):
#     soma = 0
#     for v in li:
#         if v % 2 == 0:
#             soma += v
#     print(f'Somando os valores PARES de {numeros}, temos {soma}')
#
# sorteia(numeros)
# somaPar(numeros)

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='')
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores PARES de {lista}, temos {soma}')

numeros = []

sorteia(numeros)
somaPar(numeros)


