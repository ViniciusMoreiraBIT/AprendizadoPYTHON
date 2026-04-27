#1 opção
'''import math
an= float(input('Digite o angulo que você deseja: '))
sen=math.sin(math.radians(an)) #radians = radiano
cos=math.cos(math.radians(an))
tan=math.tan(math.radians(an))
print(f'O angulo de {an} tem o SENO de {sen:.2f}')
print(f'O angulo de {an} tem o COSSENO de {cos:.2f}')
print(f'O angulo de {an} tem o TANGENTE de {tan:.2f}')'''

from math import sin, radians, cos ,tan
an = float(input('Digite o angulo que você deseja: '))
sen=sin(radians(an))
cos=cos(radians(an))
tan=tan(radians(an))
print(f'O angulo de {an} tem o SENO de {sen:.2f}')
print(f'O angulo de {an} tem o COSSENO de {cos:.2f}')
print(f'O angulo de {an} tem o TANGENTE de {tan:.2f}')
