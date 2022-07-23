# Crie um programa que leia VÁRIOS NÚMERO inteiros pelo teclado.
# O programa só vai para quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA.
# No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles.
# (desconsiderando o flag)
print('=-'*15)
núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
print('=-'*15)
