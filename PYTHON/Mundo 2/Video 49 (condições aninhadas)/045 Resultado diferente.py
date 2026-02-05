from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
comp = randint(0, 2)
print('''1 = Pedra
2 = Papel
3 = Tesoura
''')

user=int(input('Escolha: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('=-'* 10)
print(f'''Você jogou: {itens[user - 1]}
Computador jogou: {itens[comp]}
''')
if comp == 0:
    if user == 1:
        print('EMPATE')
    elif user == 2:
        print('Você Ganhou!')
    elif user == 3:
        print('Computador Ganhou!')
elif comp == 1:
    if user == 1:
        print('Computador Ganhou!')
    elif user == 2:
        print('EMPATE')
    elif user == 3:
        print('Você Ganhou!')
elif comp == 2:
    if user == 1:
        print('Você Ganhou!')
    elif user == 2:
        print('Computador Ganhou!')
    elif user == 3:
        print('EMPATE')

