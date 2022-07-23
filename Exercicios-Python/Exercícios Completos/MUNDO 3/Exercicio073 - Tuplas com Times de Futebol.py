# Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da Tabela do
# CAMPEONATO BRASILEIRO DE FUTEBOL, na ordem de colocação. Depois mostre:
# A) Apenas os 5 PRIMEIROS colocados.
# B) Os ÚLTIMOS 4 colocados da tabela.
# C) Uma lista com os times em ORDEM ALFABÉTICA.
# D) Em que POSIÇÃO na tabela está o time da Chapecoense.
print('=-'*15)
tupla = ('Palmeiras', 'Atlético-MG', 'Corinthians', 'Coritiba',
         'São Paulo', 'Athlético-PR', 'Botafogo', 'Flamengo',
         'Santos', 'América-MG', 'Fluminense', 'Internacional',
         'Avaí', 'Bragantino', 'Goiás', 'Cuiabá', 'Atlético-GO',
         'Juventude', 'Ceará SC', 'Fortaleza')
print(f'A) Os 5 primeiros colocados são:\n1ª {tupla[0]}\n2ª {tupla[1]}\n3ª {tupla[2]}\n4ª {tupla[3]}\n5ª {tupla[4]}')
print(f'B) Os 5 últimos colocados são:\n17ª {tupla[16]}\n18ª {tupla[17]}\n19ª {tupla[18]}\n20ª {tupla[19]}')
print(f'C) Ondem Alfabética:\n{sorted(tupla)}')
print('D) Posição do time do Flamengo: {}ª Posição'.format(tupla.index('Flamengo')+1))
# BONUS +
print('-'*10)
print(f'1) Lista de times do Brasileirão: {tupla}')
print(f'2) Os 5 primeiros são: {tupla[0:5]}')
print(f'3) Os 4 últimos são: {tupla[-4:]}')
print(f'4) Times em ordem alfabético: {sorted(tupla)}')
print(f'5) O Flamengo está na: {tupla.index("Flamengo")+1}º Posição')
print('=-'*15)
