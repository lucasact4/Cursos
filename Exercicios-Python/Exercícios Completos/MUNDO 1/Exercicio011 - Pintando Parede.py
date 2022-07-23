# Faça um programa que leia a largura e a altura de uma parede em metros.
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta, pinta uma área de 2m².
print('=-'*15)
l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
m = l * a
print('A parede mede {}m² e é necessário {} litros de tinta para pintá-la.'.format(m,m/2))
print('=-'*15)
