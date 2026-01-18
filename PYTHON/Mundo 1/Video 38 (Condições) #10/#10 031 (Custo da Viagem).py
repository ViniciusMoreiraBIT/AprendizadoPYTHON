'''Escreva um programa que pergunte a distância de uma viagem em Km.
Calcule o Preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM e R$0,45 para viagens mais longas'''
km=float(input('\033[32m'+'Distancia em KM: '+'\033[m'))
'''if km <= 200:
    valor = km * 0.50
    print(f'Valor da Viagem: R${valor:.2f}')
else:
    valor = km * 0.45
    print(f'Valor da Viagem +: R${valor:.2f}')'''

valor= km * 0.50 if km <= 200 else km * 0.45
print(f'Valor da Viagem: R${valor}')
print('OBRIGADO'.center(20, '-'))