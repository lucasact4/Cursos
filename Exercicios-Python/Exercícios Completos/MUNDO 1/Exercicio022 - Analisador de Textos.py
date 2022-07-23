# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiúsculas.
# > O nome com todas minúsculas.
# > Quantas letras ao todo (sem considerar espaços).
# > Quantas letras tem o primeiro nome
print('=-'*15)
nome = str(input('Digite o seu nome completo: '))
print('Formato maiúsculo: ', nome.upper())
print('Formato minúsculo: ', nome.lower())
tdl = nome.split()
tdl2 = ''.join(tdl)
print('Metodo 1: Total de letras', len(tdl2))
qlp = nome.split()
print('Quantas letras o primeiro nome ? ', len(qlp[0]))
#BONUS +
print('-'*15)
print('Seu nome tem ao todo {} palavras.'.format(len(tdl)-tdl.count('')))
print('Metodo 2: Total de letras', len(nome)-nome.count(' '))
print('Metodo 3: Total de letras {}'.format(len(nome)-nome.count(' ')))
print('Formato captalizado: ', nome.capitalize())
print('Formato title: ', nome.title())
print('=-'*15)
