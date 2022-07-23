# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
print('=-'*15)
sal = float(input('Digite o valor do seu salário R$'))
if sal > 1250:
    sal2 = sal * 10 / 100 + sal
    print('O aumento foi de 10% e agora o seu salário é R${:.2f}.'.format(sal2))
else:
    sal3 = sal * 15 / 100 + sal
    print('O aumento foi de 15% e agora o seu salário é R${:.2f}.'.format(sal3))
print('=-'*15)
