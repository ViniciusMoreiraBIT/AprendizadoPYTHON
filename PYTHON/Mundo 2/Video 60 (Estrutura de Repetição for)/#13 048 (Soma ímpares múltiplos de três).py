'''Faça um programa que calcule a soma e
entre todos os números ímpares que
são múltiplos de três e
que se encontram no intervalo de 1 até 500.'''
soma=0
loop=0
for i in range(0, 500 + 1, 3):
    if i % 2 == 1:
        soma += i
        loop += 1
print(f'A soma de todos os {loop} valores solicitados é {soma}')


