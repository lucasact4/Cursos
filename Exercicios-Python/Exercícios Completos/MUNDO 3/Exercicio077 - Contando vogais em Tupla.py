# Crie um programa que tenha uma TUPLA com VÁRIAS PALAVRAS(não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas VOGAIS.
print('=-'*15)
tupla = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
         'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
         'PRATICAR', 'TRABALHAR', 'MERCADO',
         'PROGRAMADOR', 'FUTURO')
for p in tupla:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('\nPrograma Finalizado!')
print('=-'*15)
