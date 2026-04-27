'''Desenvolva um programa que leia o comprimento de três restas e diga au usuário se elas podem ou não formar um triângulo'''
r1=float(input('Reta 1: '))
r2=float(input('Reta 2: '))
r3=float(input('Reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Triangulo')
else:
    print('ERRO')


'''MINHA SOLUÇÃO:

if r1 + r2 > r3:
    if r1 + r3 > r2:
        if r2 + r3 > r1:
            print('Triangulo! ')
        else:
            print('erro')
    else:
        print('erro')
else:
    print('erro')'''


