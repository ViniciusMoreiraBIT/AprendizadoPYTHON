def contador(i,f,p):
    """
    → Faz contagem e mostra na tela.
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    """
    cont = i
    while cont <= f:
        print(f'{cont} ',end='')
        cont += p
    print('FIM')

contador(1,20,2)

help(contador)