'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário
ou então o empréstimo será negado'''
valor=float(input('Valor do imóvel: R$ '))
salario=float(input('Salário do comprador: R$ '))
ano=int(input('Pagar por quantos anos: '))
valor_prestacao= valor / ano
valor1= salario * ( 30 / 100)
print(valor_prestacao)
print (valor1)
if valor_prestacao > salario * ( 30 / 100):
    print('Empréstimo negado')
elif valor_prestacao


