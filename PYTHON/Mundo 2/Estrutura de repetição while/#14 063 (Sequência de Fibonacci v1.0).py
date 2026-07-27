'''Escreva um programa que leia o um número n inteiro
e mostre na tela os n primeiros elementos de uma Sequência
de Fibonacci.
Ex:.
0 → 1 → 1 → 2 → 3 → 5 → 8'''

#Minha resolução
'''n = int(input('Digite um número: '))
a = 0
b = 1
cont = 0
while cont < n:
    cont += 1
    print(a, end='')
    print(' → 'if cont < n else '', end='')
    prox = a + b
    a = b
    b = prox'''

seq ='Sequência de Fibonacci'
print('=' * len(seq))
print(seq)
print('=' * len(seq))
n = int(input('Quantos termos que você quer mostrar ?'))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} → {t2} ', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'→ {t3} ', end ='')
    cont += 1
    t1 = t2
    t2 = t3
print('→ FIM')
print('~' * 30)





