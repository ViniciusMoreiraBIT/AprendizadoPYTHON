'''Faça um programa que mostre a tabuada de vários números, um de cada
vez, para cada valor digitados pelou usúario. O programa será
interrompido qaundo o número solicitado for negativo.'''

#Minha resolução ↓
'''tabuada = 1
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    tabuada = 1
    if n <= 0:
        break
    else:
        print('-' * 30)
        while tabuada <= 10:
            print(f'{n} x {tabuada} = {n * tabuada}')
            tabuada += 1
        print('-' * 30)'''

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA de tabuada encerrado...')
