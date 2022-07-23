# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
print('=-'*15)
import random
n1 = str(input('Digite o nome do primeiro aluno(a): '))
n2 = str(input('Digite o nome do segundo aluno(a): '))
n3 = str(input('Digite o nome do terceiro aluno(a): '))
n4 = str(input('Digite o nome do quarto aluno(a): '))
mylist = [n1, n2, n3, n4]
ran = random.choices(mylist, weights = [1, 1, 1, 1], k = 1)
print('O primeiro aluno que irá apagar o quadro é {}.'.format(ran))
#BONUS +
escolhido = random.choice(mylist)
print('O segundo aluno que irá apagar o quadro é {}.'.format(escolhido))
print('=-'*15)
