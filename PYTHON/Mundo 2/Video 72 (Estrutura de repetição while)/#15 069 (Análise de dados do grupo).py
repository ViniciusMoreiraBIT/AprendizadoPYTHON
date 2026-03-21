'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer o não continuar.
No final, mostre:
A)quantas pessoas tem mais de 18 anos.
B)quantos homens foram cadastrados.
C)quantas mulheres tem mais de 20 anos.'''

cadastros = 0
maior = 0
homens = mulheres = 0
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
print('\033[32;1m'+'_' * 30 ,'\033[m')