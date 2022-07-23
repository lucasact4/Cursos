# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
print('=-'*15)
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('Analisando o valor {},\nO seu dobro é {},\nO seu triplo é {},\nE sua raiz quadrada é {:.2f}.'.format(n,d,t,r))
#BONUS +
print('=-'*15)
print('Analisando o valor {},\nO seu dobro é {},\nO seu triplo é {},\nE sua raiz quadrada é {:.2f}.'.format(n,(n*2),(n*3),(n**(1/2))))
print('=-'*5)
print('Analisando o valor {},\nO seu dobro é {},\nO seu triplo é {},\nE sua raiz quadrada é {:.2f}.'.format(n,(n*2),(n*3),pow(n, (1/2))))
print('=-'*15)
