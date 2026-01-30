'''Desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas. No final do
programa, mostre:
-A média de idade do grupo
-Qual é o nome do homem mais velho.
-Quanta mulheres têm menos de 20 anos.'''
geral= []
for i in range(0,2):
    n = input('Nome: ')
    ida = int(input('Idade: '))
    s = input('Sexo: ')
    geral.append({'Nome':n,'Idade':ida,'Sexo': s})



print(geral)
print(geral[0])
print(geral[1]['Nome'])