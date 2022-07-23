# Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES,
# incluindo um sistema de visualização de DETALHES DO APROVEITAMENTO de cada jogador.
print('=-'*15)
time = list()
dicio = dict()
partidas = list()

while True:
    dicio.clear()
    dicio['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {dicio["Nome"]} jogou? '))
    partidas.clear()
    for p in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {p+1}? ')))
    dicio['Gols'] = partidas[:]
    dicio['Total'] = sum(dicio['Gols'])
    time.append(dicio.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 40)
print('cod ', end='')
for i in dicio.keys():
    print(f'{i:<16}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
print('=-'*15)
