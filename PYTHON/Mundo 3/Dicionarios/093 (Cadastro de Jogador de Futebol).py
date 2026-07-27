'''Crie um programa que gerencie o aproveitamento de um
jogador de futbol. O programa vai ler o nome do
jogador e quantas partidas ele jogou. Depois vai ler
a quantidade de gols feitos em cada partida. No final,
tuso isso será guardado em um dicionário, incluindo
o total de gols feitos durante o campeonato.'''

# Minha resolução ↓
'''jogador = {}
gols = []

jogador['Nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou?'))
for i in range(1, partidas + 1):
    gol = int(input(f'Quantos gols na partida {i}? '))
    gols.append(gol)

jogador['gols'] = gols.copy()
jogador['total'] = sum(gols)

print('=-' * 30)
print(jogador)
print('=-' * 30)

for c, v in jogador.items():
    print(f'No campo {c} tem o valor {v}.')
print('=-' * 30)

print(f'O jogador {jogador['Nome']} jogou {partidas} partidas.')
for i in range(1, partidas + 1):
    print(f'    =>Na partida {i}, fez {gols[i - 1]} gols.')
print(f'Foi um total de {jogador['total']} gols.')'''

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador['nome']} jogou ? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols da patida {c + 1}? ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

print('=-' * 30)
print(jogador)
print('=-' * 30)

for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}')

print('=-' * 30)
print(f'O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'    =>Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')