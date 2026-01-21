'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O Primeiro valor é maior
- O Segundo valor é maior
- Não existe valor maior, os dois são iguais'''

n1=int(input('Primeiro número: '))
n2=int(input('Segundo número: '))
if n1 > n2:
    print(f'O Primeiro número é maior! ({n1} {n2})')
elif n2 > n1:
    print(f'O Segundo número é maior! ({n1} {n2})')
else:
    print(f'Não existe valor maior, os dois são iguais ({n1} {n2})')
