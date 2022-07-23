# Crie um código em PYTHON que teste se o site PUDIM está acessível pelo computador usado.
import urllib
import urllib.request
print('=-'*15)
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')
    # print(site.read())
print('=-'*15)
