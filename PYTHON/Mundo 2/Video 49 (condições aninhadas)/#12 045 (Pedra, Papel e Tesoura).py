'''Crie um programa que faça o computador jogar Jokenpô com você'''
import random
from time import sleep
def joq():
    print('=-' * 15)
    print(' ')
    print(f'{game:=^30}')
    print(' ')
    print('=-' * 15)

def eu():
    if escolha == 1:
        print('Pedra')
    elif escolha == 2:
        print('Papel')
    elif escolha == 3:
        print('Tesoura')
    else:
        print('ERRO')
        exit()

def pc():
    if computador == 1:
        print('Pedra')
    elif computador == 2:
        print('Papel')
    elif computador == 3:
        print('Tesoura')

def resultado():
    if escolha == computador:
        print('Deu Velha!')
    elif escolha == 1 and computador == 3:
        print('Você Ganhou!')
    elif escolha == 2 and computador == 1:
        print('Você Ganhou!')
    elif escolha == 3 and computador == 2:
        print('Você Ganhou!')

    elif computador == 1 and escolha == 3:
        print('O PC Ganhou!')
    elif computador == 2 and escolha == 1:
        print('O PC Ganhou!')
    elif computador == 3 and escolha == 2:
        print('O PC Ganhou!')

game='JOKENPÔ'

joq()
print('''1 = Pedra
2 = Papel
3 = Tesoura''')
computador = random.randint(1,3)
escolha = int(input('Escolha algum: '))

eu() #def da minha escolha
print('  X')
sleep(1)
pc() #def escolha do PC
resultado() #def resultado do jogo
