'''Faça um programa que tenha um função chamada escreva()
que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
Ex:.escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~
'''

#Minha resolução ↓
'''def escreva(msg):
    print('~' * len(msg))
    print(f'{msg}')
    print('~' * len(msg))


escreva('  Vinicius  ')
escreva('  Curso de Python no YouTube  ')
escreva('  CeV  ')'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


escreva('Gustavo Guanabara')
escreva('Oi')
escreva('Curso de Python nop Youtube')