'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite'''
vermelho='\033[31m'
print('KM max 80')
km=int(input('Velocidade do carro: '))
if km > 80:
    print(vermelho,'MULTADO'.center(20, '-'),'\033[m')
    valor = km - 80
    valor_final= valor * 7
    print('Valor final da Multa' ,vermelho,f'R${valor_final},\033[m')
else:
    print('Parabéns, sem multas')

print('Dirija com segurança!')