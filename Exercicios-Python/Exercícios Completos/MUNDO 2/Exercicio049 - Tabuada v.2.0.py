# Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
print('=-'*15)
n = int(input('Digite um número para ver sua tabuada: '))
print('-'*15)
for x in range(1, 11):
    print(f'{n} x {x:2} = {n*x:2}')
print('-'*15)
print('=-'*15)
