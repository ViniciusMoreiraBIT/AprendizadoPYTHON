#Crie um programa que leia o nome da cidade e diga se ela começa ou não com o nome "SANTO"

cidade=str(input('Nome da cidade: ')).strip() #strip ja elimina os espaços do começo e fim
cdd=cidade.split()
print('SANTO' in cdd[0].upper())
print(cidade.upper().replace(' ','')[:5] == 'SANTO')
print(cidade[:5].upper().replace(' ','') == 'SANTO')
print(cidade[:5].upper() == 'SANTO')