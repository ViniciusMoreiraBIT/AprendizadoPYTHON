lanche = ('Hamburguer','Suco','Pizza','Pudim')

for comida in lanche:
  print(comida)
print('\n')

for i in range (0,len(lanche)):
  print(f'{i} {lanche[i]}')
print('\n')

for p, i in enumerate(lanche):
  print(p, i)

print('Comi pra caramba!')