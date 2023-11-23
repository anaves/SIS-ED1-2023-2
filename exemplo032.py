# criar uma matriz N X M preenchidas com zeros
# N -> numero de linha
# M -> numero de colunas
# E imprimir na forma de matriz
N = 20
M = 3

matriz = []
for linha in range(N):
    matriz.append([0]*M)

print(matriz)

print("------")
for linha in range(N):
    for coluna in range(M):
        print(matriz[linha][coluna],end='\t')
    print()

###### EXERCICIO #####
# ADICIONE ELEMENTOS DE FORMA ALEATORIA EM UMA MATRIZ NxM E RETORNE A QUANTIDADE DE NUMEROS PARES!