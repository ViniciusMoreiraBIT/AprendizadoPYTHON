nun = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in range(len(nun) - 1, -1, -1):
    print(nun[i], end=' ')
print()

for n in reversed(nun):
    print(n, end=' ')
print()

for i in range(1, len(nun) + 1, 1):
    print(nun[-i], end=' ')

print()
for i in nun:
    print(nun[-i],end=' ')
