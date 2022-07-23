# Faça um programa que leia um NÚMERO qualquer e mostre o seu FATORIAL.
# Ex:
# 5! = 5x4x3x2x1 = 120
print('=-'*15)
num = int(input('Digite um número para mostrar o seu FATORIAL: '))
if num == 2:
    print(f'Número fatorial de sí mesmo, portanto!\n\033[32m{num}', end='\033[31mx\033[m')
    fatorial = 2
elif num == 1:
    print(f'Número fatorial de sí mesmo, portanto!\n\033[32m{num}', end='\033[31mx\033[m')
    fatorial = 1
elif num == 0:
    print(f'Número fatorial de sí mesmo, portanto!\n\033[32m{num}', end='\033[31mx\033[m')
    fatorial = 1
else:
    print(f'\033[32m{num}', end='\033[31mx\033[m')
    ante = num - 1
    print(f'\033[32m{ante}', end='\033[31mx\033[m')
    fatorial = num * ante
    while ante != 2:
        ante = ante - 1
        print(f'\033[32m{ante}', end='\033[31mx\033[m')
        fatorial = fatorial * ante
print(f'\033[32m1\033[m = {fatorial}\033[m\nFatorial de \033[32m{num}\033[m é \033[32m{fatorial}\033[m')
# BONUS +
print('=-'*10)
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
print('=-'*15)
