'''Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-os (com idade) em um
dicionário se por acaso o CTPS for diferente de ZERo,
o dicionário receberá também o ano de contratação e o
salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.'''

from datetime import datetime
# Minha resolução ↓
'''pessoa = {}

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = datetime.now().year - int(input('Ano de Nascimento: '))
    pessoa['ctps']  = int(input('Carteira de Trabalho (0 não tem): '))
    if pessoa['ctps'] == 0:
        break
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = int(input('Salário R$: '))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - (datetime.now().year - pessoa['contratação']))
    break

print('=-' *  30)
for c, v in pessoa.items():
    print(f'  - {c} tem o valor {v}')'''

dados = {}

dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('=-' * 30)
for c, v in dados.items():
    print(f'  - {c} tem o valor {v}')