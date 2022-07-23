# Crie um programa que faça o computador jogar Jokenpô com você.
print('=-'*15)
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
nome = str(input('Eae ? tudo bem ? Para brincarmos de Jokenpô digite o seu nome: ')).upper()
print(f"Olá, {nome}! Deixa eu te explicar como funciona...\n[ 0 ] Equivale a Pedra\n[ 1 ] Equivale a Papel\n[ 2 ] Equivale a Tesoura\n Let's go ?")
perg = ''
while perg != 'NÃO' and perg != 'N' and perg != 'NAO' and perg != 'NA' and perg != 'NO':
    escolhap = int(input('Escolha uma opção: '))
    while escolhap != 2 and escolhap != 1 and escolhap != 0:
        escolhap = int(input('Opção Incorreta! Tente novamente!\nEscolha uma opção: '))
    escolhac = randint(0, 2)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    while escolhap == escolhac:
        escolhap = int(input(f'COMPUTADOR: Parece que empatamos {nome}! Vamos tentar novamente!\nDigite uma opção: '))
        while escolhap != 2 and escolhap != 1 and escolhap != 0:
            escolhap = int(input('Opção Incorreta! Tente novamente!\nDigite uma opção: '))
        escolhac = randint(0, 2)
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PO!!!')
    print(f'O computador escolheu {itens[escolhac]}\nVocê escolheu {itens[escolhap]}')
    if escolhap == 0 and escolhac == 1:
        print(f'{nome}: Pedra foi escolhido!\nCOMPUTADOR: Escolhi Papel! VENCI!')
    elif escolhap == 1 and escolhac == 2:
        print(f'{nome}: Papel foi escolhido!\nCOMPUTADOR: Escolhi Tesoura! VENCI!')
    elif escolhap == 2 and escolhac == 0:
        print(f'{nome}: Tesoura foi escolhido!\nCOMPUTADOR: Escolhi Pedra! VENCI!')
    elif escolhap == 1 and escolhac == 0:
        print(f'{nome}: Papel foi escolhido!\nCOMPUTADOR: Escolhi Pedra! Você VENCEU!')
    elif escolhap == 2 and escolhac == 1:
        print(f'{nome}: Tesoura foi escolhido!\nCOMPUTADOR: Escolhi Papel! Você VENCEU!')
    elif escolhap == 0 and escolhac == 2:
        print(f'{nome}: Pedra foi escolhido!\nCOMPUTADOR: Escolhi Tesoura! Você VENCEU!')
    perg = str(input('Deseja continuar ? Digite: (SIM ou NÃO): ')).upper()
    while perg != 'SIM' and perg != 'NÃO' and perg != 'N' and perg != 'S' and perg != 'NAO' and perg != 'SI' and perg != 'NA' and perg != 'NO' and perg != 'SI':
        perg = str(input('Opção Incorreta! Tente novamente!\nDeseja continuar ? Digite: (SIM ou NÃO): ')).upper()
print(f'Jogo Finalizado!\nObrigado por Jogar Sr. {nome}!')
print('=-'*15)
