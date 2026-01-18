'''Crie um programa que leia o nome completo da pessoa e mostre:

o nome com todas as letras Maiusculas
o nome com todas as letras minusculas
Quantas letras ao todo (sem considerar os espaços)
Quantas letras tem no primeiro nome'''

nome=str(input('Digite seu Nome:')).strip()
nome0=nome.replace(' ','')
print(f'Seu nome Maiúsculo: {nome.upper()}')
print(f'Seu nome Minusculos: {nome.lower()}')
print(f'Quantas letras tem seu nome: {len(nome) - nome.count(' ')}') # count = - o tanto de espaços que tem
#print(f'Quantas letras tem seu nome: {len(nome0)}')
#print(f'Quantas letras tem seu primeiro nome: {len(nome.split()[0])}')
print(f'Quantas letras tem seu primeiro nome: {nome.find(' ')}')#find= onde começa o primeiro espaço

