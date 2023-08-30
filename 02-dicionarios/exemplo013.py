"""
[codigo, nome, descricao, preco]
ATRIBUTOS OU CARACTERISTICAS-->codigo, nome, descricao, preco
CHAVE-> codigo
VALOR-> nome, descricao, preco. Vamos selecionar uma caracteristica nome. 

codigo: nome
"""
estoque = {}     # ED dicionario
opcao = 1
while opcao != 3:
    print('='*10)
    print('===MENU===')
    print('1- Adicionar')
    print('2- Consultar')
    print('3- Sair')
    opcao = int(input('>>>>'))
    if opcao == 1:
        codigo = input('Codigo: ')
        nome = input('Nome do produto: ')
        estoque[codigo] = nome
        print('adicionado com sucesso!')
    elif opcao == 2:  
        # vou informar o codigo e ele me retornar o nome
        codigo = input('Codigo desejado: ')
        # verificar se chave esta no estoque
        if codigo in estoque: 
            registro = estoque[codigo]
            print(f'REGISTRO RECUPERADO: {registro}')
        else:
            print('Produto nao encontrado')
    elif opcao == 3:
        print('saindo....')

