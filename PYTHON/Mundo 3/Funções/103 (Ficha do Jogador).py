'''Faça um programa que tenha uma função chamda ficha(),
que receba dois parâmetros opcinais: o nome de um jogador
e quantos gols ele marcou.
 O programa deverá ser capaz de mostrar a ficha do
jogador, mesmo que algum dado não tenha sido informado
corretamente.'''

#Minha resolução ↓
# def ficha(n='<desconhecido>',g=0):
#     print(f'O jogador {n} fez {g} gol(s) no campeonato.')
#
#
# print('-' * 30)
# nome = input('Nome do jogador: ')
# gols = input('Números de gols: ')
# if nome == '' and gols == '':
#     ficha()
# elif nome == '':
#     ficha(g = int(gols))
# elif gols == '':
#     ficha(nome)
# else:
#     ficha(nome,int(gols))

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols no campeonato.')

n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)