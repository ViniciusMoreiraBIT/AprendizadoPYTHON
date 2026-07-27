'''Faça um programa que leia nome e média
de um aluno, guardando também a situação
em um dicionário. No final, mostre o
conteúdo da estrutura na tela.'''


# Minha resolução ↓
'''dados = {}
aluno = []

for i in range(0,2):
    dados['Nome'] = str(input('Nome: '))
    dados['Média'] = float(input(f'Média de {dados['Nome']}: '))

    if dados['Média'] < 7:
        dados['Situacao'] = 'Reprovado'
    else:
        dados['Situacao'] = 'Aprovado'

    aluno.append(dados.copy())

for item in aluno:
    for chave, valor in item.items():
        print(f'{chave} é igual a {valor}')
    print('-'* 30)

# Ex:. 2 
for i in range(0,2):
    print(f'Nome é igual a {aluno[i]['Nome']}')
    print(f'Média é igual a {aluno[i]['Média']}')
    print(f'Situação é igual a {aluno[i]['Situacao']}')
    print()'''

aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']} '))

if aluno['media'] > 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('=-' * 30)
for c, v in aluno.items():
    print(f'   -{c} é igual a {v}')