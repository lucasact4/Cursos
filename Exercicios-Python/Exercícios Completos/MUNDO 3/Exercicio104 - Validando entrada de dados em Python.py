# Crie um programa que tenha a FUNÇÃO LEIAINT(), que vai funcionar de forma semelhante
# à função INPUT() do Python, só que fazendo a VALIDAÇÃO para aceitar apenas um valor númerico.

# EX:
# n = leiaInt('Digite um n')
print('=-'*15)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
print('=-'*15)
