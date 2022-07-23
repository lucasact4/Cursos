# Crie um programa onde o usuário possa digitar vários VALORES NÚMERICOS e cadastre-os em uma LISTA.
# Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO.
# No final, serão exibido todos os VALORES ÚNICOS digitados, em ORDEM CRESCENTE.
print('=-'*15)
lista = []
x = 1
while True:
    num = int(input(f'Digite o {x}ª valor númerico: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if cont == 'S':
            break
        if cont == 'N':
            break
    if cont == 'N':
        break
    x += 1
lista.sort()
print(f'Você digitou os valores {lista}')
print('=-'*15)
