'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário
ou então o empréstimo será negado'''

print('Para a realização do empréstimo as parcelas do imóvel não pode ultrapassar 30% do seu salário atual!')
valor=float(input('Valor do imóvel: R$ '))
salario=float(input('Salário do comprador: R$ '))
ano=int(input('Pagar por quantos anos: '))
valor_prestacao= valor / (ano * 12) #Valo / Meses
if valor_prestacao > salario * ( 30 / 100):
    print('Empréstimo negado')
    print(f'''30% do salario: R${salario * ( 30 / 100)}
Valor da parcela R${valor_prestacao:.2f}''')
else:
    print('\033[32m'+'=-'* 22)
    print(f'Sua prestação ficou em {ano} vezes de R${valor_prestacao:.2f}')
    print(('=-'* 22)+'\033[m')
    print(f'''30% do salario: R${salario * (30 / 100)}
Valor da parcela R${valor_prestacao:.2f}''')



