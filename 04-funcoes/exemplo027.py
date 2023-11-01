
def aniversario(idade):
    nova_idade = idade + 1
    return nova_idade


def aniversario_v2(outra_idade):
    print('<< in')
    print(outra_idade)
    outra_idade = outra_idade + 1
    print('<< in 2')
    print(outra_idade)

n_idade = aniversario(18)
# print(nova_idade) # nova_idade eh variavel local
# print(n_idade) # assim funciona

outra_idade = 20
aniversario_v2(outra_idade)
print('>> out')
print(outra_idade)