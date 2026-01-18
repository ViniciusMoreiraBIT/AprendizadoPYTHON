'''Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome'''

nome=str(input('Digite seu Nome: ')).strip()
#nome=nome.upper() ou ↓↓
print('SILVA' in nome.upper())
print(nome[:].upper())