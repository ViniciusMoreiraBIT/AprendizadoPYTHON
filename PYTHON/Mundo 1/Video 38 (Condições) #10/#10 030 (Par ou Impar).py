'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR'''
n=int(input('Digite um número: '))
if n % 2 == 0:
    print(f'{n} é','\033[1;34m'+'PAR')
else:
    print(f'{n} é','\033[1;33m'+'IMPAR')