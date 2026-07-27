frase='Curso em Video Python'
print(len(frase))
print(frase.count('o')) #.count(x) = Quantas vezes aparece a letra 'x' na frase
print(frase.count('P'))
print(frase.count('o',0,14)) #quantos 'o' tem de 0 a 14
print(frase.find('deo')) #.find = De onde começou o 'deo'
print(frase.find('Android')) #palavra inexintente da -1
print('Curso' in frase) # A palavra 'Curso' esta na frase ? = True