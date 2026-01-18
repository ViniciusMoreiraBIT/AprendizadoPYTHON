'''Escreva um programa que faça o computador "pensar" em um nuúmero inteiro entre 0 a 5 e peça
para o usuario tentar adivinhar qual foi o numero escolhido pelo computador.
 O programa devera escrever na tela se o usuário venceu ou perdeu'''
from random import randint
from time import sleep
n= randint(0,5) #Faz o computador sortear um numero de 0 a 5
print('-='*15)
print('Adivinhe o número de 0 a 5...')
print('-='*15)
res=int(input('Qual número eu pensei? '))
print('Processando...')
sleep(0.5)
if res <= 5:
    if res == n:
        print(f'Você Venceu! o número é {n}')
    else:
        print(f'Você Perdeu! o número é {n}')
    print('--FIM--')
else:
    print('Erro')