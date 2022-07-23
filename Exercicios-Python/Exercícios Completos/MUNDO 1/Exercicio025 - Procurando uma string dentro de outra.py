# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('=-'*15)
nome = str(input('Digite o seu nome completo: ')).strip()
nome = nome.upper()
nome2 = 'SILVA' in nome
print('Possui algum SILVA no nome ? {}'.format(nome2))
print('=-'*15)
