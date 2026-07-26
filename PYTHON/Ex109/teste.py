from Ex109 import moeda

p = float(input('Digite um valor: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, o valor fica {moeda.aumentar(p,10,True)}')
print(f'Diminuindo 30%, o valor fica {moeda.diminuir(p,30,True)}')


