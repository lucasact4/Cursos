# Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma LISTA.
# Depois disso, crie DUAS LISTAS EXTRAS que vão conter apenas os valores
# PARES e os valores ÍMPARES digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
print('=-'*15)
lista = []
par = []
impar = []
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
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {lista}\nA lista de pares é {par}\nA lista de ímpares é {impar}')
print('=-'*15)
