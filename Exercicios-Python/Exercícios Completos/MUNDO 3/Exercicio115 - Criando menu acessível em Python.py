# Crie um pequeno SISTEMA MODULARIZADO que permita cadastrar
# pessoas pelo seu NOME e IDADE em um arquivo de texto simples.
# O sistema só vai ter 2 OPÇÕES: CADASTRAR uma nova pessoa e LISTAR todas as pessoas cadastradas.
from modules.lib.arquivo import *
from modules.lib.interface import *
from time import sleep
print('=-'*15)

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado!')
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[31mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
print('=-'*15)
