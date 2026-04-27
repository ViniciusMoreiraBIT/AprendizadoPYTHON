#004 ex.015 (Aluguel de carro)
d=int(input('Dias Alugados: '))
km=int(input('KM rodados: '))
dia = 60 * d
km1 = km * 0.15
total= dia + km1
print(f'Total a pagar {total:.2f}')