'''Melhore o jogo do DESAFIO 028 onde o computador
vai "pensar" em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer'''

from random import randint
pc = randint(0, 10)
palpites = 1
print('O pC pensou em um número de 0 a 10!')
while True:
    res = int(input('Qual Número o PC pensou: '))
    if res != pc:
        print('Tente novamente!\n')
        palpites += 1
        continue
    else:
        break
print(f'\nPARABÉNS Você acertou!!\nVocê tentou {palpites} vezes para acertar!')