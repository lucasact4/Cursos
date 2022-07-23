# Faça um programa que calcule a soma entre todos os NÚMEROS ÍMPARES que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.
print('=-'*15)
soma = 0
c = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        c += 1
        soma += x
print(f'A soma de todos os {c} valores solicitados é {soma}')
print('=-'*15)
