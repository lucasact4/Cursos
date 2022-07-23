# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
print('=-'*15)
conf = str(input('Olá, para prosseguirmos me fale se você é do sexo Masculino ou Feminino!\nDigite (M ou F) para as respectivas opções: ')).upper()
while conf != 'M' and conf != 'F':
    conf = str(input('Opção Inválida! Tente novamente!\n(M - Masculino | F - Feminino): ')).upper()
if conf == 'F':
    print('Você é do sexo Feminino, portanto, não é obrigatório o alistamento militar!\nPrograma Finalizado!')
    quit()
from datetime import date
ano = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = ano - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {ano}.')
if idade < 18:
    print(f'Ainda faltam {18-idade} anos para o alistamento.\nSeu alistamento será em {ano+(18-idade)}')
elif idade == 18:
    print('É hora de se alistar IMEDIATAMENTE.')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade-18} anos.\nSeu alistamento foi em {ano-(idade-18)}')
print('=-'*15)
