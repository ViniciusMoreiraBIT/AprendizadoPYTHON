'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primero e o último nome separadamente.

Ex: Ana Maria de Souza
primeiro: Ana
ultimo: Souza'''

nome=str(input('Digite seu nome completo: ')).strip().split()
#nome=nome.split()
print(f'Primeiro Nome: {nome[0]}')
print(f'Ultimo Nome: {nome[-1]}')
print(len(nome))
print(f'Ultimo nome: {nome[len(nome)-1]}')
#print(nome[len(nome)]) < erro porque len de nome da o tanto exato, só que sempre começa em 0, então se der exato da mais que oque realmente tem.. por isso o -1
