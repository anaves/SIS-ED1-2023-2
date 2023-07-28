# estrutura de dados
notas = [8.0,5.5,1.5]
#print(notas[3]) # indice invalido. Precisa ser 0, 1 ou 2
#tam = len(notas) # len -> length - comprimento da ED
#print(tam)
media = (notas[0]+notas[1]+notas[2])/3
print(f"media = {media:.2f}")

media2 = (notas[0]+notas[1]+notas[2])/len(notas)
print(f"media2 = {media2:.2f}")

print("---FOR---")
notas3 = [8.0,5.5,1.5,9,10]
# exemplo do for para percorrer a ED
soma = 0
for indice in range(len(notas3)):
    #print(indice, end='>>>>')
    #print(notas3[indice]) 
    soma = soma + notas3[indice]
    #print(f"soma parcial {soma}")
####
media = soma/len(notas3)
print(f'media final={media}')