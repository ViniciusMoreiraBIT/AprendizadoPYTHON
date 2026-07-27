import math #importando tudo do math
from math import sqrt, ceil #importando só os sqrt e ceil
num = int(input('Digite um numero '))
raiz = math.sqrt(num)#metodo importando tudo
raiz = sqrt(num)#metodo importando especifico
arre=ceil(num) #arredondamento sem sentido
print(f'Raiz sem arredondar: {raiz:.2f}')
print(f'Raiz arredondada pra cima: {math.ceil(raiz):.2f}')
print(arre)

#sqrt = raiz quadrada
#ceil = arredondar pra cima
