num =[2,5,9,1]
num[2] = 3
num.append(7)
#num.sort() #colaca em ordem crescente
#num.reverse() faz com que a lista fica ao contrario
num.sort(reverse=True) #ordem decrescente
num.insert(2, 0) #adiciona elemento na lista no parametro indicado (nesse exemplo é no 2 o valor 0)
num.pop() #remove o ultimo
num.pop(2) #remove o parametro indicado
num.append(2)
if 2 in num:
    num.remove(2) #remove o primeiro 2
else:
    print('Não achei no número 2')
print(*num)
print(f'Essa lista tem {len(num)} elementos')