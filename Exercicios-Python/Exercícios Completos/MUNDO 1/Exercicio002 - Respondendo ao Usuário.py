# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
print('=-'*15)
nome = input('Digite seu nome: ')
print('1º É um prazer te conhecer,', nome+'!')
#BONUS +
print('=-'*15)
print(f'2º É um prazer te conhecer, {nome}!')
print('3º É um prazer te conhecer, {}!'.format(nome))
print('=-'*15)
