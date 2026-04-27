'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também o indice do menor e o maior valor que estão na tupla'''

#Minha resolução ↓
from random import randint
'''numeros = (randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10),randint(0, 10))
print('Os valores sorteados foram:' ,*numeros )
print(f'O maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')'''

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores digitados foram: ',end='')
for nuns in n:
    print(f'{nuns} ', end='')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')