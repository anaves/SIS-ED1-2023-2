def autenticacao(usuario, senha):
    if usuario == "admin" and senha == "*123#":
         return True
    else:
         return False
    
# main
if __name__ == "__main__":
    retorno = autenticacao('admin', '123')
    if retorno == True:
        print("acesso autorizado")
    else:
        print('acesso negado')