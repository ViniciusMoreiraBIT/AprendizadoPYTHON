'''Crie um programa que leia uma frase
qualquer e diga se ela é um palindromo,
desconsiderando os espaços
EX: Apos a sopa
A sacada da casa
A torre da derrota
O lobo Ama bolo'''

p = input('Frase: ')
#fraseS= p.lower().replace(' ','')[::-1]
#= p.lower().replace(' ','')
if p.lower().replace(' ','')[::-1] == p.lower().replace(' ',''):
    print('É um Palindromo!')
    print(p)
    print('x')
    print(p[::-1])
else:
    print('Negativo')