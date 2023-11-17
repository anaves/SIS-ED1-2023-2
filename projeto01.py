
def leitura(nome_arquivo: str):
    try:
        lista = []
        with open(nome_arquivo, 'r') as arquivo:
            arquivo.seek(0) # posicionando cursor no inicio
            for linha in arquivo:
                linha = linha.strip()
                if linha.isdigit():
                    valor =  float(linha)
                    lista.append(valor)
            return lista
    except Exception as e:
        print("Houve uma falha na abertura do arquivo")
        print(e)
        return None

def soma_valores_arquivo():
    valores = leitura("entrada.txt")
    print(valores)
    return sum(valores)

# EXERCICIOS 16/11/2023 
def maior_valor_arquivo():
    pass

def multiplica_valores_arquivo():
    pass

if __name__ == '__main__':
    resultado = soma_valores_arquivo()
    print(resultado)