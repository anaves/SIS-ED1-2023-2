"""
Utilizando listas ou tuplas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
perguntas = ("Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?")
positivos = 0
for per in perguntas:
    resposta = input(per + " sim ou nao >>>  ")
    if resposta.lower() == 'sim':
        positivos = positivos + 1
print('---------------------')
if positivos == 2:
    print('suspeita')
elif positivos == 3 or positivos == 4:
    print('cumplice')
elif positivos == 5:
    print('assassino')
else:
    print('inocente')
