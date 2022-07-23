# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
print('=-'*15)
n = int(input('Digite um número: '))
a = n-1
s = n+1
print('Analisando o valor {}, o seu antecessor é {} e o seu sucessor é {}'.format(n,a,s))
#BONUS +
print('=-'*15)
print(f'Analisando o valor {n}, o seu antecessor é {a} e o seu sucessor é {s}')
print('Analisando o valor {}, o seu antecessor é {} e o seu sucessor é {}'.format(n,(n-1),(n+1)))
print('Analisando o valor', n, ', o seu antecessor é', n-1, 'e o seu sucessor é', n+1)
print('=-'*15)
