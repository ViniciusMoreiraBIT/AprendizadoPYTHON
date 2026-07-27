'''Faça um programa que leia três números e mostre qual é o maior e o menor'''
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
n3 = int(input('Terceiro Número '))
'''max= max(n1,n2,n3)
min= min(n1,n2,n3)
print('O maior é'+'\033[32m',f'{max}'+'\033[m'+' e o Menor é'+'\033[31m'+f' {min}')'''
#Verificando o menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#verificando quem é o maior:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior é {maior} e o menor é {menor}')

