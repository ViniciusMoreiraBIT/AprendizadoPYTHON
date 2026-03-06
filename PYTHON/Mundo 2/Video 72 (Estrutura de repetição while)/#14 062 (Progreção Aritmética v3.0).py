'''Melhore o DESAFIO 061, perguntando para o usúario se ele
quer mostrar mais alguns termos. O programa encerra
quando ele disser que quer mostrar 0 termos'''

while True:
    rr = input('Quer ver algum termo ?\n(1)SIM\n(0)NÃO\n')
    if not rr.isdigit() or int(rr) not in (1,0):
        continue
    else:
        rr = int(rr)
        if rr == 1:
            termo = int(input('Primeiro termo: '))
            PA = int(input('Razão da PA: '))
            loop = 1
            res = termo
            while loop <= 10:
                print(res, end='')
                print(' → ' if loop < 10 else '\n', end='')
                res += PA
                loop += 1

        elif rr == 0:
            break




