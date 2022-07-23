# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
print('=-'*15)
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
#BONUS +
san = cidade.split()
san2 = san[0]
san3 = san2.upper()
print('A cidade {} começa com SANTO ? {}'.format(cidade, 'SANTO' in san3))
print('=-'*15)
