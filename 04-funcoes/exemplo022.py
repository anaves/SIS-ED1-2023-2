# Forma 1
# import exemplo021
# retorno = exemplo021.autenticao()
# Forma 2
# import exemplo021 as ex
# retorno = ex.autenticao()
from exemplo021 import autenticacao

user = input('Digite login: ')
pwd = input('Digite senha: ')
retorno = autenticacao(user,pwd)
if retorno == True:
    print(f"Seja bem vindo(a) {user}")
else:
    print('login ou senha incorretos')