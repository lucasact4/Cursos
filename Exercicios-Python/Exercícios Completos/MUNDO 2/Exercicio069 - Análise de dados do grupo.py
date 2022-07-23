# Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 ANOS.
# B) Quantos HOMENS foram cadastrados.
# C) Quantas MULHERES tem menos de 20 ANOS.
print('=-'*15)
cont = 1
maior = 0
homens = 0
mulheres = 0
while True:
    print(f'----- {cont}ª PESSOA -----')
    idade = int(input('IDADE: '))
    if idade > 18:
        maior += 1
    while True:
        sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
        if sexo != 'M' and sexo != 'F':
            print('Opção inválida! Tente novamente com (M - Masculino | F - Feminino)!')
        else:
            break
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres += 1
    while True:
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if continuar != 'S' and continuar != 'N':
            print('Opção inválida! Tente novamente com (S - Sim | N - Não)!')
        else:
            break
    if continuar == 'N':
        break
    cont += 1
print(f'Total de pessoas com mais de 18 anos: {maior}\nAo todo temos {homens} homens cadastrados\nE temos {mulheres} mulheres com menos de 20 anos.')
print('=-'*15)
