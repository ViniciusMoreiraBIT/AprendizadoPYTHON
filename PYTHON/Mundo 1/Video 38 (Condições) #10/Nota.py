n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m= (n1+n2) / 2
print(f'A sua média foi {m:.1f}')
'''if m >= 6.0:
    print('Sua média foi boa')
else:
    print('Sua média foi ruim ')'''
print('Parabens' if m >= 6.0 else 'Estude mais')
