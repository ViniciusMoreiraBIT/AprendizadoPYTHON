'''o= float(input('Comprimeito do cateto oposto: '))
a= float(input('Comprimeto do cateto adjacente: '))
res= (o**2 + a**2) ** (1/2)
print(f'A hipotenusa vai medir {res:.2f}')''' #forma normal

import math
o= float(input('Comprimeito do cateto oposto: '))
a= float(input('Comprimeto do cateto adjacente: '))
res= math.hypot(o,a) #hypot = hipotenusa
print(f'A hipotenusa vai medir {res:.2f}')




