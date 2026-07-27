from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    rep = menu(['Listar pessoas cadastradas','Cadastrar nova Pessoa','Encerrar programa'])
    if rep == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
        sleep(1)
    elif rep == 2:
        #Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1)
    elif rep == 3:
        #Opção de sair do programa
        cabeçalho('Saindo do Sistema.... Até logo!')
        sleep(1)
        break
    else:
        print('Opção inválida!')

