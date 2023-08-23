"""
Escreva um programa que remova todos os elementos da primeira lista que também estão presentes na segunda lista.
A = [4,5,2,3,1,2,5] = {1,2,3,4,5}
B = [3,1,5,8,9]     = {1,3,5,8,9}
Resultado = {2,4}
"""
A = [4,5,2,3,1,2,5]
B = [3,1,5,8,9]
cA = set(A)
cB = set(B)
# trazer cA-cB
cR = cA.difference(cB)
print(cR)