lista = ['Zacarias','Dede', 'Mussum', 'Didi']
print(lista[2])

notas = [[10,20,90],
         [30,40],
         [50,60,80,90],
         [70,80]]
print(notas[1])
print(notas[0])
print(notas[2][1])
# print(notas[2,1])  # erro
# mudar o valor 70 para 700
# notas[3][0]= 700
notas[3][0] = notas[3][0]*10
print(notas)
# linha 0 -> [10,20,90] -> coluna -> 0,1,2
# linha 1 -> [30,40] -> coluna -> 0,1
# linha 2 -> [50,60,80,90] -> coluna -> 0,1,2,3
# linha 3 -> [70,80] -> coluna -> 0,1
for linha in range(4):
    print(notas[linha])

# quandidade fixas!!!
print(f"Total de linhas: {len(notas)}")
for linha in range(len(notas)):
    # notas_aluno_tmp = notas[linha]
    for coluna in range(len(notas[linha])):
        print(notas[linha][coluna], end = '\t')
    print() # quebrar linha