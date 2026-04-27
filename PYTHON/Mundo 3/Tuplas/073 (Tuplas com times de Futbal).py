'''Crie uma tupla preenchida coms os 20 primeiros colocados da tabela do Campeonato Brasileiro
de Futebal, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os últimos 4 colocados da tabela.
c) Uma lista com times em ordem alfabética.
d) Em que posição na tabela está o time da Chapecoence.'''

#Minha resolução ↓ (igual a do professor)
times = ("Palmeiras","São Paulo","Fluminense","Flamengo","Bahia",
         "Athletico-PR","Coritiba","Atlético-MG","Red Bull Bragantino",
         "Botafogo","Grêmio","Vasco","Internacional","Vitória","Santos",
         "Corinthians","Chapecoense","Remo","Cruzeiro","Mirassol")

print(f'Lista de Times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 5 Primeiros são {times[0:5]}')
print('-=' * 20)
print(f'Os 4 Ultimos são {times[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 20)
print(f'O Fluminense está na {times.index('Fluminense')+1} posição')


