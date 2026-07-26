'''Crie um progama que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) A média de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da média'''

# Minha resolução ↓
'''pessoas = []
dados = {}
idade = 0
while True:
    dados['Nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper()
    while dados['sexo'] not in 'MF':
        print('ERRO! Apenas M ou F.')
        dados['sexo'] = str(input('Sexo: [M/F] ')).upper()
    dados['idade'] = float(input('Idade: '))
    idade += dados['idade']
    pessoas.append(dados.copy())
    per = str(input('Quer continuar? [S/N] ')).upper()
    while per not in 'NS':
        per = str(input('Quer continuar? [S/N] ')).upper()
    if per == 'N':
        break

media = idade / len(pessoas)

print('=-' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media:.2f} anos.')
print('- As mulheres cadastradas foram:', end='')
for i in range(0, len(pessoas)):
    if pessoas[i]['sexo'] == 'F':
        print(f' {pessoas[i]["Nome"]}', end='')
print('\n- A lista de pessoas acima da média:')
for i in range(0, len(pessoas)):
    if pessoas[i]['idade'] > media:
        print()
        print(f'Nome = {pessoas[i]['Nome']}; Sexo = {pessoas[i]['sexo']}; Idade = {pessoas[i]['idade']:.0f}')

print('<< ENCERRADO >>')'''

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Apenas S ou N.')
    if resp == 'N':
        break

print('=-' * 30)
print(f'Ao todo temos {len(galera)} pessoas registradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end='')
print()
print('Lista de pessoas acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
print('<< ENCERRADO >>')

