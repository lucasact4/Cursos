# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
print('=-'*15)
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('SIM ! Os valores digitados das retas podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Isósceles!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
else:
    print('NÃO ! Os valores digitados das retas não podem formar um triângulo !')
print('=-'*15)
