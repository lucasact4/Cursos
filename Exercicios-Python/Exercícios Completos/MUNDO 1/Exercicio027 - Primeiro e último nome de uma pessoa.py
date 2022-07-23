# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza
print('=-'*15)
nome = str(input('Digite o seu nome completo: '))
pn = nome.split()
print('Primeiro nome: {}'.format(pn[0]))
print('Último nome: {}'.format(pn[-1]))
# BONUS +
print('Excluindo espaços existentes da direita: {}'.format(nome.rstrip()))
print('Excluindo espaços existentes da esquerda: {}'.format(nome.lstrip()))
print('Excluindo espaços existentes da direita e da esquerda: {}'.format(nome.strip()))
first = nome.split()[0]
last = nome.split()[-1]
print('Primeiro nome: {}'.format(first))
print('Último nome: {}'.format(last))
print('-'*5)
# OUTRO METODO
print('Último nome: {}'.format(pn[len(pn)-1]))
print('=-'*15)
