opcao = 1
bd_estoque = []    #bd -> banco de dados
while opcao != 4:
    print('='*10)
    print("1- Adicionar")
    print('2- Consultar estoque')
    print('3- Consultar Valor Total do Estoque')
    print('4- Sair')
    opcao = int(input('Opcao >>>> '))
    if opcao == 1:
        print('-----Adicionar produto-----')
        codigo = int(input('Codigo: '))
        nome = input('Nome: ')
        descricao = input('Descricao: ')
        preco = float(input('Preco: R$ '))
        # adicionar a quantidade do produto no estoque
        produto = [codigo, nome, descricao, preco]
        bd_estoque.append(produto) # adicionar produto na lista estoque
        print('-----Adicionado com sucesso-----')
    elif opcao == 2:
        print('-----Estoque-----')
        # percorrer o bd
        print(bd_estoque)
        print('Codigo\tNome\tDescricao\tPreco')
        for prod in bd_estoque:
            print(prod[0],end='\t')   ### \t tab
            print(prod[1],end='\t')
            print(prod[2],end='\t')
            print(prod[3])
        print('-----Fim estoque-----')
    elif opcao == 3:
        pass    # implementar aqui
    elif opcao == 4:
        print('saindo....')
    else:
        print('opcao incorreta')