# Crie um programa que leia VÁRIOS NÚMERO inteiros pelo teclado.
# O programa só vai para quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA.
# No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles.
# (desconsiderando o flag)
print('=-'*15)
num2 = []
cont = 1
print('Para prosseguir, digite números inteiros! Caso deseja finalizar, digite o valor 999!')
while True:
    num = int(input(f'Digite o {cont}ª valor: '))
    if num == 999:
        break
    num2.append(num)
    cont += 1
print(f'Total de números digitados: {len(num2)}\nSoma entre eles: {sum(num2)}')
print('=-'*15)
