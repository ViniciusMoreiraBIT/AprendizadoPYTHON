'''Melhore o DESAFIO 061, perguntando para o usúario se ele
quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos'''

while True:
    rr = int(input('Quer ver algum termo ?\n(1)SIM\n(0)NÃO\n'))
    if rr == 1:
        termo = int(input('Primeiro termo: '))
        PA = int(input('Razão da PA: '))
        loop = 1
        while loop <= 10:
            res = termo + (loop - 1) * PA
            loop += 1
            print(f'{loop - 1} Termo (a{loop - 1}) = {res}')
    elif rr == 0:
        exit()
    else:
        print('Apenas 1 e 0!')
        continue



