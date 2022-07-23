# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
print('=-'*15)
from random import shuffle
n1 = str(input('Digite o nome do primeiro aluno(a): '))
n2 = str(input('Digite o nome do segundo aluno(a): '))
n3 = str(input('Digite o nome do terceiro aluno(a): '))
n4 = str(input('Digite o nome do quarto aluno(a): '))
mylist = [n1, n2, n3, n4]
shuffle(mylist)
print('A ordem de apresentação é {}.'.format(mylist))
print('=-'*15)
