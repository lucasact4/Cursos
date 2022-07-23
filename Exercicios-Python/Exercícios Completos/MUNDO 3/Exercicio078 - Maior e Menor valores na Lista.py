# Faça um programa que leia 5 VALORES NÚMERICOS e guarde-os em uma LISTA.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
print('=-'*15)
lista = []
mai = 0
men = 0
for x in range (0, 5):
    lista.append(int(input(f'Digite um valor númerico para a posição {x}: ')))
    if x == 0:
        mai = men = lista[x]
    else:
        if lista[x] > mai:
            mai = lista[x]
        elif lista[x] < men:
            men = lista[x]
print(f'Você digitou os valores:', end=' ')
for p in lista:
    print(p, end=': ')
print(f'\nMaior valor digitado: {mai} nas posições ', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nMenor valor digitado: {men} nas posições ', end='')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end='')
print()
print('=-'*15)
