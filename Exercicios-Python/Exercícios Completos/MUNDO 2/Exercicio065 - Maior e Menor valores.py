# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado.
# No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual foi o MAIOR e o MENOR valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não CONTINUAR a digitar valores.
print('=-'*15)
num2 = []
cont = 1
nummaior = 0
nummenor = 0
print('Para prosseguir, digite números inteiros!')
while True:
    num = int(input(f'Digite o {cont}ª valor: '))
    if cont == 1:
        nummaior = num
        nummenor = num
    else:
        if num > nummaior:
            nummaior = num
        elif num < nummenor:
            nummenor = num
    num2.append(num)
    perg = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while perg != 'S' and perg != 'N':
        perg = str(input('Ação incorreta! Use (S - Sim | N - Não)\nDeseja continuar? [S/N]')).upper().strip()[0]
    if perg == 'N':
        break
    cont += 1
print(f'Média dos números digitados: {sum(num2)/len(num2):.2f}\nMaior deles: {nummaior}\nMenor deles: {nummenor}')
print('=-'*15)
