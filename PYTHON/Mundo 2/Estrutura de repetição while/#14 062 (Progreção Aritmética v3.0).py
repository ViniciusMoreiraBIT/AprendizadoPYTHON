'''Melhore o DESAFIO 061, perguntando para o usúario se ele
quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos'''

#Minha resolução ↓
'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
conttermo = 0
while cont <= 10:
    print(termo,end='')
    print(' → ' if cont < 10 else '', end='')
    termo += razao
    cont += 1
    conttermo += 1
    if cont > 10:
        print('\n')
        per = int(input('Quantos termos você quer mostrar a mais? '))
        if per != 0:
            cont -= per
        else:
            print(f'Progressão finalizada com {conttermo} termos mostrados.')'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end='')
        print(' → ' if cont < total else '', end='')
        termo += razao
        cont += 1
    mais = int(input('\nQauntos termos a mais você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
print('\nFIM')