import json

# 'r' - abrir pra leitura
# 'w' - abrir para escrita (sobrescreve)
# 'a' - abrir para escrita (anexa no fim)
with open('base_dados/dados.json', 'r') as arquivo:
    registros = json.load(arquivo)

print(registros)
print(type(registros))