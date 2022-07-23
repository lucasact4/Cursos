# Faça um programa que mostre a TABUADA de VÁRIOS NÚMEROS, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for NEGATIVO.
print('=-'*15)
cont = 1
print('---------- TABUADAS ----------\nPara sair digite um número negativo!\n------------------------------')
while True:
    num = int(input(f'Valor NEGATIVO para sair!\nDigite o valor da {cont}ª TABUADA: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')
    cont += 1
print('Programa finalizado!')
print('=-'*15)
