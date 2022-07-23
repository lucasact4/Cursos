# Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma LISTA.
# Depois disso, mostre:
# A) QUANTOS números foram digitados.
# B) A lista de valores, ordenada de forma DECRESCENTE.
# C) Se o valor 5 foi digitado e está ou não na LISTA.
print('=-'*15)
lista = []
x = 1
while True:
    num = int(input(f'Digite o {x}ª valor númerico: '))
    lista.append(num)
    print('Valor adicionado com sucesso...')
    while True:
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if cont == 'S':
            break
        if cont == 'N':
            break
    if cont == 'N':
        break
    x += 1
lista.sort(reverse=True)
print(f'A) Você digitou {len(lista)} elementos.')
print(f'B) Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('C) O valor 5 faz parte da lista!')
else:
    print('C) O valor 5 não faz parte da lista!')
print('=-'*15)
