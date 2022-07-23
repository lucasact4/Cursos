# Crie um programa onde o usuário possa digitar SETE VALORES NUMÉRICOS
# e cadastre-os em uma LISTA ÚNICA que mantenha separados os valores PARES e ÍMPARES.
# No final, mostre os valores pares e ímpares em ordem CRESCENTE.
print('=-'*15)
lista = [[], []]
for x in range(1, 8):
    num = int(input(f'Digite o {x}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f'Par {lista[0]}\nÍmpar {lista[1]}')
print('=-'*15)
