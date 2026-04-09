'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer o não continuar.
No final, mostre:
A)quantas pessoas tem mais de 18 anos.
B)quantos homens foram cadastrados.
C)quantas mulheres tem mais de 20 anos.'''

#Minha resolução ↓
'''
homens = mulheres = cadastros = maior = 0
while True:
    idade = int(input('Digite sua idade: '))
    if idade > 18:
        maior += 1
    sexo = input('Digite seu sexo (M/F): ').strip().upper()
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade > 20:
        mulheres += 1
    per = input('Quer continuar? (S/N): ').strip().upper()
    cadastros += 1
    if per not in 'SN':
        print('ERRO, tente novamente: ')
        per = input('Quer continuar? (S/N): ').strip().upper()
    if per == 'S':
        continue
    elif per == 'N':
        break

print('\033[32;1m'+'_' * 30 ,'\033[m')
print(f'{maior} pessoa tem mais de 18 anos.' if maior == 1 else f'{maior} pessoas tem mais de 18 anos.')
print(f'{homens} homem foi cadastrado.' if homens == 1 else f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulher é maior de 20 anos.' if mulheres == 1 else f'{mulheres} mulheres são maior de 20 anos.')
print(f'{cadastros} cadastros foram realizados.')
print('\033[32;1m'+'_' * 30 ,'\033[m')'''

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if idade > 20 and sexo == 'F':
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'Temos {totM20} mulheres com mais de 20 anos.')