dados = []
time = []
print(f'{'Lists de Jogadores':-^30}')
while True:
    nome = str(input('Nome do Jogador: '))
    qntp = int(input(f'Quantas partidas {nome} jogou? '))
    cont = 0
    dados.append([nome,qntp])
    golsp = []
    while cont < qntp:
        gols = int(input(f'Gols na partida {cont +1}: '))
        cont += 1
        golsp.append(gols)
    dados.append(golsp)
    time.append(dados[:])
    dados.clear()
    per = str(input('Quer continuar ? [S/N]')).upper().strip()
    if per == 'N':
        break

print('=-'*30)
print(f'{'cod': <5}{'nome': <10}{'gols':<10}{'total':>10}')
for indice, pessoa in enumerate(time):
    print(f'{indice: <5}{pessoa[0][0]:<10}{str(pessoa[1]):<10}{sum(pessoa[1]):>8}')

while True:
    try:
        print('=-' * 30)
        per = int(input('Deseja ver qual indice? [999 para sair]  '))
        if per == 999:
            break
        elif per < len(time):
            print(f'Levantamentos do jogador {time[per][0][0]}')
            for i in range(0,len(time[per][1])):
                if time[per][1][i] != 1:
                    print(f'No jogo {i + 1} fez {time[per][1][i]} gols.')
                else:
                    print(f'No jogo {i + 1} fez 1 gol')
    except ValueError:
        continue

