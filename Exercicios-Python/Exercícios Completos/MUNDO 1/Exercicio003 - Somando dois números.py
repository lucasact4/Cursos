# Crie um programa que leia dois números e mostre a soma entre eles.
print('=-'*15)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre os números digitados são:', s, '!')
#BONUS +
print('=-'*15)
print('A soma entre {} e {} é: {} !'.format(n1,n2,s))
print(f'A soma entre {n1} e {n2} é: {s} !')
print('=-'*15)
