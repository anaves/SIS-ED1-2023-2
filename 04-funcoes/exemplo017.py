##  exemplo de uma funcao que calcula a media

def media(lista):
    soma = 0
    for e in lista:
        # acumula soma de cada elemento e
        soma = soma + e
    print(lista)
    med = soma/len(lista)
    print(f"a media eh igual: {med}")

if __name__=='__main__':
    minha_lista=[1,2,3,4,5]
    print('ANTES DE CHAMAR A FUNCAO')
    media(minha_lista)
    media([10,20,30,40,50])