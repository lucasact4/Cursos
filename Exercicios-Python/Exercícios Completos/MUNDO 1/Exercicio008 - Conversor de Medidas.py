# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.
print('=-'*15)
d = float(input('Digite uma distância em metros: '))
print('{} km'.format(d/1000))
print('{} hm'.format(d/100))
print('{} dam'.format(d/10))
print('{} dm'.format(d*10))
print('{} cm'.format(d*100))
print('{} mm'.format(d*1000))
#BONUS +
print('=-'*15)
cm = d * 100
mm = d * 1000
print(f'A medida de {d}m corresponde a {cm:.0f}cm e {mm:.0f}mm')
print('=-'*15)
