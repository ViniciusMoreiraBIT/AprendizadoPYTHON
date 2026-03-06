'''Refaça o DESAFIO 051, lendo o primeiro
termo e a razão de uma PA, mostrando 10
primeiros termos da progressão usando a estrutura while'''

#Minha resolução ↓
'''termo = int(input('Primeiro termo: '))
PA = int(input('PA: '))
loop = 1
while loop <= 10:
    razao = termo + (loop -1) * PA
    loop += 1
    print(f'{loop - 1} termo (a{loop - 1}) = {razao}')'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
while cont <= 10:
    print(f'{termo}', end='')
    print(' → ' if cont < 10 else '', end='')
    termo += razao
    cont += 1
print('\nFIM')
