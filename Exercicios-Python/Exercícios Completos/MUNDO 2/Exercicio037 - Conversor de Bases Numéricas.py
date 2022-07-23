# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a
# BASE DE CONVERSÃO:
# - 1 para BINÁRIO
# - 2 para OCTAL
# - 3 para HEXADECIMAL
print('=-'*15)
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
while opção != 1 and opção != 2 and opção != 3:
    opção = int(input('Opção Incorreta! Tente novamente!\nSua opção: '))
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
else:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
print('=-'*15)
