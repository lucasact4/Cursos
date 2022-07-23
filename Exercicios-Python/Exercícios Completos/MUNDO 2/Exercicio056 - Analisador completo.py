# Desenvolva um programa que leia o nome, idade, e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.
print('=-'*15)
nome = []
idade = []
sexo = []
idademaior = 0
nomedomaior = ''
quantm = 0
for x in range(1, 5):
    print(f'----- {x}ª PESSOA -----')
    nom = str(input('Nome: '))
    nome.append(nom)
    idad = int(input('Idade: '))
    idade.append(idad)
    sex = str(input('Sexo [M/F]: ')).upper()
    while sex != 'M' and sex != 'F':
        sex = str(input(f'Opção incorreta!\nTente novamente com (M - Masculino | F - Feminino)!\nSexo [M/F]: ')).upper()
    sexo.append(sex)
    # OU if idad > idademaior and sex in 'Mm':
    if idad > idademaior and sex == 'M':
        idademaior = idad
        nomedomaior = nom
    if idad < 20 and sex == 'F':
        quantm += 1
media = sum(idade) / 4
print(f'Média de idade do grupo: {media}\nNome do homem mais velho com {idademaior} anos: {nomedomaior}\nTotal mulheres com menos de 20 anos: {quantm}')
print('=-'*15)
