# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.
print('=-'*15)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('SIM ! Os valores digitados das retas podem formar um triângulo !')
else:
    print('NÃO ! Os valores digitados das retas não podem formar um triângulo !')
#BONUS +
print('-'*15)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('SIM ! Os valores digitados das retas podem formar um triângulo !')
else:
    print('NÃO ! Os valores digitados das retas não podem formar um triângulo !')
print('=-'*15)
