'''Faça um programa que mostre a tabuada de vários números, um de cada
vez, para cada valor digitados pelou usúario. O programa será
interrompido qaundo o número solicitado for negativo.'''

#Minha resolução ↓
tabuada = 1
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
        print('-' * 30)
