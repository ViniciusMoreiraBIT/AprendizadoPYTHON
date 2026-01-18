'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor de seu aumento
Para salarios superiores a 1250,00, calcule um aumento de 10%
Para inferiores ou iguais, o aumento é de 15%'''
salario=float(input('Salario: '))
if salario > 1250:
    aumento= salario * 0.10
    sa_final = salario + aumento
    print(f'Salario base R${salario}, aumento de R${aumento}. Salario final: R${sa_final:.2f}')
else:
    aumento= salario * ( 15 / 100) #Ou aumento = aumento + (aumento * (15 /100)
    sa_final = salario + aumento
    print(f'Salario base R${salario}, aumento de R${aumento}. Salario final: R${sa_final}')
print(' ')
print('PARABÉNS'.center(20,'-'))