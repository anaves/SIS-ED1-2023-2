"""
Crie duas listas em python, uma para armazenar o nome e outra lista para armazenar a idade de 5 pessoas. Posteriormente indique quais pessoas tem 18 anos ou mais e quantas pessoas sao menores de idade.
Ex: 
Jose, 10 anos
Joaquim, 19 anos
Jailton, 30 anos
Juarez, 5 anos
Joao, 18 anos
--> sao maiores de idade: Joaquim, Jailton, Joao
--> sao menores de idade: Jose, Juarez 
"""
nomes = []
idades = []
n_pessoas =  5
for i in range(n_pessoas):
    nomes.append(input("Digite o nome: "))
    tmp = int(input(f"Digite a idade {nomes[i]}: "))
    idades.append(tmp)

maiores = "--> sao maiores de idade: "
menores = "--> sao menores de idade: "
for j in range(len(idades)):
    if idades[j] >= 18:
        tmp = nomes[j]
        maiores = maiores + tmp + ", "
    else:
        tmp = nomes[j]
        menores = menores + tmp + ", "
print("--------------------------------")
print(maiores[:-2])
print(menores[:-2])