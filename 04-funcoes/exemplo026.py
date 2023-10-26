def sem_parametros():
    # sem retorno
    print("comando 1")
    for i in range(10):
        print(i)
    print("comando 2")

def sem_parametros_com_retorno():
    print("comando 3")
    valor = input("digite s ou n: ")

    if valor == 's':
        return 100
    print("comando 4")
    return "comando 4"

def com_parametro_com_retorno(valor1, valor2):
    # funcao vai comparar se valor1 == valor2
    if valor1 == valor2:
        return "sao iguais"
    else:
        # poderia ter outros comandos
        return "sao diferentes"
    

def com_parametro_sem_retorno(valor1, valor2):
    # funcao vai comparar se valor1 == valor2
    global valor3 ### quebrei a regra, e defini valor3 global (levo pra fora)
    valor3 =  90
    if valor1 == valor2:
        print("sao iguais")
    else:
        # poderia ter outros comandos
        print("sao diferentes")
    print("dentro da funcao")
    print(valor1)
    
if __name__ == "__main__":
    print("inicio")
    # sem_parametros() # a funcao vai ser chamada (invocada)
    # numero = sem_parametros_com_retorno()
    # print("depois da chamada da funcao")
    # print(numero)
    # auxiliar = com_parametro_com_retorno(4.56,4.56)
    # print(auxiliar)
    # print("chamada 2")
    # auxiliar = com_parametro_com_retorno("chapeuzinho vermelho","chapeuzinho")
    # print(auxiliar)
    valor1 = 10
    valor3 = 0 
    com_parametro_sem_retorno(8,8)
    print("fora da funcao")
    print(valor1)
    print(valor3)

