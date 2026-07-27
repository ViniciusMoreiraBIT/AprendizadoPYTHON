'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

#Minha resolução ↓
listagem = ('Lápis',1.75,
            'Borracha',2.00,
            'Caderno',15.90,
            'Estojo',25.00,
            'Transferidor',4.20,
            'Compasso',9.99,
            'Mochila',120.32,
            'Canetas',22.30,'Livro',34.90)
'''print('-'*40)
print(f'{'LISTAGEM DE PREÇO': ^40}')
print('-'*40)
for i in listagem:
    if type(i) == str: #Jeito facil mas rigido
        print(f'{i:.<30}R$',end='')
    elif isinstance(i, float): #Jeito alternativo com verificação de herança
        print(f'{i: >8.2f}')
print('-'*40)'''

print('-'*40)
print(f'{'LISTAGEM DE PREÇO': ^40}')
print('-'*40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}',end='')
    else:
        print(f'R${listagem[item]:>8.2f}')
print('-'*40)