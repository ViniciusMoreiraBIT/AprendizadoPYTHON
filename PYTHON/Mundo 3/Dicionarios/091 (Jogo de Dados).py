'''Crie um programa onde 4 jogadores joguem dados
e tenham resultados aleatórios. Guarde esses
resultados em um dicionário. No final, coloque
esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep

# Minha resolução ↓
'''jogo = {}
resultados = []
pontos = []

input('')
print('\rValores Sorteados:')

for i in range(1,5):#------------------------------------→ Adiciona jogador1,2,3,4 e seus valores aleatórios de 1 a 6 no (jogo)
    jogo[f'jogador{i}'] = randint(1,6)

resultados.append(jogo.copy())#--------------------------→ Copia o em uma lista o dicionário "jogo"

for jogador in resultados:#------------------------------→ Percorre cada item da lista
    for chave , valor in jogador.items():#---------------→ Percorre cada chave e valor da lista
        print(f'  O {chave} tirou {valor}')#-------------→ Mostra a chave e o valor daquela volta
        sleep(1)

for i in range(1,5):
    pontos.append(resultados[0][f'jogador{i}'])#---------→ Adiciona os resultados na lista pontos

pontos = list(set(pontos))#------------------------------→ Remove números iguais
pontos.sort(reverse=True)#-------------------------------→ Ordena de forma decrescente

print('Ranking de jogadores: ')

cont = 0
for v in pontos: #---------------------------------------→ Valor de cada jogador
    for lop in range(1,5): #-----------------------------→ Loop de verificação
        if v == resultados[0][f'jogador{lop}']: #--------→ Se o valor for igual ao jogador1, 2, 3, 4 então:
            cont += 1
            sleep(1)
            print(f'  {cont}º lugar: jogador{lop} = {resultados[0][f"jogador{lop}"]}') #-→ Print da posição e do jogador que fez mais pontos..'''

from operator import itemgetter

jogo = { 'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}

ranking = list()

print('Valores Sorteados:')

for c, v in jogo.items():
    print(f'  {c} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #-→ A lista ranking vira a cópia do jogo
                                                                #-→ sorted jogo.items() deixa em ordem / key=itemgetter(1) a ordem vai ser apenas o indice 1 de cada jogador

print('Ranking de Jogadores: ')
for i, v in enumerate(ranking):
    print(f'  -{i + 1}º Lugar {v[0]} = {v[1]}')
    sleep(1)
# print('Ranking de Jogadores: ')
# cont = 0
# for i in ranking:
#     cont += 1
#     print(f'  -{cont}º Lugar: {i[0]} = {i[1]}')