# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é MAIOR
# - O segundo valor é MAIOR
# - Não existem valor maior, os dois são iguais
print('=-'*15)
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
if n1 > n2:
    print('O primeiro valor é MAIOR')
elif n2 > n1:
    print('O segundo valor é MAIOR')
else:
    print('Não existem valor maior, os dois são iguais')
print('=-'*15)
