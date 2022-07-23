# Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.
print('=-'*15)
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('O primeiro número que é {} é o MAIOR.'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O segundo número que é {} é o MAIOR.'.format(n2))
elif n3 > n2 and n3 > n1:
    print('O terceiro número que é {} é o MAIOR.'.format(n3))
if n1 == n2 and n1 != n3:
    print('O primeiro e o segundo número que é {}, são IGUAIS.'.format(n1))
elif n2 == n3 and n2 != n1:
    print('O segundo e o terceiro número que é {}, são IGUAIS.'.format(n2, n3))
elif n1 == n3 and n3 != n2:
    print('O primeiro e o terceiro número que é {}, são IGUAIS.'.format(n1, n3))
elif n1 == n2 and n1 == n2 and n2 == n3:
    print('Todos os números são IGUAIS.')
if n1 < n2 and n1 < n3:
    print('O primeiro número que é {} é o MENOR.'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O segundo número que é {} é o MENOR.'.format(n2))
elif n3 < n2 and n3 < n1:
    print('O terceiro número que é {} é o MENOR.'.format(n3))
#BONUS +
print('-'*15)
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior valor digitado foi {}.'.format(maior))
print('O menor valor digitado foi {}.'.format(menor))
print('=-'*15)
