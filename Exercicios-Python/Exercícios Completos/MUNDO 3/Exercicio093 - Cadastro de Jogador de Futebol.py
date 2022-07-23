# Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL.
# O programa vai ler o NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou.
# Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA.
# No final, tudo isso será guardado em um DICIONÁRIO,
# incluindo o TOTAL DE GOLS feitos durante o campeonato.
print('=-'*15)
dicio = {'Nome': str(input('Nome do Jogador: ')), 'Gols': [], 'Total': 0}
tot = int(input(f'Quantas partidas {dicio["Nome"]} jogou? '))
for p in range(0, tot):
    dicio['Gols'].append(int(input(f'   Quantos gols na partida {p}? ')))
dicio['Total'] = sum(dicio['Gols'])
print('-' * 20)
print(dicio)
print('-' * 20)
for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}')
print('-' * 20)
print(f'O jogador {dicio["Nome"]} jogou {tot} partidas.')
for c in range(0, tot):
    print(f'    => Na partida {c}, fez {dicio["Gols"][c]} gols.')
print(f'Foi um total de {dicio["Total"]} gols.')
print('=-'*15)
