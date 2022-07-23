# Desenvolva um programa que leia QUATRO VALORES pelo TECLADO e guarde-os em uma TUPLA. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números PARES.
print('=-'*15)
tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foi: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
print('\nPrograma Finalizado!')
print('=-'*15)
