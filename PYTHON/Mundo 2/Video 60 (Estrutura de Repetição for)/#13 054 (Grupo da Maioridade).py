'''Crie um programa que leia o ano de
nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores'''
p = []
idadee = []
for i in range(1, 7):
    ano = int(input('Ano de Nascimento: '))
    p.append(ano)

for i in range(0,6):
    idade = 2026 - p[i]
    if idade < 18:
        print(f'{idade} Anos, ainda não atingiu a maioridade!')
        idadee.append(idade)
    else:
        print(f'{idade} Anos, Maior de idade!')
        idadee.append(idade)

print(idadee)





