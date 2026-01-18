#004 ex.010 (Real pra dolar / Dolar pra real)
real=int(input('R$ '))
dolar = real / 5.50
print(f'U${dolar:.2f}')

dolar=int(input('U$ '))
real = dolar * 5.50
print(f'R$ {real:.2f}')