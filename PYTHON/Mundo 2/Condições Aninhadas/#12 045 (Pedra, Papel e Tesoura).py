'''Crie um programa que faça o computador jogar Jokenpô com você'''
import random
from time import sleep
print('''1 = Pedra
2 = Papel
3 = Tesoura''')
computador = random.randint(1,3)
if computador == 1:
    computador= 'Pedra'
elif computador == 2:
    computador= 'Papel'
elif computador == 3:
    computador = 'Tesoura'

escolha = int(input('Escolha algum: '))
if escolha == 1:
    escolha= 'Pedra'
elif escolha == 2:
    escolha= 'Papel'
elif escolha == 3:
    escolha = 'Tesoura'
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print(' ')
print(f'''Você jogou: {escolha}
O computador jogou: {computador}''')
if escolha == computador:
    print('Deu Velha!')
elif escolha == 'Pedra' and computador == 'Tesoura':
    print('Você Ganhou!')
elif escolha == 'Papel' and computador == 'Pedra':
    print('Você Ganhou!')
elif escolha == 'Tesoura' and computador == 'Papel':
    print('Você Ganhou!')

elif computador == 'Pedra' and escolha == 'Tesoura':
    print('O PC Ganhou!')
elif computador == 'Papel' and escolha == 'Pedra':
    print('O PC Ganhou!')
elif computador == 'Tesoura' and escolha == 'Papel':
    print('O PC Ganhou!')
