def parOuImpar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

r1 = parOuImpar(4)
r2 = parOuImpar(3)
r3 = int(input('Número: '))
print('É par?..')
print(f'R1 deu {r1}')
print(f'R2 deu {r2}')
print(f'Seu número deu {parOuImpar(r3)}')
if parOuImpar(r3):
    print('É PAR')
else:
    print('É IMPAR')