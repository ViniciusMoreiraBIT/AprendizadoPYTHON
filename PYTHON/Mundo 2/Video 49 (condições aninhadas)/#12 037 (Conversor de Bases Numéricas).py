'''Escreva um programa que leia um número inteiro qualquer e peça para o usúario escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal'''

num=int(input('Digite um número inteiro: '))
print('''Escolha uma base de conversão: 
(1) Binário
(2) Octal
(3) Hexadecimal''')
bi = bin(num)
oc = oct(num)[2:]
res= int(input(' '))
if res == 1:
    print(f'{num} em Binário: {bi[2:]}')
elif res == 2:
    print(f'{num} em Octal: {oc}')
elif res == 3:
    print(f'{num} em Hexadecimal: {hex(num)[2:]}')
else:
    print('ERRO')
