'''Crie um programa que leia dois valores e
mostre um menu na tela:
1 soma
2 multiplicar
3 qual o maior
4 novos números
5 sair do programa

Seu programa deverá realizar a operação solicitada em cada caso'''

#Minha resolução ↓
'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
while True:
    print('=-'* 10,'\n',' '*6,'MENU\n'+'=-'*10)
    print('1 SOMAR\n2 MULTIPLICAR\n3 MAIOR VALOR\n4 NOVOS NÚMEROS\n5 SAIR DO PROGRAMA')
    res = int(input('Qual deseja? '))
    if res == 4:
        n1 = int(input('\nPrimeiro número: '))
        n2 = int(input('Segundo número: '))
        print('Valores alterados.\n')
    elif res == 1:
        print(f'\nA Soma de {n1} + {n2} é {n1 + n2}\n')
    elif res == 2:
        print(f'\nA Multiplicação de {n1} x {n2} é {n1 * n2}')
    elif res == 3:
        print(f'O maior valor ente {n1} e {n2} é {max(n1,n2)}')
    elif res == 5:
        break
    else:
        print('\nOpção invalida..\n')'''

from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opção = 0
while opção != 5:
    print('=-'* 10,'\n',' '*6, 'MENU\n'+'=-'*10)
    print('1 SOMAR\n2 MULTIPLICAR\n3 MAIOR VALOR\n4 NOVOS NÚMEROS\n5 SAIR DO PROGRAMA')
    opção = int(input('Qual deseja ? → '))
    if opção == 1:
        soma = n1 + n2
        for i in [n1,'+',n2,'=',soma]:
            print(i,'',end='')
            sleep(0.5)
        print('')
    elif opção == 2:
        mult = n1 * n2
        print(f'{n1} x {n2} = {mult}')
        sleep(1)
    elif opção == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
            sleep(1)
        else:
            print(f'O maior é {n2}')
            sleep(1)
    elif opção == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
        sleep(1)
        print('Valores atualizados.')
for i in range(0,3):
    print('.',end='')
    sleep(0.4)
print('\nFim do programa!')
