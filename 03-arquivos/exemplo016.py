# encoding: utf-8
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

while opcao != 5:
    print("="*10)
    print("1- Adicionar")
    print("2- Consultar por codigo")
    print("3- Consultar todos")
    print("4- Atualizar precos")
    print("5- Sair")
    opcao = int(input("Escolha a opcao: "))
    if opcao==1:
        print('-'*10)
        print("CADASTRO")
        codigo = input('Digite codigo: ')
        nome = input('Digite nome do produto: ')
        preco = float(input('Digite o preco do kg/unidade: '))
        banco_dados[codigo] = {"nome": nome, "preco": preco}
        
    elif opcao == 2:
        print('-'*10)
        print("CONSULTAR POR CODIGO")
        produto = banco_dados[codigo]
        print(produto['nome'])
        print(banco_dados[codigo]['nome'])
    elif opcao == 3:
        print('-'*10)
        print("CONSULTAR TODOS")
        print(banco_dados)
    elif opcao == 4:
        taxa = float(input('Digite taxa de acrescimo ou desconto(-): '))
        for codigo in banco_dados:
            produto = banco_dados[codigo]
            preco =  produto['preco']
            novo_preco = preco*(1+taxa/100)
            # atualizar novo preco
            produto['preco'] = round(novo_preco, 2)       
    elif opcao == 5:
        # abrir arquivo e salva as mudancas
        with open("base_dados/estoque.json", "w", encoding='utf8') as arquivo:
            json.dump(banco_dados, arquivo, indent=4)
        arquivo.close()
        print('-'*10)
        print('SAIR')
    else:
        print('-'*10)
        print('opcao invalida')
