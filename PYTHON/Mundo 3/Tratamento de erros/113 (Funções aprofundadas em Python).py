'''Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora
a possibilidade da digitação de um número de tipo inválido
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

cor = '\033[31m'
x = '\033[m'

#Minha resolução ↓
# def leiaInt(msg):
#     while True:
#         try:
#             n = int(input(msg))
#         except KeyboardInterrupt:
#             print(f'\n{cor}O usuário preferiu não digitar esse número.{x}')
#             return 0
#         except:
#             print(f'{cor}ERRO! digite um número inteiro válido.{x}')
#         else:
#             return n
#
#
# def leiaFloat(msg):
#     while True:
#         try:
#             n = float(input(msg))
#         except KeyboardInterrupt:
#             print(f'{cor}O usuário preferiu não digitar esse número.{x}')
#             return 0
#         except:
#             print(f'{cor}ERRO! digite um número real válido.{x}')
#         else:
#             return n
#
#
# n1 = leiaInt('Digite um inteiro: ')
# n2 = leiaFloat('Digite um Real:')
# print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')

from ex113 import leiaInt, leiaFloat

n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')

print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
