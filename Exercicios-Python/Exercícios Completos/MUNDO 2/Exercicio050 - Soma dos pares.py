# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
print('=-'*15)
mult = []
c = 0
for x in range(1, 7):
    n = int(input(f'Digite o {x}º número inteiro: '))
    if n % 2 == 0:
        mult.append(n)
        c += 1
    else:
        print('Número ÍMPAR, Desconsiderano-o!')
print(f'Soma dos {c} números pares: {sum(mult)}')
print('=-'*15)
