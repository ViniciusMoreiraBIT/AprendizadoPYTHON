'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

valor = float(input('Preço do Produto: '))
print('''Escolha uma forma de pagamento:

-(1) à vista dinheiro/cheque: 10% de desconto
-(2) À vista no cartão: 5% de desconto
-(3) Em até 2x no cartão: preço normal
-(4) 3x ou mais no cartão: 20% de juros''')
pag = int(input('Forma de pagamento: '))
if pag == 1:
    desconto = valor * ( 10 / 100)
    print(f'Valor a ser pago: R${valor - desconto:.2f}')
elif pag == 2:
    desconto = valor * ( 5 / 100)
    print(f'Valor a ser pago: R${valor - desconto:.2f}')
elif pag == 3:
    print(f'2 parcelas de R${valor / 2:.2f}')
    print(f'Valor a ser pago: R${valor:.2f}')
elif pag == 4:
    parcelas = int(input('Quantas parcelas = '))
    juros = valor * ( 20 / 100)
    print(f'{parcelas} parcelas de R${(valor + juros) / parcelas:.2f}')
    print(f'''Valor sem juros: R${valor}
Valor com juros: R${valor + juros:.2f}''')
else:
    print('Opção invalida!')
