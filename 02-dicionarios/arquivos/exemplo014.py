# biblioteca para manipular arquivo json
import json  

reg01={'nome': "Chiclete", "idade": 10, "matriculado": True}
reg02={'nome': "Banana", "idade": 12, "matriculado": False}

dados = {"alunos":[reg01,reg02]}
print('dicionario python')
print(dados)
# dumps serializa o dicionario para json em uma string
json_str = json.dumps(dados)
print('string serializada - formato json')
print(json_str)
# dump serializa pra json e salvar em arquivo
with open('base_dados/dados.json', 'w') as json_file:
    json.dump(dados,json_file)