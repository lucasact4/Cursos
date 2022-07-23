# Crie um programa onde 4 JOGADORES joguem um DADO e tenham resultados ALEATÓRIOS.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
print('=-'*15)
from random import randint
from time import sleep
from operator import itemgetter
dicio = {'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}
ranking = list()
cont = 1
print('Valores sorteados:')
for k, v in dicio.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print('-' * 15)
ranking = sorted(dicio.items(), key=itemgetter(1), reverse=True)
print(f'{"=== RANKING DOS JOGADORES ===":^40}')
for k, v in ranking:
    print(f'  {cont}º Lugar - {k} com {v} no dado.')
    cont += 1
print('=-'*15)
