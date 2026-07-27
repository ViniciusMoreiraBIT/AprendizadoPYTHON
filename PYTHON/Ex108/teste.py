from Ex108 import moeda

p = float(input('Digite um valor: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, o valor fica {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuindo 30%, o valor fica {moeda.moeda(moeda.diminuir(p,30))}')


