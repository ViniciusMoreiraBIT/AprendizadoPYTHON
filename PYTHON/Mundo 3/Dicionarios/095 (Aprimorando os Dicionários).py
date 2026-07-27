'''Aprimore o DESAFIO 093 para que ele funcione
com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de
cada jogador.'''

#Minha resolução ↓
'''jogadores = list()
dados = dict()
gols = []

while True:
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados['nome']} jogou? '))
    for i in range(0, partidas):
        gol = int(input(f'Quantos gols na partida {i + 1}? '))
        gols.append(gol)
    dados['gols'] = gols.copy()
    jogadores.append(dados.copy())
    gols.clear()
    per = str(input('Quer continuar ? [S/N] ')).upper()
    if per == 'N':
        break

print('=-' * 30)
print(f'{'cod': <5}{'nome': <10}{'gols':<15}{'total':>8}')
for i, v in enumerate(jogadores):
    print(f'{i:<5}{v['nome']:<10}{str(v['gols']):<15}{sum(v['gols']):>6}')
   #print(f'{i:<5}{v['nome']:<10}{v['gols']:<15}{sum(v['gols']):>8}')

while True:
    print('=-' * 30)
    per = int(input('Mostrar dados de qual jogador? '))
    if per == 999:
        break
    elif per >= len(jogadores) or per < 0:
        print(f'ERRO! Não existe jogador com código {per}! Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[per]['nome'].upper()}--')
        for i in range(0,len(jogadores[per]['gols'])):
            print(f'  No jogo {i + 1} fez {jogadores[per]['gols'][i]} gols.')

print('<< VOLTE SEMPRE >>')'''

time = []
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou ? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols da patida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = str(input('Quer continuar ? [S/N] ')).upper()
    while resp not in 'NS':
        resp = str(input('Quer continuar ? [S/N] ')).upper()[0]
    if resp == 'N':
        break

print('=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-' * 40)
for c, v in enumerate(time):
    print(f'{c:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

print(time)
while True:
    bus = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if bus == 999:
        break
    if bus >= len(time):
        print(f'Erro! Mão existe jogador com código {bus}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[bus]['nome'].upper()} --')
        for i, v in enumerate(time[bus]['gols']):
            print(f'   - No jogo {i + 1} fez {v} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')