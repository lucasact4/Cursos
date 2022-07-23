# Reescreva a função LEIAINT() que fizemos no DESAFIO 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido.
# Aproveite e crie também uma função LEIAFLOAT() com a mesma funcionalidade.
print('=-'*15)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


# Programa Principal
n1 = leiaInt('Digite um número Inteiro: ')
n2 = leiaFloat('Digite um número Real: ')
print(f'Número Inteiro {n1}')
print(f'Número Real {n2}')
print('=-'*15)
