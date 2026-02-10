'''Crie um programa que leia dois valores e
mostre um menu na tela:
1 soma
2 multiplicar
3 qual o maior
4 novos números
5 sair do programa

Seu programa deverá realizar a operação solicitada em cada caso'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
while True:
    print('=-'* 10,'\n',' '*6,'MENU\n'+'=-'*10)
    print('1 SOMA\n2 MULTIPLICAR\n3 MAIOR VALOR\n4 NOVOS NÚMEROS\n5 SAIR DO PROGRAMA')
    res = int(input('Qual deseja? '))
    if res == 4:
        n1 = int(input('\nPrimeiro número: '))
        n2 = int(input('Segundo número: '))
        print('Valores alterados.\n')
        continue
    elif res == 1:
        print(f'\nA Soma de {n1} + {n2} é {n1 + n2}\n')
    elif res == 2:
        print(f'\nA Multiplicação de {n1} x {n2} é {n1 * n2}')
    elif res == 3:
        print(f'O maior valor ente {n1} e {n2} é {max(n1,n2)}')
    elif res == 5:
        break
