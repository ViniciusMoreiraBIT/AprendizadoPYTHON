'''Desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas. No final do
programa, mostre:
-A média de idade do grupo
-Qual é o nome do homem mais velho.
-Quantas mulheres têm menos de 20 anos.'''
geral= []
pessoa = []
soma_idade=0
mulher_cont = 0
for i in range(0,3):
    n = input('Nome: ')
    ida = int(input('Idade: '))
    s = input('Sexo: ')
    soma_idade += ida
    geral.append({'Nome':n,'Idade':ida, 'Sexo': s})
    if s.upper() == 'F' and ida < 20:
        mulher_cont += 1

print(len(geral))

print(f'Média de idade: {soma_idade / 3:.0f}')
print(f'{mulher_cont} Mulheres menor de 20 anos')

maior = 0
idade = 0
for i in range(0, 3):
    if geral[i]['Sexo'].upper() == 'M':
        pessoa.append(geral[i]['Idade'])
if pessoa:
    maior = max(pessoa)
    for i in range(3):
        if maior == geral[i]['Idade'] and geral[i]['Sexo'].upper() == 'M':
            print(f'Homem mais velho é o {geral[i]['Nome']} com idade de {geral[i]['Idade']} Anos')
else:
    print('Nenhum homem')


'''media = 0
maiorhomem = 0
mulher20 =0
nomehomemv = ''
for i in range(0 , 3):
    print(f'--{i} PESSOA--')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    media += idade
    if i == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomehomemv = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomehomemv = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print(f'A média de idade é {media / 3} Anos')
print(f'O homem mais velho é o {nomehomemv} com {maiorhomem} Anos')
print(f'{mulher20} Mulheres tem menos de 20 anos')'''




