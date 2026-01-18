'''Faça um programa que leia o número de 0  a 9999 e mostre na tela cada um dos digitos separados
Ex. Digite um numero: 1834

unidade:1
Dezena:3
Centena:8
Milhar:1
'''

num=int(input('Digite um Numero até 9999:'))
u=num // 1 % 10
d=num // 10 % 10
c=num // 100 % 10
m=num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')