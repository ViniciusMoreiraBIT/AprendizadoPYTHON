'''Faça um programa que calcule a soma e
entre todos os números ímpares que
são múltiplos de três e
que se encontram no intervalo de 1 até 500.'''

for i in range(0, 500 + 1, 3):
    if i % 2 == 1:
         print(i)

