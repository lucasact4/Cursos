# Faça um programa que leia NOME E PESO de VÁRIAS PESSOAS, guardando tudo em uma LISTA.
# No final, mostre:
# A) QUANTAS pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais PESADAS.
# C) Uma listagem com as pessoas mais LEVES.
print('=-'*15)
pessoas = []
pessoa = []
mai = men = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = pessoa[1]
    else:
        if pessoa[1] > mai:
            mai = pessoa[1]
        elif pessoa[1] < men:
            men = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    while True:
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()
        if sn in 'SN':
            break
    if sn == 'N':
        break
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {mai}Kg. Peso(s) de: ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {men}Kg. Peso(s) de: ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
print()
print('=-'*15)
