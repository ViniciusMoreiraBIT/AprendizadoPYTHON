import moeda #se estiver no mesmo diretório pode importar sem usar from...

p = float(input('Digite um valor: R$ '))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, o valor fica R${moeda.aumentar(p,10)}')
print(f'Diminuindo 30%, o valor fica R${moeda.diminuir(p,30)}')


