# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
# Seu programa deverá ler um número pelo teclado (ENTRE 0 E 20) e mostrá-lo por extenso.
print('=-'*15)
tupla = ("Zero", "Um", "Dois", "Três", "Quatro",
         "Cinco", "Seis", "Sete", "Oito", "Nove",
         "Dez", "Onze", "Doze", "Treze", "Catroze",
         "Quinze", "Dezesseis", "Dezessete", "Dezoito",
         "Dezenove", "Vinte")
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Número escrito por extenso: {tupla[num]}')
while True:
    while True:
        teste = str(input('Quer tentar novamente ? (S/N)')).upper().strip()[0]
        if teste == 'N':
            break
        elif teste == 'S':
            while True:
                num = int(input('Digite um número entre 0 e 20: '))
                if 0 <= num <= 20:
                    break
                print('Tente novamente. ', end='')
            print(f'Número escrito por extenso: {tupla[num]}')
    if teste == 'N':
        print('Programa Encerrado!')
        break
print('=-'*15)
