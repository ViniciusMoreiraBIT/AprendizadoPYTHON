'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: JUNIOR
-Até 20 anos: SÊNIOR
-Acima: MASTER'''
import datetime
ano = int(input('Anos de Nascimento: '))
idade = datetime.date.today().year - ano
if idade <= 9:
    print(f'Idade| {idade}')
    print('MIRIM')
elif idade <= 14:
    print(f'Idade| {idade}')
    print('INFANTIL')
elif idade <= 19:
    print(f'Idade| {idade}')
    print('JUNIOR')
elif idade == 20:
    print(f'Idade| {idade}')
    print('SÊNIOR')
elif 20 < idade :
    print(f'Idade| {idade}')
    print('MASTER')