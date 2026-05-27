'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear
6 números entre 1 a 60 para cada jogo, cadastrando tudo em uma lista composta'''

#Minha resolução ↓ (números repetem)
from time import sleep
from random import randint
'''jogos = []
print('-'*30)
print('JOGO DA MEGA SENA'.center(30))
print('-'*30)
per = int(input('Quantos jogos você quer que eu sorteie? '))
print(f' Sorteando {per} Jogos '.center(30,'='))

for i in range(1, per + 1):
    jogos = [randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60),randint(1,60)]
    jogos.sort()
    print(f'Jogo {i}: {jogos}')
    jogos.clear()
    sleep(1)
print(f'{' Boa Sorte ':=^30}')'''


lista = []
jogos = []
print('-'*30)
print('       JOGA NA MEGA SENA       ')
print('-'*30)
quant = int(input('Quantos jogos sortear? '))
tot = 0
while tot < quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)


