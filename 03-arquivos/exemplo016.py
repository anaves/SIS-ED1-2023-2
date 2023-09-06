"""
produto - frutas
atributos: nome, codigo, preco, peso
    chave: codigo
    valor: nome, preco, peso
"""
import json
banco_dados = {}
opcao = 1
# preciso carregar o que estiver no arquivo
try:
    with open("base_dados/estoque.json", 'r') as arquivo:
        banco_dados = json.load(arquivo)
except:
    print('o arquivo nao existe')

while opcao != 4:
    print("="*10)
    print("1- Adicionar")
    print("2- Consultar por codigo")
    print("3- Consultar todos")
    print("4- Sair")
    opcao = int(input("Escolha a opcao: "))
    if opcao==1:
        print('-'*10)
        print("CADASTRO")
        codigo = input('Digite codigo: ')
        nome = input('Digite nome do produto: ')
        preco = float(input('Digite o preco do kg/unidade: '))
        banco_dados[codigo] = {"nome": nome, "preco": preco}
        # adicionar no arquivo
        with open("base_dados/estoque.json", "w") as arquivo:
            json.dump(banco_dados, arquivo, indent=4)
    elif opcao == 2:
        print('-'*10)
        print("CONSULTAR POR CODIGO")
    elif opcao == 3:
        print('-'*10)
        print("CONSULTAR TODOS")
        print(banco_dados)
    elif opcao == 4:
        print('-'*10)
        print('SAIR')
    else:
        print('-'*10)
        print('opcao invalida')
