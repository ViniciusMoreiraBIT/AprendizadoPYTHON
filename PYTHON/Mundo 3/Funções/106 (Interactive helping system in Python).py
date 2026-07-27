'''Faça um mini sistema que utilize o interactive help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando
o usuário digitar FIM, o programa incerrará.
OBS:. Use cores'''
from time import sleep

#Minha resolução ↓
# cor = {'green': '\033[;42;1m',
#            'red': '\033[;41;1m',
#            'blue': '\033[;44;1m',
#            'white': '\033[7;40m',
#            'clean': '\033[m'}
#
# def bunitin(msg,mm):
#     '''
#     Mensagem com cor de fundo
#     :param msg: A string
#     :param mm: A cor
#     :return: --
#     '''
#     tam = len(msg) + 4
#     c = mm
#     print(cor[f'{c}'], end='')
#     print('~' * tam )
#     print(f'  {msg}  ')
#     print('~' * tam)
#     print(cor['clean'], end='')
#
#
# def h(msg):
#     while True:
#         bunitin('SISTEMA DE AJUDA PyHELP','green')
#         res = input(msg)
#         if res.upper() == 'FIM':
#             bunitin('ATÉ LOGO!','red')
#             sleep(3)
#             break
#         bunitin(f"Acessando o manual do '{res}'",'blue')
#         print(cor['white'])
#         help(res)
#         print(cor['clean'], end='')
#         sleep(3)
#
#
# h('Função ou Bibliotaca >')
c = ('\033[m', #0 apagar
     '\033[0;41;1m', #1 vermelho
     '\033[0;42;1m', #2 verde
     '\033[0;43;1m', #3 amarelo
     '\033[0;44;1m', #4 azul
     '\033[0;45;1m', #5 roxo
     '\033[7;40m'    #6 branco
     )
def ajuda(com,cor=0):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    print(c[cor])
    help(com)
    print(c[0])
    sleep(2)

def titulo(msg,cor = 0):
    tam = len(msg) + 4
    print(c[cor],end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0],end='')
    sleep(0.5)


#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP',2)
    comando = str(input('Função ou Biblioteca>'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando,6)
titulo('Até logo!',1)
