# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
print('=-'*15)
print('Olá, vamos calcular o seu Índíce de Massa Corporal (IMC)?')
peso = float(input('Digite o seu peso (KG): '))
altura = float(input('Digite a sua altura (M): '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.2f}')
if imc < 18.5:
    print('Classificação: Abaixo do Peso.')
elif 18.5 <= imc < 25:
    print('Classificação: Peso Ideal.')
elif 25 <= imc < 30:
    print('Classificação: Sobrepeso.')
elif 30 <= imc < 40:
    print('Classificação: Obesidade.')
elif imc >= 40:
    print('Classificação: Obesidade Mórbida, CUIDADO!')
print('=-'*15)
