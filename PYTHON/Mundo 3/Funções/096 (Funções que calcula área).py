'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura
e comprimento) e mostre a área do terreno.'''

# Minha resolução ↓
'''def area(a,b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m².')


area(float(input('LARGURA (m): ')),float(input('COMPRIMENTO (m):')))'''

def area(larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} = {a}m²')


print(' Controle de terrenos')
print('-'* 20)
l = float(input('Largura (m):'))
c = float(input('Comprimento (m):'))
area(l,c)