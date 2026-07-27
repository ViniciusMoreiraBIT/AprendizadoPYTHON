'''Desenvolva um programa que leia seis
números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor
digitado for impar, desconsidere-o.'''
soma = 0
soma2 = 0
for i in range(1,6+1):
    num = int(input(f'{i} Número: '))
    if num % 2 == 0:
        soma = num + soma
    else:
        soma2 = num + soma2
print(f'Pares: {soma}')
print(f'Impares: {soma2}')