# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A".
# > Em que posição ela aparece a primeira vez.
# > Em que posição ela aparece a última vez.
print('=-'*15)
frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('Quantas vezes aparece a letra A ? {}'.format(frase.count('A')))
print('Primeira posição ? {}'.format(frase.find('A')+1))
print('Última posição ? {}'.format(frase.rfind('A')+1))
print('-'*15)
# BONUS +
print('A frase é {} e quantas vezes aparece a letra A ?'.format(frase.title()))
print('Primeira posição no Sistema Python: {}'.format(frase.find('A')))
print('Última posição no Sistema Python: {}'.format(frase.rfind('A')))
print('=-'*15)
