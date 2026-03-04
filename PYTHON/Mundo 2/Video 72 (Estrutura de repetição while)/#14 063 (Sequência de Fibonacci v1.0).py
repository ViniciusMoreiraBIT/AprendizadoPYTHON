'''Escreva um programa que leia o um número n inteiro
e mostre na tela os n primeiros elementos de uma Sequência
de Fibonacci.
Ex:.
0 → 1 → 1 → 2 → 3 → 5 → 8'''

n = int(input('Digite um número: '))
a = 0
b = 1
cont = 0
while cont < n:
    print(a)
    prox = a + b
    a = b
    b = prox
    cont += 1




