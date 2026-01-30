'''Refaça o DESAFIO 009, mostrando a
tabuada de um número que o usuário
escolher, só que agora utilizando um laço for'''

tab = int(input('Tabuada: '))
print(f'TABUADA DO {tab}')
for i in range (1, 10 + 1):
    print(f'{tab} x {i} = {tab * i}')