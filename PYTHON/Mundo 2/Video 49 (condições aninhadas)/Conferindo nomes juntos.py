nome= str(input('Digite seu nome: '))
if nome.upper() == 'VINICIUS':
    print(f'É voce {nome}')
elif nome.upper() in 'MARCOS CARLOS VAGNER JORGE':
    print(f'Nome legal {nome}')
else:
    print('Nome normal o teu puff')