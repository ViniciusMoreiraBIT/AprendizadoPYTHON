'''Faça um programa que leia um número
inteiro e diga se ele é ou não um número primo'''

print('''Verificando se o Número é Primo!
''')
num = int(input('Digite um Número: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[m', end='')
    print(f'{i}', end=' ')
print('\n\033[m'+f'O número {num} foi divisivel {tot} vezes')
if tot == 2 or num == 2:
    print('É um número PRIMO!')
else:
    print('Não é Primo')


