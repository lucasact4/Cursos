# Crie um programa que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS,
# guardando os dados de cada pessoa em um DICIONÁRIO e todos os dicionários em uma LISTA.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo.
# C) Uma lista com todas as MULHERES.
# D) Uma lista com todas as pessoas com IDADE acima da MÉDIA.
print('=-'*15)
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] in 'Ff':
        print(f'[{p["Nome"]}] ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
print('=-'*15)
