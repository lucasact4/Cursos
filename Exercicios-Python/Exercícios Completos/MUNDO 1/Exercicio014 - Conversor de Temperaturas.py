# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
print('=-'*15)
tc = float(input('Digita a temperatura em graus Celcius: '))
tf = tc * 1.8 + 32
print('A temperatura {}° em graus Celcius será {:.1f}° em graus Fahrenheit.'.format(tc, tf))
#BONUS +
tf2 = 9 * tc / 5 + 32
print(f'Graus Fahrenheit: {tf2}°F')
print('=-'*15)
