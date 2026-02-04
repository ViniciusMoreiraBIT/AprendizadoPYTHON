'''Desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas. No final do
programa, mostre:
-A média de idade do grupo
-Qual é o nome do homem mais velho.
-Quantas mulheres têm menos de 20 anos.'''
geral= []
pessoa = []
soma_idade=0
for i in range(0,3):
    n = input('Nome: ')
    ida = int(input('Idade: '))
    s = input('Sexo: ')
    geral.append({'Nome':n,'Idade':ida, 'Sexo': s})

for i in range(0, 3):
    soma_idade += geral[i]['Idade']

print(f'Média de idade: {soma_idade / 3:.0f}')

idade = 0
mulher = 0
mulher_cont = 0
for i in range(0, 3):
    if geral[i]['Sexo'].upper() == 'M':
        idade = geral[i]['Idade']
        pessoa.append(idade)

for i in range(0, 3):
    if max(pessoa) == geral[i]['Idade'] and geral[i]['Sexo'].upper() == 'M':
        print(f'Homem mais velho é o {geral[i]['Nome']} com idade de {geral[i]['Idade']} Anos')

for i in range(0, 3):
    if geral[i]['Sexo'].upper() == 'F':
        if geral[i]['Idade'] < 20:
            mulher_cont += 1
if mulher_cont > 1:
    print(f'{mulher_cont} Mulheres com idade a baixo de 20 anos')
elif mulher_cont == 1:
    print(f'{mulher_cont} Mulher com idade a baixo de 20 anos')





