cor='\033[7;30;41m'
reset='\033[m'
cores={'clean':'\033[m',
       'red':'\033[31m',
       'yellow':'\033[33m'}
print('Cor',cores['red'],'Vermelha',cores['clean'], 'e Cor',cores['yellow'],'Amarela',cores['clean']+'!')
print('\033[1;30;41mTESTE\033[m')
print(cor+'TESTE'+reset)
