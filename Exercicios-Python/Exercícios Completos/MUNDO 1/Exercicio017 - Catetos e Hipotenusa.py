# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
# calcule e mostre o comprimento da hipotenusa.
# Formula: a² = b² + c²
# Ex: a=hipotenusa b=cateto c=cateto
# a² = 4² + 3²
# a² = 16 + 9
# a² = 25
# a  = √25
# a  = 5
print('=-'*15)
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
cal = co ** 2 + ca ** 2
print('A hipotenusa deste triângulo retângulo é {:.2f}.'.format(math.sqrt(cal)))
#BONUS +
hi = math.hypot(co, ca)
print('A hipotenusa deste triângulo retângulo é {:.2f}.'.format(hi))
print('A hipotenusa deste triângulo retângulo é {:.2f}.'.format(cal**(1/2)))
print('=-'*15)
