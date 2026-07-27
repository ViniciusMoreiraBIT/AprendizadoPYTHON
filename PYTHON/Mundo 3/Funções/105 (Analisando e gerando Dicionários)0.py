'''Faça um programa que tenha uma função notas() que pode
receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
-Quantidade de notas
-A maior nota
-A menor nota
-A média da turma
-A situação (opcional)

Adicione também as docstrings da função.'''

# def notas(*n, sit=False):
#     '''
#     -→ Função para analisar notas e situações de vários alunos.
#     :param n: Uma ou mais notas dos alunos (aceita várias)
#     :param sit: Valor opcional, indicando se deve ou não adicionar a situação
#     :return: Dicionário com várias informações sobre a situação da turma.
#     '''
#     alunos = {}
#     alunos['total'] = len(n)
#     alunos['maior'] = max(n)
#     alunos['menor'] = min(n)
#     alunos['média'] = sum(n) / len(n)
#     if sit:
#         if alunos['média'] >= 7:
#             alunos['situação'] = 'BOA'
#         elif 6 <= alunos['média'] < 7:
#             alunos['situação'] = 'RAZOÁVEL'
#         else:
#             alunos['situação'] = 'RUIM'
#     return alunos
#
# resp = notas(5.5,9.5,10,6.5, sit= True)
# print(resp)
# resp = notas(3.5,10,6.5, sit=True)
# print(resp)
# resp = notas(3.5,2,6.5,2,7,4, sit= True)
# print(resp)
# help(notas)


def notas(*n,sit=False):
    '''
    → Função para analiar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias infortmações sobre a situação da turma.
    '''
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


#Programa principal
resp =  notas(5.5,2.5,1.5,sit=True)
print(resp)
help(notas)