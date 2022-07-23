# Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
# [ 1 ]Somar
# [ 2 ]Multiplicar
# [ 3 ]Maior
# [ 4 ]Novos Números
# [ 5 ]Sair do Programa
# Seu programa deverá realizar a operação solicitada em cada caso.
print('=-'*15)
from time import sleep
num1 = float(input('Digite o 1ª valor: '))
num2 = float(input('Digite o 2ª valor: '))
print('----- OPERAÇÕES -----\n[ 1 ]Somar\n[ 2 ]Multiplicar\n[ 3 ]Maior\n[ 4 ]Novos Números\n[ 5 ]Sair do Programa')
op = int(input('Digite o número da opeçação que deseja: '))
while op > 5 or op < 0:
    op = int(input('Operação inválida! Tente novamente!\nDigite o número da opeçação que deseja: '))
while op == 4:
    print('Solicitando novamente... ')
    sleep(1)
    num1 = float(input('Digite o 1ª valor: '))
    num2 = float(input('Digite o 2ª valor: '))
    op = int(input('Digite o novo número da opeçação que deseja: '))
if op == 1:
    print('Somando... ', end='')
    sleep(1)
    print(f'A soma entre os dois valores é: {num1+num2}')
elif op == 2:
    print('Multiplicando... ', end='')
    sleep(1)
    print(f'A multiplicação entre os dois valores é: {num1*num2}')
elif op == 3:
    print('Verificando... ', end='')
    sleep(1)
    if num1 > num2:
        print(f'O maior valor entre os dois números é: {num1}')
    elif num2 > num1:
        print(f'O maior valor entre os dois números é: {num1}')
    else:
        print(f'Os dois valores são iguais! {num1} e {num2}')
else:
    print('Saindo do programa... ', end='')
    sleep(1)
    print('Programa Fechado!')
print('=-'*15)
