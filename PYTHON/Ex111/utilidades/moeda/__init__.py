def aumentar(preço = 0, taxa = 0,format = False):
    res =  preço + (preço * taxa / 100)
    return res if format == False else moeda(res)


def diminuir(preço = 0, taxa = 0,format = False):
    res = preço - (preço * taxa / 100)
    return res if format == False else moeda(res)


def dobro(preço = 0,format = False):
    res = preço * 2
    return res if not format else moeda(res)


def metade(preço = 0,format = False):
    res = preço / 2
    return res if format is False else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')

def resumo(n,a = 0,d = 0):
    print('=-' * 20)
    print(f'{'RESUMO DE VALORES': ^40}')
    print('=-' * 20)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'A metade do preço: \t{metade(n,True)}')
    print(f'{'O dobro do preço:': <19} {dobro(n,True)}')
    print(f'{f'Aumentando {a}%:': <19} {aumentar(n, a, True)}')
    print(f'{f'Diminuindo {d}%:': <19} {diminuir(n, d, True)}')
    print('=-' * 20)


