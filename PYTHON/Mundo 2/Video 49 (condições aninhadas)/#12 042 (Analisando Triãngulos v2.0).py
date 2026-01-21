'''Refaça o DESAFIO 035 dos triãngulos, acrescentando o recurso de mostrar que tipo de triãngulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes'''

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Equilátero! Todos lados iguais')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Escaleno! Todos os lados diferentes')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Isósceles! Dois lados iguais')
else:
    print('NÃO TRIANGULO')
