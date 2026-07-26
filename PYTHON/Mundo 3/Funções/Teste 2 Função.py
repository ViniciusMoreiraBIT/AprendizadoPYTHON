def contador(*vini): #" * " receba vários argumentos no parametro vini
    print(f'Você digitou {len(vini)} números:')
    print(vini)
    for i in range(0,len(vini)):
        print(vini[i], end=' ')
    print()
    for i in vini:
        print(i,end=' ')
    print()
    print()


contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)