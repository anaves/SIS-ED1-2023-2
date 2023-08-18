perguntas = ("Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia $ para a vítima?","Já trabalhou com a vítima?")
positivo = 0
for pergunta in perguntas:
    resposta = input(pergunta + " Sim ou Nao >>> ")
    if resposta.lower() == 'sim':
        positivo = positivo + 1
if positivo == 2:
    print("Voce e' suspeito")
elif 3 <= positivo <= 4:
    print("Voce e' cumplice")
elif positivo == 5:
    print("Voce e' assassino")
else:
    print("Voce e' inocente")