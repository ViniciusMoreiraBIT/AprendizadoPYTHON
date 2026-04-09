'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final
do jogo'''

#Minha resolução ↓
from random import randint
'''print('=-' *12,'\nVAMOS JOGAR PAR OU IMPAR')
vitoria = 0
while True:
    print('=-' *12)
    n = int(input('Digite um valor: '))
    pc = randint (0,10)
    poi = str(input('Par ou Ímpar? [P/I]: ')).upper()
    soma = n + pc
    if poi == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {n} e o computador {pc}. Total de {soma} DEU PAR')
            print('\033[1;32mVocê VENCEU!\033[m\nVamos jogar novamente...')
            vitoria += 1
            continue
    else:
        print(f'Você jogou {n} e o computador {pc}. Total de {soma} DEU IMPAR')
        break
    if poi == 'I':
        if soma % 2 == 1:
            print(f'Você jogou {n} e o computador {pc}. Total de {soma} DEU IMPAR')
            print('\033[1;32mVocê VENCEU!\033[m\nVamos jogar novamente...')
            vitoria += 1
            continue
    else:
        print(f'Você jogou {n} e o computador {pc}. Total de {soma} DEU PAR')
        break
print('\033[1;31mVocê PERDEU!\033[m')
print('=-'*12)
vitoria >= 1 and print(f'GAME OVER! Você venceu {vitoria} vezes.')
vitoria == 0 and print('Você não venceu nenhuma vez')'''

v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]  ')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('Deu PAR'if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes!')

